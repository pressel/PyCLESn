import sys, os
import mpi4py as MPI


myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')

import mesh



def test_mesh_comm():

    namelist_dict = {}
    test_mesh = mesh.Mesh(namelist_dict)

    assert test_mesh.comm.rank == 0
    assert test_mesh.comm.size == 1


    return


def test_Mesh2DCart_comm():

    namelist_dict = {}
    test_mesh = mesh.Mesh2DCart(namelist_dict)


    assert test_mesh.comm.rank == 0
    assert test_mesh.comm.size == 1

    return
