import os.path
import sys

from collections import defaultdict

def if_good_ride(l):
    if len(l) == 2:
        return 1
    else:
        for i in range(2,len(l)):
            if l[i] - l[i-1] != l[i-1] - l[i-2]:
                return 0
        return 1

def pillars_remove(line):
    d = defaultdict(lambda: "Not Present")
    for i in range(1,len(line)):
        for j in range(i):
            slope = line[i] - line[j]
            included = 0
            for key,value in d.items():
                if key[0] == line[j] and key[1] == slope:
                    included = value
            if included !=0:
                d[(line[i],slope)] = included+1
            if included == 0:
                d[(line[i],slope)] = 2
#For dict d above: eg. d[(15,5)] = 3 .... 15 means the pillar with height 15
# 5 means 15 - 10 = 5  .....    3 means value of d[(10,5)] +1
    best_ride_nb = 0
    for value in d.values():
        if value > best_ride_nb:
            best_ride_nb = value
    remove_pillars_nb = len(line) - best_ride_nb
    print('The minimal number of pillars to remove to build a perfect ride from the rest is:', remove_pillars_nb)

def longest_good_ride(line):
    lgr = defaultdict(lambda: "Not Present")
    for i in range(1,len(line)):
            slope = line[i] - line[i-1]
            included = 0
            for key,value in lgr.items():
                if key[0] == line[i-1] and key[1] == slope:
                    included = value
            if included !=0:
                lgr[(line[i],slope)] = included+1
            if included == 0:
                lgr[(line[i],slope)] = 2
    best_length = 0
    for value in lgr.values():
        if value > best_length:
            best_length = value
    best_length -= 1
    print('The longest good ride has a length of:',best_length)
    
    

file = input("Please enter the name of the file you want to get data from: ")

try:
    with open(file) as new_file:
        pass
except:
    print('Sorry, there is no such file.')
    sys.exit()

line_nb = []
with open(file) as new_file:
    for line in new_file:
        if not line.isspace():
            new_line_nb = line.split()
            if len(line_nb) == 0:
                line_nb = new_line_nb
            else:
                line_nb = line_nb + new_line_nb

try:
    if len(line_nb) < 2:
        raise ValueError
    line_nb = [int(x) for x in line_nb]
    for i in line_nb:
        if i <=0:
            raise ValueError
            
    for i in range(1,len(line_nb)):
        if line_nb[i] <= line_nb[i-1]:
            raise ValueError
        
except ValueError:
    print('Sorry, input file does not store valid data.')
    sys.exit()


if if_good_ride(line_nb) == 1:
    print('The ride is perfect!')
    longest_good_ride(line_nb)
    print('The minimal number of pillars to remove to build a perfect ride from the rest is: 0')
else:
    print('The ride could be better...')
    longest_good_ride(line_nb)
    pillars_remove(line_nb)
