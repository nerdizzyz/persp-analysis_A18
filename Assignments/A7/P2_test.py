# -*- coding: utf-8 -*-
"""
Created on Tue Nov 20 13:38:55 2018

@author: Donghyun Kang
"""
def month_length(month, leap_year=False):
    """Return the number of days in the given month."""
    if month in {"September", "April", "June", "November"}:
        return 30
    elif month in {"January", "March", "May", "July",
                   "August", "October", "December"}:
        return 31
    if month == "February":
        if not leap_year:
            return 28
        else:
            return 29
    else:
        return None
    
def test_month_length():
    assert month_length("January") == 31
    assert month_length("February", leap_year = False) == 28
    assert month_length("February", leap_year = True) == 29
    assert month_length("March") == 31
    assert month_length("April") == 30
    assert month_length("May") == 31
    assert month_length("June") == 30
    assert month_length("July") == 31
    assert month_length("August") == 31
    assert month_length("September") == 30
    assert month_length("October") == 31
    assert month_length("November") == 30
    assert month_length("December") == 31
    assert month_length("whatever") == None