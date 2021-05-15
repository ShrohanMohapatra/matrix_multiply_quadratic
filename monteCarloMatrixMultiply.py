from random import randint
import matplotlib.pyplot as plt
from time import time
def monteCarloMatrixMultiply(A,B):
    n = len(A)
    C = [[{k:False for k in range(n)} for j in range(n)] for i in range(n)]
    D = [[{k:False for k in range(n)} for j in range(n)] for i in range(n)]
    AB = [[0  for j in range(n)] for i in range(n)]
    for i in range(n):
        for j in range(n):
            C[i][j]['size'] = 0
            D[i][j]['size'] = 0
    while True:
        for i in range(n):
            for j in range(n):
                k = randint(0,n-1)
                if C[i][k][j] and D[k][j][i]: pass
                else:
                    C[i][k][j] = True
                    C[i][k]['size'] = C[i][k]['size'] + 1
                    D[k][j][i] = True
                    D[k][j]['size'] = D[k][j]['size'] + 1
                    AB[i][j] = AB[i][j] + A[i][k]*B[k][j]
        flag = True
        for i in range(n):
            for j in range(n):
                flag = flag and C[i][j]['size'] == n and D[i][j]['size'] == n
        if flag: break
    return AB
def actualMatrixMultiply(A,B):
    n = len(A)
    C = [[0 for j in range(n)] for i in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                C[i][j] = C[i][j] + A[i][k]*B[k][j]
    return C
print(monteCarloMatrixMultiply([[5,0],[0,7]],[[6,0],[0,10]]))
print(monteCarloMatrixMultiply(
    [[1,0,0],[0,1,0],[0,0,1]],[[6,0,4],[0,10,10],[1,2,3]]))
setparams = [5,45,5]
actualTime = [k for k in range(setparams[0],setparams[1],setparams[2])]
experiTime = [k for k in range(setparams[0],setparams[1],setparams[2])]
xaxis = [k for k in range(setparams[0],setparams[1],setparams[2])]
for k in range(len(xaxis)):
    n1 = xaxis[k]
    A = [[randint(5,10) for i in range(n1)] for j in range(n1)]
    B = [[randint(5,10) for i in range(n1)] for j in range(n1)]
    start = time()
    actualMatrixMultiply(A,B)
    end = time()
    actualTime[k] = end - start
    start = time()
    monteCarloMatrixMultiply(A,B)
    end = time()
    experiTime[k] = end - start
fig, ax = plt.subplots()
ax.plot(xaxis,actualTime,label='Schoolbook algo')
ax.plot(xaxis,experiTime,label='My algo')
legend = ax.legend()
plt.show()