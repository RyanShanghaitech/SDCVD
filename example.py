from numpy import *
from matplotlib.pyplot import *
from scipy.spatial import voronoi_plot_2d
from sdcvd import *

sizIm = 128

# generate radial trajectory
lstTht = linspace(0, 2*pi, ceil((pi*1)/(1/sizIm)).astype(int64), endpoint=False)
lstRho = linspace(0, 0.5, int64(sizIm/2), endpoint=False)
lstKxKy = zeros([lstTht.size, lstRho.size, 2], dtype=float64)
print(lstKxKy.shape)
idxKxKy = 0
for idxTht in range(lstTht.size):
    for idxRho in range(lstRho.size):
        lstKxKy[idxTht,idxRho,:] = [lstRho[idxRho]*cos(lstTht[idxTht]), lstRho[idxRho]*sin(lstTht[idxTht])]

# calculate Ds by Voronoi diagram
lstDs, objVor = getDs(lstKxKy.reshape([-1,2]))

# plot voronoi diagram
voronoi_plot_2d(objVor)
axis("equal"); title("Voronoi diagram"); xlim([0.45, 0.55]); ylim([-0.05, 0.05])

# plot trajectory and Ds
figure()
subplot(121)
plot(lstKxKy[:,:,0].flatten(), lstKxKy[:,:,1].flatten(), marker=".")
axis("equal"); title("Radial trajectory")
subplot(122)
plot(lstDs, marker="."); title("Ds"); xlim([0, sizIm*4])

show()