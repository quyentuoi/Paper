__author__ = 'quyen'
"""
Implementation of Sparse Regularized SVD (ToN2012)
Input: size of matrix X, indices of known elements, values of known elements
Output: Estimated X
Evaluation criteria: NMAE, NMSE
X.npy: matrix X extracted from Abilene network, size 2006x144
"""
import numpy as np

def SRSVD(size, indices):
    pass
def main():
    X = np.load("X.npy")
    # for i in dir(X):
    #     print i
    print X.shape
main()
