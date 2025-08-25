from __future__ import annotations
import argparse, numpy as np, matplotlib.pyplot as plt
from scipy.spatial import cKDTree
from sim.weights_schedules import node_volumes, gaussian_weights
def field_and_grad(X):
    pi=np.pi; s=np.sin(pi*X); c=np.cos(pi*X); n=np.prod(s,axis=1)
    grads=[]; d=X.shape[1]
    for k in range(d):
        term=pi*c[:,k]
        for j in range(d):
            if j==k: continue
            term*=s[:,j]
        grads.append(term)
    grad=np.stack(grads,axis=1); grad2=np.sum(grad**2,axis=1)
    return n,grad2
def discrete_action(rows,cols,W,n): return 0.5*float(np.sum(W*(n[cols]-n[rows])**2))
def continuum_action_MC(X,V):
    _,g2=field_and_grad(X); return 0.5*float(np.sum(V*g2))
def run(dim,Ns,seed,out):
    rng=np.random.default_rng(seed); S=[]; eps=[]
    S_eff=None
    for N in Ns:
        X=rng.random((N,dim)); r=(np.log(N)/N)**(1.0/dim)
        tree=cKDTree(X); pairs=tree.query_pairs(r,output_type='ndarray')
        rows=np.concatenate([pairs[:,0],pairs[:,1]]); cols=np.concatenate([pairs[:,1],pairs[:,0]])
        dists=np.linalg.norm(X[rows]-X[cols],axis=1); W=gaussian_weights(dists,r,1.0); V=node_volumes(N)
        n,_=field_and_grad(X); S.append(discrete_action(rows,cols,W,n)); eps.append(r)
        if S_eff is None: S_eff=continuum_action_MC(X,V)
    S=np.array(S); eps=np.array(eps)
    plt.figure(); plt.plot(eps,S,'o-',label='S_eps'); 
    if S_eff is not None: 
        plt.axhline(S_eff,ls='--',label='S_eff (MC)')
    plt.gca().invert_xaxis(); plt.xlabel('radius r (ε proxy)'); plt.ylabel('action')
    plt.title('Γ-convergence: S_ε → S_eff'); plt.legend(); plt.tight_layout(); plt.savefig(out,dpi=160)
    print("Saved",out)
def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--dim',type=int,default=4)
    ap.add_argument('--Ns',type=int,nargs='+',default=[20000,40000,80000])
    ap.add_argument('--seed',type=int,default=123); ap.add_argument('--out',default='figures/fig_action_convergence.png')
    a=ap.parse_args(); run(a.dim,a.Ns,a.seed,a.out)
if __name__=='__main__': main()
