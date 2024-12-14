from numpy import *
from . import *

def fixVol(lstArrVol:list[ndarray], fFix:float) -> ndarray:
    """
    description:
    Fix compensation factor at the boundary of trajectory due to inprecise of Voronoi diagram.

    parameters:
    `lstArrVol`: list of volume
    `fFix`: from what fraction of index to fix Ds, need to be 0~1

    return:
    list of fixed compensation factor
    """
    nPE = len(lstArrVol)
    for iPE in range(nPE):
        nRO = lstArrVol[iPE].shape[0]
        iRO_Fix = int(fFix*nRO)
        dVol = (lstArrVol[iPE][iRO_Fix] - lstArrVol[iPE][iRO_Fix-(nRO//10)])/(nRO//10)
        lstArrVol[iPE][iRO_Fix:] = lstArrVol[iPE][iRO_Fix] + dVol*arange(nRO-iRO_Fix)
    return lstArrVol
