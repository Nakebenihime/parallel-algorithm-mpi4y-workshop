from mpi4py import MPI

communication = MPI.COMM_WORLD
rank = communication.rank
size = communication.size
master = 0
total = 0
v1 = [1, 2, 3, 4]
v2 = [5, 6, 7, 8]

status = MPI.Status()
if rank == master:
    print("scattering :", v1, " and ", v2)

data = v1[rank] * v2[rank]

data = communication.gather(data, root=master)

if rank == master:
    for i in range(0, len(data)):
        total += data[i]
        print("master total: ", total)