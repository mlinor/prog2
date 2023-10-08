# prog2
Comment on the results:
  Numba has some overhead for the initial compilation of the code. For very small tasks, the compilation overhead can outweigh the performance improvement. So, when n = 20, the initial number, the cost of numbda is larger than pure python.
  Overall, the C++ implementation is the fastest, followed by Numba-optimized Python, and pure Python is the slowest. 

  For n = 47, the excusion time for numba and C++ are similor (about 50s). For large values of n, Numba's optimization capabilities become more pronounced, and it can approach the execution speed of C++. And they are dominated by the same algorithmic complexity.
