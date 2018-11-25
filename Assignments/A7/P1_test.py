# -*- coding: utf-8 -*-
"""
Created on Tue Nov 20 12:40:46 2018

@author: Donghyun Kang
"""

def smallest_factor(n):
    """Return the smallest prime factor of the positive integer n."""
    if n == 1: return 1
    for i in range(2, int(n**.5) + 1):
        if n % i == 0: return i
    return n

def test_smallest_factor():
    assert smallest_factor(3) == 3
    assert smallest_factor(4) == 2
    assert smallest_factor(5) == 5
    assert smallest_factor(6) == 2
    assert smallest_factor(7) == 7
    assert smallest_factor(8) == 2
    assert smallest_factor(9) == 3 
    assert smallest_factor(10) == 2

