from numpy import *
from matplotlib.pyplot import *
from packSDCVD.modSDCVD import funGetDs
from scipy.spatial import voronoi_plot_2d

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
figure()
plot(lstKxKy[:,:,0].flatten(), lstKxKy[:,:,1].flatten(), marker=".")
axis("equal")
title("Radial trajectory")

# calculate Ds by Voronoi diagram
lstDs, objVor = funGetDs(lstKxKy.reshape([-1,2]))
voronoi_plot_2d(objVor)
axis("equal")
title("Voronoi diagram")

show()