# PARALLEL COMPUTING USING MPI4PY PYTHON PACKAGE
This repository contains the basic concepts of parallel computing using the Python package (mpi4py) which provides bindings to the **Message Passing
Interface** (MPI) standard for the Python programming language. You will find in this project, examples of basic point-to-point and collective communication.

## TECHNOLOGY STACK
COMPONENT              | TECHNOLOGY     | FOR MORE INFORMATION
---                    | ---            |---
Languages & Frameworks | `python`       | https://www.python.org/
PyPI Packages          | `mpi4py`       | https://pypi.org/project/mpi4py/

## PREREQUISITES
These instructions will allow you to get a copy of the project on your **windows** machine, you must have the following software correctly installed in order to build MPI for Python.

### INSTALL MPI
Download and install Microsoft MPI v10.1.2 from the microsoft.com download center:
```
You need to download and run the *.msi and *.exe files
```
Set the folder path in your system environment variable, in my case $PATH$ is where Microsoft MPI was installed:
```
  - C:\Program Files\Microsoft MPI\Bin
  - C:\Program Files (x86)\Microsoft SDKs\MPI
```
### INSTALL PYTHON & PIP
Download the Python 3.x Windows x86-64 executable installer from the python.org download page:
```
Launch the installer, choose Add Python 3.x to PATH and click Install Now.
```
Verify that both Python and pip are correctly installed by using the following commands:
```
C:\Windows\System32> python --version
Python 3.x.x
```
```
C:\Windows\System32> pip --version
pip x.x.x ...
```
### INSTALL MPI4PY
Install mpi4py using pip by using the following command:
```
C:\Windows\System32> pip install mpi4py
```
## GETTING STARTED
To install this application, run the following commands:
```
git clone https://github.com/Nakebenihime/parallel-algorithm-mpi4py-workshop.git
cd parallel-algorithm-mpi4py-workshop
```
To quickly test the installation, run the command mpiexec:
```
mpiexec -n <number_process> python HelloWorld.py
```
CLI output (the order might change):
```
I am process < 3 > of  4  processors
I am process < 1 > of  4  processors
I am process < 0 > of  4  processors
I am process < 2 > of  4  processors
```