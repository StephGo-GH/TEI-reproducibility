import numpy as np
from sim.graph_generators import generate_rgg
from sim.poincare_check import estimate_constant
from sim.weights_schedules import node_volumes, gaussian_weights
def test_poincare_constant_small():
    X,rows,cols,dists,W,V,r=generate_rgg(dim=3,N=2000,seed=1,k=12,radius=None)
    Cmin,cs=estimate_constant(rows,cols,W,V,samples=4,seed=0)
    assert Cmin>0.0
