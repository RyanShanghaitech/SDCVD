from numpy import *
from matplotlib.pyplot import *
from scipy.spatial import voronoi_plot_2d
from sdcvd import *
import time

nPix = 1024

# read trajectory
arrK = load(f"./Resource/arrK_{nPix}.npy")
nPE, nRO, _ = arrK.shape

# calculate aera by Voronoi diagram
t = time.time()
arrCompFac = getCompFac_Seg(arrK.reshape(-1,2), 2/nPix).reshape(nPE, nRO)
# arrCompFac = getCompFactor(arrK)
arrCompFac = fixCompFac(arrCompFac, nRO*0.9)
t = time.time() - t
print(f"time elapsed: {t}s")

# plot trajectory and Ds
figure()
subplot(121)
for iPE in range(nPE): plot(arrK[iPE,:,0], arrK[iPE,:,1], ".-")
axis("equal"); title("Spiral2D trajectory")
subplot(122)
plot(arrCompFac.reshape([-1]), ".-"); title("Dv")

show()