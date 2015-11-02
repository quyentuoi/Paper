import os 
import matplotlib.pyplot as plt

from numpy.fft import fft
import numpy as np

def gen_ADT_matrix(n,alpha):
	import numpy as np 
	A = 0.0*np.random.rand(n,n); 
	A = np.asarray(A)
	for i in range(n-1):
		A[i, i] = 1
		A[i, i+1] = -1
	A[n-1, n-1] = alpha
	return A 

def linear_mapping(X):
	'''
	This function finds the linear mapping between the first row and the rest 
	'''
	from  sklearn.linear_model import Lasso
	n = X.shape[1] # number of flow

	y = X[:,0]  # data of first flow 
	A = X[:,1:n]  # data of n-1 remained flows
	print A.shape
	lasso = Lasso(alpha=0.3)
	lasso.fit(A,y) 
	omega = lasso.fit(A,y)
	omega = omega.coef_
	# omega = np.dot(np.linalg.inv(A),y)
	return omega 	

X = np.load("X.npy")
"""
omega = linear_mapping(X)
t = 2
print X[t,0] - np.dot(X[t,1:X.shape[1]], omega)
"""
from Metrics import *

X = np.random.rand(5,6)
X_pred = np.random.rand(5,6)
print NMSE(X,X_pred)




