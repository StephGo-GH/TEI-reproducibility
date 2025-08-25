from __future__ import annotations
import argparse, numpy as np, matplotlib.pyplot as plt
def load_graph(path):
    z=np.load(path,allow_pickle=True); rows,cols=z['rows'],z['cols']; N=z['X'].shape[0]
    neigh=[[] for _ in range(N)]
    for i,j in zip(rows,cols): neigh[int(i)].append(int(j))
    return neigh
def simulate_front(neighbors,steps,seed):
    rng=np.random.default_rng(seed); N=len(neighbors); start=rng.integers(0,N)
    frontier={start}; radii=[0]
    for k in range(1,steps+1):
        new=set(frontier)
        for u in frontier:
            for v in neighbors[u]: new.add(v)
        frontier=new; radii.append(k)
    return np.array(radii)
def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--graph',required=True)
    ap.add_argument('--steps',type=int,default=50); ap.add_argument('--out',default='figures/fig_cone_emergence.png')
    a=ap.parse_args(); neighbors=load_graph(a.graph); radii=simulate_front(neighbors,a.steps,0)
    t=np.arange(len(radii)); plt.figure(); plt.plot(t,radii,marker='o')
    plt.xlabel('iterations (τ_ε)'); plt.ylabel('hop radius'); plt.title('Finite propagation: emergent cone')
    plt.tight_layout(); plt.savefig(a.out,dpi=160); print("Saved",a.out)
if __name__=='__main__': main()
