from mpi4py import MPI

communication = MPI.COMM_WORLD
rank = communication.rank
size = communication.size
master = 0
tag = 100

vectorSize = 4
v1 = [1, 2, 3, 4]
v2 = [5, 6, 7, 8]

if rank == master:
    status = MPI.Status()
    total = 0
    for i in range(1, vectorSize + 1):
        v = [v1[i - 1], v2[i - 1]]
        print("master: sending vector ", v, " to compute", i)
        communication.send(v, dest=i, tag=tag)
    for i in range(1, vectorSize + 1):
        rcv = communication.recv(source=MPI.ANY_SOURCE, tag=tag, status=status)
        print("master: recv value: ", rcv)
        total += rcv
    print("Inner Product = ", total)
else:
    status = MPI.Status()
    rcv = communication.recv(source=MPI.ANY_SOURCE, tag=tag, status=status)
    print("worker ", rank, "recv: ", rcv)
    communication.send(rcv[0]*rcv[1], dest=master, tag=tag)