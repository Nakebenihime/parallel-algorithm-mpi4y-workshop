from mpi4py import MPI
import random
import itertools

comm = MPI.COMM_WORLD
size = comm.size
rank = comm.rank
master = 0
max = 100
tab = []
bucket = [[] for _ in range(size)]
if rank == master:
    tab = [random.randint(0, max - 1) for i in range(15)]
    print("Tab to sort : ", tab)
    for i in range(0, len(tab)):
        if (tab[i] <= max // size):
            bucket[0].append([tab[i]])
        elif (tab[i] <= (max // size) * 2):
            bucket[1].append([tab[i]])
        elif (tab[i] <= (max // size) * 3):
            bucket[2].append([tab[i]])
        else:
            bucket[3].append([tab[i]])

process_bucket = comm.scatter(bucket, root=master)
print("Process ", rank, " received : ", process_bucket, " ==> Sort : ", sorted(process_bucket))
process_bucket = sorted(process_bucket)

data = comm.gather(process_bucket, root=master)

if rank == master:
    flat = list(itertools.chain(*list(filter(None, data))))
    print("Sorted tab length : ", len(flat))
    print("Sorted tab : ", flat)
