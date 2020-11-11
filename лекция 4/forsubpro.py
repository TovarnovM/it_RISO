from math import *
import numpy as np

def slow_foo_sub(arr1, arr2):
    res = np.zeros_like(arr1)
    for i in range(len(arr1)):
        if arr1[i] > 0:
            res[i] = arr1[i] * sin(arr2[i]) + arr2[i] + 42
        else:
            res[i] = arr1[i] * cos(arr2[i]) + arr2[i] - 42
    return res

def f(x):
    return x*x