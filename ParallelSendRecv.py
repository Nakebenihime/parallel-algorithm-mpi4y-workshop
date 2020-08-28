import random
from mpi4py import MPI

communication = MPI.COMM_WORLD
rank = communication.rank

randNum = 0
rank_number = -1

if rank == 0:
    randNum = random.randint(0, 10)
    print("Process", rank, "drew the number", randNum)
    communication.send(randNum, dest=1, tag=rank)
elif rank == 1:
    print("Process", rank, "before receiving has the number", randNum)
    print("Sender rank:", rank_number)
    status = MPI.Status()
    rcv = communication.recv(source=MPI.ANY_SOURCE, tag=MPI.ANY_TAG, status=status)
    rank_number = status.source
    print("Process", rank, "received the number", rcv)
    print("Sender rank:", rank_number)
