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
    lstD2s = lstDs[:,idxFix] - lstDs[:,idxFix-1]
    for idxPt in range(idxFix, numPt):
        lstDs[:,idxPt] = lstDs[:,idxPt-1] + lstD2s
    return lstDs.reshape([-1])
