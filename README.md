Quadratic-time algorithm for matrix multiplication with positive integers
--------------------------------------------------------------------------

This source code is a preliminary implementation of my quadratic-time positive integer matrix multiplication that was theoretically proven of its time and space complexity in one of my preprints [1]. There have been several proposals on sub-cubic algorithm optimizations since the improvization of the recursive version by Strassen( running in O(n^log2(7)) = O(n^2.807)) [2], such as that by Bini et al. (running in O(n^2.78)) [3], another one by Strassen (running in O(n^2.479)) [4], by Coppersmith and Winograd (running in O(n^2.375)) [5], by Williams (running in O(n^2.3729)) [6] and most recently by Francois Le-Gall (running in O(n^2.3728639)) [7]. But all of them are theoretically sound but not practically implementable due to the heavy data structures such as tensor powers. The theoretical background has been shown and proven on its correctness based on number theoretic methods [1]. The file 'my_matrix_multiply.py' is basically a unit testing file that practically proves the correctness of my method. But the method has been designed and tested only for positive integers, which can be aptly modified to suit the cases with negative integers, floating numbers, and complex numbers as well. 

References
-----------

[1] S. Mohapatra, "Convolutional number-theoretic method to optimise integer matrix multiplication", [arXiv:1806.03701], 2018
[2] V. Strassen, "Gaussian Elimination is not Optimal", Numer. Math. 13, p. 354-356, 1969
[3] D. Bini, M. Capovani, F. Romani, and G. Lotti. "O(n^2.7799) complexity for n × n approximate matrix multiplication" Inf. Process. Lett., pp. 234–235, 1979
[4] V. Strassen, "The Asymptotic Spectrum of Tensors and the Exponent of Matrix Multiplication", Proc. 27th Ann. IEEE Symp. on Foundations of Computer Science, pp. 49-54, 1984
[5] D. Coppersmith, S. Winograd, "Matrix multiplication via arithmetic progressions". J. Symbolic Comput. pp. 251–280, 1980
[6] V. Williams, "Multiplying matrices faster than Coppersmith-Winograd". ACM: pp.887–898, 2012
[7] F. Le Gall, "Powers of tensors and fast matrix multiplication", Proc. 39th Int. Symp. on Symbolic and Algebraic Computation, 2014
