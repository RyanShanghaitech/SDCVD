from numpy import *
from matplotlib.pyplot import *
from scipy.spatial import voronoi_plot_2d
from sdcvd import *
import time

nPix = 128
# nPix = 1024

# read trajectory
arrK = load(f"./Resource/K_{nPix}.npy")
nPE, nRO, _ = arrK.shape

# calculate aera by Voronoi diagram
t = time.time()
fig = figure()
ax = fig.add_subplot(111)
lstArrVol = getVol([*arrK], ax)
ax.axis("equal")
ax.set_ylim(-0.5,0.5)
ax.set_xlim(-0.5,0.5)
lstArrVol = fixVol(lstArrVol, 0.9)
t = time.time() - t
print(f"time elapsed: {t}s")

# plot trajectory and Ds
figure()
subplot(121)
for iPE in range(nPE): plot(arrK[iPE,:,0], arrK[iPE,:,1], ".-")
axis("equal"); title("Spiral2D trajectory")
subplot(122)
for arrVol in lstArrVol:
    plot(arrVol.reshape([-1]), ".-"); title("vol")

show()