# -*- coding: utf-8 -*-
"""factorial.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/github/utokyo-ipp/annex/blob/master/assignments/pre5/factorial.ipynb
"""

def fact(n):
    prod = 1
    for i in range(1, n + 1):
        prod *= i
    return prod