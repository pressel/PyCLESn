from mpi4py import MPI

class Mesh:
    def __init__(self, namelist):

        self.comm = MPI.COMM_WORLD

        return



class Mesh2DCart(Mesh):
    def __init__(self, namelist):

        Mesh.__init__(self, namelist)



        return