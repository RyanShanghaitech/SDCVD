from numpy import *

def fixDs(lstDs:ndarray, idxFix:int) -> ndarray:
    """
    description:
    Fix Ds at the boundary of trajectory due to inprecise of Voronoi diagram.

    parameters:
    `lstDs`: list of Ds
    `idxFix`: from what index to fix Ds

    return:
    list of fixed Ds
    """
    assert(lstDs.ndim <= 2)
    if lstDs.ndim == 1: lstDs = lstDs.reshape(1, -1)
    numTrj, numPt = lstDs.shape
    for idxPt in range(idxFix + 1, numPt):
        lstDs[:,idxPt] = 2*lstDs[:,idxPt-1] - lstDs[:,idxPt-2]
    return lstDs
