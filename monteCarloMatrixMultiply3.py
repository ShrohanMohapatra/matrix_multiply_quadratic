import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import numpy as np
from random import randint
from scipy import optimize
from time import time
def monteCarloMatrixMultiply2(A,B):
    n = len(A)
    C = [[{} for j in range(n)] for i in range(n)]
    D = [[{} for j in range(n)] for i in range(n)]
    AB = [[0  for j in range(n)] for i in range(n)]
    for i in range(n):
        for j in range(n):
            C[i][j]['size'] = 0
            D[i][j]['size'] = 0
    while True:
        for i in range(n):
            for j in range(n):
                k = randint(0,n-1)
                if j in C[i][k] and i in D[k][j]: pass
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
def testPoly(x,a,b,c,d):
    return a*x**3 + b*x**2 + c*x + d
setparams = [5,105,5]
experi2Time = [k for k in range(setparams[0],setparams[1],setparams[2])]
xaxis = [k for k in range(setparams[0],setparams[1],setparams[2])]
for k in range(len(xaxis)):
    n1 = xaxis[k]
    A = [[randint(5,10) for i in range(n1)] for j in range(n1)]
    B = [[randint(5,10) for i in range(n1)] for j in range(n1)]
    start = time()
    monteCarloMatrixMultiply2(A,B)
    end = time()
    experi2Time[k] = end - start
    print('size = ',xaxis[k],' --> done ...')
np.random.seed(0)
params, params_covariance = optimize.curve_fit(
    testPoly,xaxis,experi2Time,
    p0=[1, 1, 1, 1])
print(
    '(',params[0],')x^3 + (',params[1],')x^2 + (',params[2],')x +',params[3]
    )