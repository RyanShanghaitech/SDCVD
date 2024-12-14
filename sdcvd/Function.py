from numpy import *
from matplotlib.pyplot import *
from matplotlib.axes import Axes
from scipy.spatial import Voronoi, ConvexHull, voronoi_plot_2d

def getVol(lstArrK:list[ndarray], ax:Axes|None=None) -> ndarray:
    """
    description:
    Calculate compensation factor by Voronoi diagram.

    parameters:
    `lstArrK`: list of trajectory: (trj, pt, ax)
    `ax`: axes to be plot on, can be None

    return:
    array of compensating factor to be mutiplied with kspace data
    """
    nPE = len(lstArrK)
    arrK = concatenate(lstArrK, axis=0)
    arrVol = zeros(arrK.shape[0])
    try:
        vor = Voronoi(arrK) #, qhull_options=f"C-1e-15 QbB Q12")
        # C-1e-15 prevents the precision error compared to C-0, and faster than Qx, QbB normalize the input to reduce precision error, Q12 ignore wide facet error, default"Qbb Qc Qz"
        # note: 1e-16 and 1e-8 is the precision limit of float64 and float32
        # note: we don't normalize ourselves, it will still cause error
        # print("[SUCC] Voronoi")
        for iPt in range(vor.npoints):
            if vor.regions[vor.point_region[iPt]][0] == -1:
                arrVol[iPt] = 0
            else:
                arrVol[iPt] = ConvexHull(vor.vertices[vor.regions[vor.point_region[iPt]]]).volume

            # handle the case when multiple points share the same cell
            arrVol[iPt] /= argwhere(vor.point_region == vor.point_region[iPt]).size

        if ax != None and vor.ndim == 2: voronoi_plot_2d(vor, ax)
    except Exception as e:
        print(f"[ERRO] Voronoi")
        print(e)

    lstArrVol = [None]*nPE
    idxArrVol = 0
    for iPE in range(nPE):
        nRO = lstArrK[iPE].shape[0]
        lstArrVol[iPE] = arrVol[idxArrVol:idxArrVol+nRO]
        idxArrVol += nRO
    return lstArrVol
