# -*- coding: utf-8 -*-
"""
Created on Tue Jul  5 20:14:35 2022

@author: Lincoln
"""
import sys

code = input("Please input the heroes' powers: ").split()

for i in range(len(code)):
    try:
        int(code[i])
    except ValueError:
        print('Sorry, these are not valid power values.')
        sys.exit()

for i in range(len(code)):
        code[i] = int(code[i])        

nb_of_switches = input("Please input the number of power flips: ")
nb_of_switches = int(nb_of_switches)

try:
    if nb_of_switches > len(code):
        raise ValueError
except ValueError:
    print('Sorry, this is not a valid number of power flips.')
    sys.exit()
    
#Strating swithcing
def switching_many_times(power,n):
    positive = []
    negative = []
    
    for i in range(len(power)):
        if power[i] < 0:
            negative.append(power[i])
        if power[i] >= 0:
            positive.append(power[i])
    
    #positive = sorted(positive)
    negative = sorted(negative)
    if n <= len(negative):
        for _ in range(n):
            low = negative[0]
            negative.remove(low)
            positive.append(low*(-1))
    
    if n > len(negative):
        nb_negative = len(negative)
        negative = [-x for x in negative]
        positive = positive + negative
        negative =[]
        if (n-nb_negative)%2 == 1:
            positive = sorted(positive)
            positive[0] = -positive[0]
        
    result = sum(positive)+sum(negative)
    return result

def swithing_at_most_once(power,n):
    positive = []
    negative = []
    
    for i in range(len(power)):
        if power[i] < 0:
            negative.append(power[i])
        if power[i] >= 0:
            positive.append(power[i])
            
    negative = sorted(negative)
    if n <= len(negative):
        for _ in range(n):
            low = negative[0]
            negative.remove(low)
            positive.append(low*(-1))
    
    if n > len(negative):
        nb_negative = len(negative)
        negative = [-x for x in negative]
        positive = sorted(positive)
        for _ in range(n - nb_negative):
            low = positive[0]
            positive.remove(low)
            negative.append(low*(-1))
        
        
    result = sum(positive)+sum(negative)
    return result

def switching_in_sequence(power,n):
    sub_sum = sum(power[0:n])
    high = sub_sum*-1 +sum(power[n:])
    
    for i in range(len(power)-n):
        sub_sum = sub_sum + power[n+i] - power[i]
        new_high = sub_sum*-1 + sum(power[0:i+1]) + sum(power[n+i+1:])
        if new_high > high:
            high = new_high
    return high

def switching_in_no_limit_sequence(power):
    high = sum(power)
    for n in range(1,len(power)):
        new_high = switching_in_sequence(power,n)
        if new_high > high:
            high = new_high
    return high
    
r1 = switching_many_times(code,nb_of_switches)
print('Possibly flipping the power of the same hero many times, the greatest achievable power is',r1,end = '.\n')
r2 = swithing_at_most_once(code,nb_of_switches)
print('Flipping the power of the same hero at most once, the greatest achievable power is',r2,end = '.\n')
r3 = switching_in_sequence(code,nb_of_switches)
print('Flipping the power of nb_of_flips many consecutive heroes, the greatest achievable power is',r3,end = '.\n')
r4 = switching_in_no_limit_sequence(code)
print('Flipping the power of arbitrarily many consecutive heroes, the greatest achievable power is',r4,end = '.\n')
