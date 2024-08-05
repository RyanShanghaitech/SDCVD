from numpy import *

def fixDs_Spiral(lstDs:ndarray, numSp:int, numPt:int, idxFix:int) -> ndarray:
    """
    description:
    Fix Ds at the boundary of spiral due to inprecise of Voronoi diagram.

    parameters:
    `lstDs`: list of Ds
    `numSp`: number of spirals
    `numPt`: number of points in each spiral
    `idxFix`: from what index to fix Ds

    return:
    list of fixed Ds
    """
    assert(lstDs.ndim == 1)
    lstDs = lstDs.reshape([numSp, numPt])
    lstD2s = lstDs[:,idxFix] - lstDs[:,idxFix-1]
    for idxPt in range(idxFix, numPt):
        lstDs[:,idxPt] = lstDs[:,idxPt-1] + lstD2s
    return lstDs.reshape([-1])
