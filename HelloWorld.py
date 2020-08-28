from mpi4py import MPI

communication = MPI.COMM_WORLD
rank = communication.rank
size = communication.size

print("I am process <", rank, ">" + " of ", size, " processors")
