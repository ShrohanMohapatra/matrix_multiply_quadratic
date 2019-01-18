from math import log10
from random import randint
def my_matrix_multiply(A,B):
    flag = True
    flag = flag and (len(A) == len(B))
    if not flag: return None
    N = len(A)
    for i in range(N): flag = flag and (len(A[i])==len(B[i]))
    if not flag: return None
    maxi=0
    for i in range(N):
		for j in range(N):
			if maxi<A[i][j]: maxi=A[i][j]
			if maxi<B[i][j]: maxi=B[i][j]
    M=int(log10(maxi))+1
    P=int(log10((10**(2*M)-1)*N))+1
    C,D,E=[0 for i in range(N)],[0 for i in range(N)],[[0 for i in range(N)] for j in range(N)]
    for i in range(N):
		for j in range(N):
			C[i] = C[i]*(10**P)+A[i][j]
    for j in range(N):
		for i in range(N):
			D[j] = D[j]*(10**P)+B[N-1-i][j]
    for i in range(N):
		for j in range(N):
			E[i][j]=int(C[i]*D[j]/(10**(P*(N-1))))%(10**P)
    return E
def ijk_method(A,B): # for verification
    flag = True
    flag = flag and (len(A) == len(B))
    if not flag: return None
    N = len(A)
    for i in range(N): flag = flag and (len(A[i])==len(B[i]))
    if not flag: return None
    C = [ [ 0 for j in range(N) ] for i in range(N) ]
    for i in range(N):
        for j in range(N):
            for k in range(N):
                C[i][j] = C[i][j] + A[i][k]*B[k][j]
    return C
N = randint(1,30)
A = [ [ randint(1,150) for j in range(N) ] for i in range(N) ]
B = [ [ randint(1,150) for j in range(N) ] for i in range(N) ]
C1 = my_matrix_multiply(A,B)
C2 = ijk_method(A,B)
flag = True
for i in range(N):
    for j in range(N): flag = flag and C1[i][j] == C2[i][j]
if flag:
    print 'Input size',N
    print 'Input matrix A'
    for i in range(N):
        for j in range(N): print A[i][j],
        print
    print 'Input matrix B'
    for i in range(N):
        for j in range(N): print B[i][j],
        print
    print 'Output matrix C1'
    for i in range(N):
        for j in range(N): print C1[i][j],
        print
else: print 'Debug needed'