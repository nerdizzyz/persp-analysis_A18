# -*- coding: utf-8 -*-
"""
Created on Tue Nov 20 14:12:25 2018

@author: Donghyun Kang
"""
import pytest

def operate(a, b, oper):
    """Apply an arithmetic operation to a and b."""
    if type(oper) is not str:
        raise TypeError("oper must be a string")
    elif oper == '+':
        return a + b
    elif oper == '-':
        return a - b
    elif oper == '*':
        return a * b
    elif oper == '/':
        if b == 0:
            raise ZeroDivisionError("division by zero is undefined")
        return a / b
    raise ValueError("oper must be one of '+', '/', '-', or '*'")
    
def test_operate():
    with pytest.raises(TypeError) as typeinfo:
        operate(1, 1, 2)
    assert typeinfo.value.args[0] == "oper must be a string"

    with pytest.raises(TypeError) as typeinfo:
        operate(1, 1, [1,2])
    assert typeinfo.value.args[0] == "oper must be a string"

    assert operate(4, 3, "+") == 7
    assert operate(4, 3, "-") == 1
    assert operate(4, 3, "*") == 12
    assert operate(12, 3, "/") == 4
    
    with pytest.raises(ZeroDivisionError) as zero:
        operate(12, 0, "/") == 4 
    assert zero.value.args[0] == "division by zero is undefined" 
    
    with pytest.raises(ValueError) as v_err:
        operate(1, 2, "a")
    assert v_err.value.args[0] == "oper must be one of '+', '/', '-', or '*'"
        
    
    
    
        
