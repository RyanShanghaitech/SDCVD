from numpy import *
from matplotlib.pyplot import *
from scipy.spatial import voronoi_plot_2d
from sdcvd import *

sizIm = 128

# generate radial trajectory
lstKxKy = load("./Resource/trjSpiral.npy")
numSp, numPt, _ = lstKxKy.shape

# calculate Ds by Voronoi diagram
lstDs, objVor = getDs(lstKxKy.reshape([-1,2]))
lstDs = fixDs_Spiral(lstDs, numSp, numPt, int(numPt*0.95))

# plot voronoi diagram
voronoi_plot_2d(objVor)
axis("equal"); title("Voronoi diagram"); xlim([-0.55, 0.55]); ylim([-0.55, 0.55])

# plot trajectory and Ds
figure()
subplot(121)
scatter(lstKxKy.reshape([-1,2])[:,0], lstKxKy.reshape([-1,2])[:,1])
axis("equal"); title("Radial trajectory")
subplot(122)
plot(lstDs.reshape([-1]), marker="."); title("Ds")

show()