from numpy import *
from matplotlib.pyplot import *
from matplotlib.axes import Axes
from scipy.spatial import Voronoi, ConvexHull, voronoi_plot_2d

def getDcf(lstArrK:list[ndarray], ax:Axes|None=None) -> ndarray:
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
        vor = Voronoi(arrK) # , qhull_options="")
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
