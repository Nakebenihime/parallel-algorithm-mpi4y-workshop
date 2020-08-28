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
# distribution to all processes, including the master process two vector values
d1 = communication.scatter(v1, root=master)
d2 = communication.scatter(v2, root=master)

# product of the two retrieved values
print("process ", rank, "received: ", d1, " and ", d2)
data = d1 * d2

# gather data from all processes into a single process
data = communication.gather(data, root=master)

if rank == master:
    for i in range(0, len(data)):
        total += data[i]
        print("master total: ", total)