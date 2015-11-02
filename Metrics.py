__author__ = 'quyen'
from sklearn.metrics import *
import numpy as np

def NMAE(X_true, X_pred):
    return mean_absolute_error(X_true, X_pred)
def NMSE(X_true, X_pred):
    return mean_squared_error(X_true, X_pred)

