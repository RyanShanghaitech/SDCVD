from numpy import *
from matplotlib.pyplot import *
from scipy.spatial import Voronoi, ConvexHull, voronoi_plot_2d

def getCompFactor(arrK:ndarray) -> ndarray:
    """
    description:
    Calculate compensation factor by Voronoi diagram.

    parameters:
    `arrK`: ndarray - trajectory: (trj, pt, ax)

    return:
    array of compensating factor to be mutiplied with rawdata
    """
    assert arrK.ndim == 3, "arrK shouold be (trj, pt, ax)"
    dimTrj = arrK.shape[:-1]
    arrK = arrK.reshape((-1,arrK.shape[-1]))
    kmax = sqrt((arrK**2).sum(axis=1)).max() # useful for denormalization
    arrVol = zeros(arrK.shape[0])
    try:
        vor = Voronoi(arrK, qhull_options=f"C-1e-15 QbB Q12") # C-1e-15 prevents the precision error compared to C-0, and faster than Qx, QbB normalize the input to reduce precision error, Q12 ignore wide facet error, default"Qbb Qc Qz"
        # note: 1e-16 and 1e-8 is the precision limit of float64 and float32
        # note: we don't normalize ourselves, it will still cause error
        # print("[SUCC] Voronoi")
        for idxPt in range(vor.npoints):
            if vor.regions[vor.point_region[idxPt]][0] == -1:
                arrVol[idxPt] = 0
            else:
                arrVol[idxPt] = ConvexHull(vor.vertices[vor.regions[vor.point_region[idxPt]]]).volume

            # handle the case when multiple points share the same cell
            arrVol[idxPt] /= argwhere(vor.point_region == vor.point_region[idxPt]).size

        # if vor.ndim == 2:
        #     voronoi_plot_2d(vor)
        #     axis("equal")
        #     xlim([-0.5,0.5])
        #     ylim([-0.5,0.5])
    except Exception as e:
        print(f"[ERRO] Voronoi")
        print(e)

    arrVol *= (kmax/0.5)**arrK.shape[-1] # denormalization
    return arrVol.reshape(dimTrj)
