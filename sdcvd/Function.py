from numpy import *
from scipy.spatial import Voronoi, voronoi_plot_2d

def _getPolygonAera(lstVertice):
    # Ensure the vertices are a NumPy array for efficient computation
    lstVertice = asarray(lstVertice)
    
    # Extract x and y coordinates
    x = lstVertice[:,0]
    y = lstVertice[:,1]
    
    # Compute the area using the Shoelace formula
    area = 0.5*abs(dot(x, roll(y,1)) - dot(y, roll(x,1)))
    return area

def getDs(traj:ndarray) -> tuple[ndarray, Voronoi]:
    """
    description:
    Calculate Ds by Voronoi diagram.

    parameters:
    `traj`: ndarray - trajectory of shape (numPt, 2)

    return:
    tuple including list of Ds and Voronoi object
    """
    assert(traj.shape[-1] == 2) # only 2D is supported
    numPt = traj.reshape(-1, 2).shape[0]
    objVor = Voronoi(traj.reshape(-1, 2))
    lstVert = objVor.vertices
    lstRegion = [objVor.regions[i] for i in objVor.point_region]
    lstCntRep = [sum(objVor.point_region == objVor.point_region[i]) for i in range(numPt)]
    lstDs = zeros([numPt], dtype=float64)
    for idxDs in range(numPt):
        if -1 in lstRegion[idxDs]:
            lstDs[idxDs] = 0
        else:
            lstDs[idxDs] = _getPolygonAera([lstVert[i,:] for i in lstRegion[idxDs]])/lstCntRep[idxDs]
    lstDs = lstDs.reshape(traj.shape[:-1])
    return lstDs, objVor