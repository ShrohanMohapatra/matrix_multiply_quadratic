from math import log10
import unittest
from random import randint

def my_matrix_multiply(A,B):
	N=len(A)
	maxi=0
	for i in range(N):
		for j in range(N):
			if maxi<A[i][j]: maxi=A[i][j]
			if maxi<B[i][j]:maxi=B[i][j]
	M=int(log10(maxi))+1
	P=int(log10((10**(2*M)-1)*N))+1
	C,D,E=[],[],[[0 for i in range(N)] for j in range(N)]
	for i in range(N):
		sum_1=0
		for j in range(N):
			sum_1 = sum_1*(10**P)+A[i][j]
		C.append(sum_1)
	for j in range(N):
		sum_1=0
		for i in range(N):
			sum_1=sum_1*(10**P)+B[N-1-i][j]
		D.append(sum_1)
	for i in range(N):
		for j in range(N):
			E[i][j]=int(C[i]*D[j]/(10**(P*(N-1)))) %(10**P)
	return E

def ijk_method(A,B):
    N = len(A)
    C = [ [ 0 for j in range(N) ] for i in range(N) ]
    for i in range(N):
        for j in range(N):
            for k in range(N):
                C[i][j] = C[i][j] + A[i][k]*B[k][j]
    return C

class TestMatrixProduct(unittest.TestCase):
    
    def test_RandomMatrix1(self):
        N = randint(1,30)
        A = [ [ randint(1,150) for j in range(N) ] for i in range(N) ]
        B = [ [ randint(1,150) for j in range(N) ] for i in range(N) ]
        self.assertEquals(ijk_method(A,B),my_matrix_multiply(A,B),msg='Mismatch')

def test_suite():
    suite = unittest.TestSuite()
    for i in range(100): suite.addTest(unittest.makeSuite(TestMatrixProduct))
    return suite

test = test_suite()
result = unittest.TestResult()
test.run(result)
print 'Number of given tests',result.testsRun
print 'Number of erroneous tests',len(result.errors)
print 'Number of tests that failed',len(result.failures)
