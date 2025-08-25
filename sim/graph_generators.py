from __future__ import annotations
import argparse, os, json, numpy as np
from scipy.spatial import cKDTree
from sklearn.neighbors import kneighbors_graph
from sim.weights_schedules import node_volumes, gaussian_weights
def generate_rgg(dim:int,N:int,seed:int,k:int|None,radius:float|None):
    rng=np.random.default_rng(seed); X=rng.random((N,dim))
    if k is not None:
        A=kneighbors_graph(X,n_neighbors=k,mode='distance',include_self=False).tocoo()
        rows,cols,dists=A.row,A.col,A.data
    else:
        if radius is None: radius=(np.log(N)/N)**(1.0/dim)
        tree=cKDTree(X); pairs=tree.query_pairs(radius,output_type='ndarray')
        if pairs.size==0: raise RuntimeError("No edges; increase radius or N")
        rows=np.concatenate([pairs[:,0],pairs[:,1]]); cols=np.concatenate([pairs[:,1],pairs[:,0]])
        dists=np.linalg.norm(X[rows]-X[cols],axis=1)
    if radius is None: radius=(np.log(N)/N)**(1.0/dim)
    W=gaussian_weights(dists,radius,1.0); V=node_volumes(N)
    return X,rows,cols,dists,W,V,radius
def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--dim',type=int,default=4); ap.add_argument('--N',type=int,default=50000)
    ap.add_argument('--seed',type=int,default=42); ap.add_argument('--k',type=int,default=None)
    ap.add_argument('--radius',type=float,default=None); ap.add_argument('--out',required=True)
    a=ap.parse_args()
    X,rows,cols,dists,W,V,r=generate_rgg(a.dim,a.N,a.seed,a.k,a.radius)
    os.makedirs(os.path.dirname(a.out),exist_ok=True)
    np.savez_compressed(a.out,X=X,rows=rows,cols=cols,dists=dists,W=W,V=V,radius=r,meta=json.dumps(vars(a)))
    print("Saved",a.out)
if __name__=='__main__': main()
