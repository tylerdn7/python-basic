# -*- coding: utf-8 -*-
"""
Created on Thu Feb 28 22:54:12 2019

@author: Hamza
"""
#!usr/bin/python3
def is_prime(n):
    if (n == 1):
        return False
    for x in range(2,n):
        if n % x == 0:
            return False
        else:
            print("{} is a prime number".format(n))
            return True
        
for n in range(1,50):
    is_prime(n)
