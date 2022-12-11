# -*- coding: utf-8 -*-
"""
Created on Sat Jul  9 13:20:33 2022

@author: Lincoln
"""

import os.path
import sys
from collections import deque

def into(l1,l2,lenght):
    in_celling = l1[0]
    in_floor = l2[0]
    count = 0
    for i in range(1,length):
        count += 1
        if l1[i] <= in_floor or l2[i] >= in_celling:
            break
    print('From the west, one can into the tunnel over a distance of', count)

def max_distance(l1,l2,length):
    
    celling = l1[0]
    floor = l2[0]
    left_blocked = 0
    best_length = 0
    i = 1
    while i < length:
        if l1[i] >= celling and l2[i] <= floor:
            i += 1
        elif l1[i] < celling and l1[i] > floor and l2[i] <= floor:
            celling = l1[i]
            i += 1
        elif l2[i] > floor and l2[i] < celling and l1[i] >= celling:
            floor = l2[i]
            i += 1
        elif l1[i] < celling and l1[i] > floor and l2[i] > floor and l2[i] < celling:
            celling = l1[i]
            floor = l2[i]
            i += 1
        # Above is four situations that look through will not be blocked
        # Below is the situation where look through will be blocked and 
        #how to find the new beginning
        elif l1[i] <= floor or l2[i] >= celling:
            new_best_length = i - left_blocked
            if new_best_length > best_length:
                best_length = new_best_length
            for j in range(0,i):
                if l1[j] <= l2[i] or l2[j] >= l1[i]:
                    new_i = j
            i = new_i + 1
            left_blocked = i
            celling = l1[i]
            floor = l2[i]
    # this is for when the looke through come to the end
    if i == length:
        new_best_length = i - left_blocked
        if new_best_length > best_length:
            best_length = new_best_length
            
    print('Inside the tunnel, one can into the tunnel over a maximum distance of',best_length)
        


file = input("Please enter the name of the file you want to get data from: ")

line_1 = []
line_2 = []
try:
    with open(file) as new_file:
        count_line = 0
        for line in new_file:
            if not line.isspace():
                new_line = line.split()
                if count_line == 0:
                    line_1 = new_line
                if count_line == 1:
                    line_2 = new_line
                count_line += 1
    if count_line != 2:
        raise ValueError
    if len(line_1) != len(line_2) or len(line_1) < 2 or len(line_2) < 2:
        raise ValueError
    try:
        line_1 = [int(x) for x in line_1]
        line_2 = [int(x) for x in line_2]
    except:
        raise ValueError
    length = len(line_1)
    for i in range(length):
        if line_1[i] <= line_2[i]:
            raise ValueError
except ValueError:
    print('Sorry, input file does not store valid data.')
    sys.exit()
except:
    print('Sorry, there is no such file.')
    sys.exit()
    

into(line_1,line_2,length)
max_distance(line_1,line_2,length)
