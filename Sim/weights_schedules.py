from __future__ import annotations
import numpy as np
def node_volumes(N:int)->np.ndarray:
    return np.full(N,1.0/N)
def gaussian_weights(dists:np.ndarray,r:float,alpha:float=1.0)->np.ndarray:
    sigma2=(alpha*r)**2*2.0
    return np.exp(-(dists**2)/sigma2)
