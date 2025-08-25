from __future__ import annotations
import argparse, json, numpy as np, matplotlib.pyplot as plt
def load_graph(path):
    z=np.load(path,allow_pickle=True); return z['rows'],z['cols'],z['W'],z['V']
def energy(rows,cols,W,n): return float(np.sum(W*(n[cols]-n[rows])**2))
def varV(V,n): m=float(np.sum(V*n)); return float(np.sum(V*(n-m)**2))
def estimate_constant(rows,cols,W,V,samples=8,seed=0):
    rng=np.random.default_rng(seed); cs=[]
    N=V.shape[0]
    for _ in range(samples):
        n=rng.normal(size=N); cs.append( energy(rows,cols,W,n)/(varV(V,n)+1e-12) )
    return float(np.min(cs)), np.array(cs)
def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--graph',required=True)
    ap.add_argument('--samples',type=int,default=8); ap.add_argument('--out',default='figures/fig_poincare_ratio.png')
    a=ap.parse_args()
    rows,cols,W,V=load_graph(a.graph); Cmin,cs=estimate_constant(rows,cols,W,V,a.samples)
    print(f"Estimated C ≈ {Cmin:.4e}")
    plt.figure(); plt.plot(cs,marker='o'); plt.xlabel('sample'); plt.ylabel('energy/variance')
    plt.title('Discrete Poincaré ratio'); plt.tight_layout(); plt.savefig(a.out,dpi=160)
if __name__=='__main__': main()
