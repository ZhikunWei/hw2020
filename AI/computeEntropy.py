#!/usr/bin/python 
# -*-coding:utf-8 -*-
__author__ = '99K'
import math

if __name__ == '__main__':
    fenzi = int(input())
    fenmu = int(input())
    p = fenzi / fenmu
    res = - p * math.log(p, 2)
    
    p2 = 1-p
    res += -p2 * math.log(p2, 2)
    
    print(res)