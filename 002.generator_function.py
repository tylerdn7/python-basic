# -*- coding: utf-8 -*-
"""
Created on Thu Feb 28 22:54:12 2019

@author: Hamza
"""
#!usr/bin/python3
def is_prime(n):
    if (n < 2):
        return False
    for x in range(2,n):
        if n % x == 0:
            return False
    return True

def generator(n = 1):
    while(True):
        if is_prime(n) : yield n
        n += 1
        
for n in generator():
    if is_prime(n) == True:
        print(n)
        if n > 100:
            break
