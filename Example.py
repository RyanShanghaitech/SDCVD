from numpy import *
from matplotlib.pyplot import *
from scipy.spatial import voronoi_plot_2d
from sdcvd import *
import time

# read trajectory
arrK = load(f"./Resource/K.npy")
nPE, nRO, _ = arrK.shape

# calculate DCF by Voronoi diagram
t = time.time()

fig = figure(figsize=(6,6), dpi=150)
ax = fig.add_subplot(222)
lstArrDcf = getDcf([*arrK], ax, dict(show_vertices=0, line_width=0.5, point_size=4))
ax.axis("equal")
ax.set_ylim(0.20,0.25)
ax.set_xlim(0.20,0.25)
ax.set_title("Voronoi Diagram")

lstArrDcf = fixDcf(lstArrDcf, 0.9)

t = time.time() - t
print(f"time elapsed: {t:.3f}s")

# plot trajectory and DCF
ax = fig.add_subplot(221)
for iPE in range(nPE):
    ax.plot(arrK[iPE,:,0], arrK[iPE,:,1], ".-")
ax.axis("equal")
ax.set_title("Spiral2D trajectory")

ax = fig.add_subplot(212)
for arrDcf in lstArrDcf:
    ax.plot(arrDcf.reshape([-1]), ".-")
ax.grid("on")
ax.set_title("DCF")

show()