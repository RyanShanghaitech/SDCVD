from numpy import *
from . import *

def fixCompFac(arrCompFac:ndarray, iRO_Fix:int) -> ndarray:
    """
    description:
    Fix compensation factor at the boundary of trajectory due to inprecise of Voronoi diagram.

    parameters:
    `lstDs`: list of Ds
    `idxFix`: from what index to fix Ds

    return:
    list of fixed compensation factor
    """
    assert(arrCompFac.ndim <= 2)
    if arrCompFac.ndim == 1: arrCompFac = arrCompFac[newaxis,:]
    iRO_Fix = int(iRO_Fix)
    nPE, nRO = arrCompFac.shape
    dCompFac = (arrCompFac[:,iRO_Fix] - arrCompFac[:,iRO_Fix-(nRO//10)])/(nRO//10)
    for iRO in range(iRO_Fix + 1, nRO):
        arrCompFac[:,iRO] = arrCompFac[:,iRO-1] + dCompFac
    return arrCompFac

def getCompFac_Seg(arrK:ndarray, drho:int|float, kmax:int|float=0.5) -> ndarray:
    """
    description:
    get sampling density compensation factor by segmenting the trajectory, to save memory

    parameters:
    `arrK`: trajectory: (pt, ax)
    `drho`: length of segment of rho, suggested to be nyquist interval

    return:
    compensation factor
    """
    assert arrK.ndim==2, "arrK should be (pt, ax)"
    nPt, nAx = arrK.shape
    arrRho = sqrt((arrK**2).sum(axis=1))
    arrCompFac = zeros([nPt])
    for rho in arange(0,kmax,drho):
        print(f"rho = {rho}")
        rhoMin = rho
        rhoMax = rho + drho
        arrIdx, = where((arrRho>=rhoMin) & (arrRho<rhoMax))
        _arrIdx, = where((arrRho>=rhoMin-1*drho) & (arrRho<rhoMax+1*drho))
        _arrCompFac = getCompFactor(arrK[_arrIdx,:][newaxis,:,:]).squeeze()
        arrCompFac[arrIdx] = _arrCompFac[[(idx in arrIdx) for idx in _arrIdx]]
    
    return arrCompFac