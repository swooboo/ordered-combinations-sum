# -*- coding: utf-8 -*-
"""
Created on Fri Oct 22 02:01:02 2021

@author: swooboo
"""

from sympy import poly
from sympy.abc import x

def poly_sum_ordered_reps(numbers, target_sum=0):
    """ Returns the number of ordered combinations of numbers that sum up to
    the target sum. For example, for [1,2] and 5, the number of combinations
    is 8. This implementation uses polynomes to represent different combinations.
    The coefficients of the polynomes are the numbers of combinations, and the
    powers are the sums with that number of combinations."""

    base_poly = base_polynome(numbers)
    big_poly = poly(1, x)
    total_combinations = 0
    for _ in range(1, target_sum+1):
        big_poly = big_poly * base_poly
        big_poly = big_poly.slice(0, target_sum+1)
        total_combinations += big_poly.coeff_monomial(x**target_sum)

    return total_combinations


def base_polynome(numbers):
    """ Returns a polynome representing the numbers list. For example, with
    the list [1,2,4], the polynome will be P(x)=x**4+x**2+x."""

    monomes = [ x**n for n in numbers ]
    polynome = sum(monomes)

    return poly(polynome, x)
