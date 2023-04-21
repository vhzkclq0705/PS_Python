# LEVEL 2

import math

def find_gcd(arr):
    gcd = 0
    for i in arr:
        gcd = math.gcd(gcd, i)
        
    return gcd

def check_gcd(arr, gcd):
    for i in arr:
        if i % gcd == 0:
            return 0
    
    return gcd

def solution(arrayA, arrayB):
    a = check_gcd(arrayA, find_gcd(arrayB))
    b = check_gcd(arrayB, find_gcd(arrayA))
    
    return 0 if a == b == 0 else max(a, b)