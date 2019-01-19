from math import log10
from threading import Thread
from random import randint
from time import time
import unittest
from pprint import pprint
def threadCompare(A, B, i, j, maxi):
  	if maxi[0] < A[i][j] : maxi[0] = A[i][j]
	if maxi[0] < B[i][j] : maxi[0] = B[i][j]
def threadOne_New(A, C, i, j, P):
  	C[i] = C[i]*10**(P) + A[i][j]
def threadTwo_New(B, D, i, j, P, N):
  	D[j] = D[j]*10**(P) + B[N - 1 - i][j]
def threadThree_New(E, C, D, i, j, P, N) :
  	E[i][j] = int(C[i]*D[j]/(10**(P*(N - 1))))%(10**P)
def new_matrix_multiply(A, B):
  	N = len(A)
	maxi = [0]
	threadSeries = [[Thread(target = threadCompare, args =(A, B, i, j, maxi,)) for j in range(N)] for i in range(N)]
	for i in range(N):
 		for j in range(N): threadSeries[i][j].start()
	for i in range(N):
 		for j in range(N): threadSeries[i][j].join()
	M = int(log10(maxi[0]))+1
	P = int(log10((10**(2*M)-1)*N))+1
	C, D, E = [0 for i in range(N)], [0 for i in range(N)], [[0 for j in range(N)] for i in range(N)]
	threadSeriesOne = [[Thread(target = threadOne_New, args =(A, C, i, j, P,)) for j in range(N)] for i in range(N)]
	threadSeriesTwo = [[Thread(target = threadTwo_New, args =(B, D, i, j, P, N,)) for j in range(N)] for i in range(N)]
	for i in range(N):
 		for j in range(N): threadSeriesOne[i][j].start()
	for i in range(N):
 		for j in range(N): threadSeriesOne[i][j].join()
	for i in range(N):
 		for j in range(N): threadSeriesTwo[i][j].start()
	for i in range(N):
 		for j in range(N): threadSeriesTwo[i][j].join()
	threadSeriesThree = [[Thread(target = threadThree_New, args =(E, C, D, i, j, P, N,)) for j in range(N)] for i in range(N)]
	for i in range(N):
 		for j in range(N): threadSeriesThree[i][j].start()
	for i in range(N):
 		for j in range(N): threadSeriesThree[i][j].join()
	return E
def ijk_method(A,B):
    N = len(A)
    C = [[0 for j in range(N)] for i in range(N)]
    for i in range(N):
        for j in range(N):
            for k in range(N): C[i][j] = C[i][j] + A[i][k]*B[k][j]
    return C
class TestCAMatrixProduct(unittest.TestCase):
    def test_RandomMatrix1(self):
        N = randint(1,3)
        A = [ [ randint(1,5) for j in range(N) ] for i in range(N) ]
        B = [ [ randint(1,5) for j in range(N) ] for i in range(N) ]
        self.assertEquals(ijk_method(A,B),new_matrix_multiply(A,B),msg='Mismatch')
def test_suite():
    suite = unittest.TestSuite()
    for i in range(20): suite.addTest(unittest.makeSuite(TestCAMatrixProduct))
    return suite
test = test_suite()
result = unittest.TestResult()
test.run(result)
print 'Number of given tests',result.testsRun
print 'Number of erroneous tests',len(result.errors)
if len(result.errors) != 0:
    print 'Erroneous tests'
    pprint(result.errors)
print 'Number of tests that failed',len(result.failures)
if len(result.failures) != 0:
    print 'Failed tests'
    pprint(result.failures)
