Question 3
Consider the following picture of a tunnel, determined by a sequence of ceiling heights, namely, the sequence (7, 9, 6, 8, 7, 9, 8, 7, 9, 6, 8, 7, 9, 8, 7), and a corresponding sequence of floor heights, namely, the sequence (6, 2, 1, 5, 4, 3, 6, 6, 2, 1, 5, 4, 3, 6, 6). West of the tunnel, it is possible to see into the tunnel over a distance of 2 (units, whatever that is); this is depicted in blue. Inside the tunnel, it is possible to see into the tunnel over a maximum distance of 6; this is depicted in green. Note that on this picture, the heights of the blue and green segments are at the same level, but in general they could be at different levels. Also, there could be many green line segments, as there could be many parts of the tunnel where it is  possible to see into the tunnel over the same maximum distance.



Write a program, stored in a file named tunnel.py, that performs the following task.

The program prompts the user to input a file name. If there is no file with that name in the working directory, then the program outputs an error message and exits.

The contents of the file should consist of exactly two lines with the same number of at least two (positive or negative) integers. Consecutive numbers are separated by at least one space, and there can be extra spaces, including empty lines, anywhere. Also, the i-th number of the first sequence should be strictly greater than the i-th number of the second sequence because at any point in the tunnel, the ceiling is above the floor. If that is not the case then the program outputs another error message and exits.

The program then outputs:

the distance over which one can see into the tunnel when looking outside the tunnel from the West;

the maximum distance over which one can see into the tunnel when being inside the tunnel.
