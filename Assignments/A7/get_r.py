# -*- coding: utf-8 -*-
"""
Created on Tue Nov 20 16:18:48 2018

@author: Donghyun Kang
"""
import numpy as np 
def get_r(K, L, alpha, Z, delta):
    '''
    This function generates the interest rate or vector of interest rates
    ''' 
    #raise value error for alpha, Z, delta   
    if np.isscalar(K) and np.isscalar(L):
        r = alpha * Z * ((L/K))**(1-alpha) - delta 
        return r     
    if not np.isscalar(K) and not np.isscalar(L):
        K = np.array(K)
        L = np.array(L)
        if len(K) == len(L):
            assert("the length of two input should be the same")
        r = alpha * Z * ((L/K))**(1-alpha) - delta 
        return r