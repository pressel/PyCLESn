import sys, os
import mpi4py as MPI


myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')

import mesh


namelist_dict = {}
test_mesh = mesh.Mesh(namelist_dict)


def test_mesh_comm():
    assert test_mesh.comm.rank == 0
    assert test_mesh.comm.size == 1

    return
