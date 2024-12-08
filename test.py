from numpy import *
from matplotlib.pyplot import *
import mrtrjgen
import sdcvd

nPix = 1024
fov = 0.5
nSp = 32
dtGrad = 10e-6
dtADC = 1e-6

# get trajectory
lstArrK = []
for iSp in range(nSp):
    tht0 = (2*pi)*(iSp/nSp)
    _, arrG = mrtrjgen.genSpiral2D(0.5/(2*pi)/(nPix/2)*nSp, 0, tht0, 0.5, 100*42.58e6*fov/nPix, ov=10)
    arrK, _ = mrtrjgen.intpTraj(arrG, dtGrad, dtADC)
    lstArrK.append(arrK)
arrK = array(lstArrK)
nPE, nRO, _ = arrK.shape

save(f"./Resource/arrK_{nPix}.npy", arrK)