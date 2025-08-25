import numpy as np
from sim.gamma_convergence import field_and_grad, discrete_action, continuum_action_MC
from sim.weights_schedules import node_volumes, gaussian_weights
from scipy.spatial import cKDTree
def test_gamma_convergence_small():
    rng=np.random.default_rng(0); dim=3; N=3000
    X=rng.random((N,dim)); r=(np.log(N)/N)**(1.0/dim)
    tree=cKDTree(X); pairs=tree.query_pairs(r,output_type='ndarray')
    rows=np.concatenate([pairs[:,0],pairs[:,1]]); cols=np.concatenate([pairs[:,1],pairs[:,0]])
    dists=np.linalg.norm(X[rows]-X[cols],axis=1); W=gaussian_weights(dists,r,1.0); V=node_volumes(N)
    n,_=field_and_grad(X); Se=discrete_action(rows,cols,W,n); SMC=continuum_action_MC(X,V)
    assert Se>0 and SMC>0
