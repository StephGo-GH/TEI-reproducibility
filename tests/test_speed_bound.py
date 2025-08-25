from sim.hyperbolicity_test import simulate_front
def test_front_growth():
    neighbors=[[] for _ in range(5)]
    neighbors[0]=[1]; neighbors[1]=[0,2]; neighbors[2]=[1,3]; neighbors[3]=[2,4]; neighbors[4]=[3]
    radii=simulate_front(neighbors,steps=4,seed=0)
    assert len(radii)==5 and radii[-1]>=4
