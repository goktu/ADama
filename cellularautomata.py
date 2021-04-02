#!/usr/bin/env python

""" First-Order & Second-Order Phase Transitioning Ising Model """

__author__ = "Goktug Islamoglu"
__copyright__ = "Copyright 2021, Goktug Islamoglu"
__credits__ = "Goktug Islamoglu"
__license__ = "GPL"
__version__ = "1.0.1"
__maintainer__ = "Goktug Islamoglu"
__email__ = "goktugislamoglu@gmail.com"
__status__ = "Prototype"

#    GNU Public License

#    GNU_PUBLIC_LICENSE
#    PyClustering is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
    
#    PyClustering is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
    
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.


##
# Built on: PyCX 0.3 Realtime Visualization Template
#    
# Source:
# http://pycx.sourceforge.net/
#  
# Written by:
# Chun Wong
# email@chunwong.net
#
# Revised by:
# Hiroki Sayama
# sayama@binghamton.edu


import matplotlib
matplotlib.use('TkAgg')

from pylab import *
import numpy as np

L = 100  # size of space: LxL

#ferrimagnetic-ferromagnetic transition phase - ≈ 0.769   
#p = 0.5 + np.log(1+sqrt(2))/2 - tan(pi/8)*tan(pi/8) 

#ferromagnetic phase - maximum cell count with state "1", ≈ 0.6478  
#p = np.log(1+sqrt(2))/2 + (tan(pi/8))/2 

#p = float(0.5 + (1 / (2 * sqrt(2)))) # ferrimagnetic ground state - coupled, ≈ 0.8535
#p = 0.8536 #first order transition, immediately above the ferrimagnetic ground state, demagnetization/degaussing 

#p = float(0.5 - (1 / (2 * sqrt(2)))) # antiferromagnetic ground state - coupled, ≈ 0.1464466
#p = 0.1464465 #first order transition, immediately below the antiferromagnetic ground state, no magnetization

#Inverse Ising critical temperature - paramagnetic phase, ≈ 0.4407 
#p = np.log(1+sqrt(2))/2

#Lower bound cotangent graph - "count 1" graph intersection point, ≈ 0.269   
#p = np.log(1+sqrt(2))/2 - tan(pi/8)*tan(pi/8)

#Upper bound cotangent graph - "count 1" graph intersection point, ≈ 0.828  
#p = 2*tan(pi/8)

p = np.log(1+sqrt(2))/2 + 0.5*(sqrt(2)-1) #maximum 

def init():
    global c, nc, slope0, slope1, delta, o
    c = zeros([L, L])
    for x in xrange(L):
        for y in xrange(L):
            c[x, y] = 1 if random() < p else 0
    nc = zeros([L, L])
    o = 0
    slope0 = []
    slope1 = []
    delta = []

# visualizing the content of an array

def draw():
    cla()
    imshow(c)

# count of upper neighbors of a live cell's Moore neighborhood


def number_of_upper_neighbors(x, y):
    upper_count = 0
    for dx in range(-1, 2):
        upper_count += c[(x + dx) % L, (y + 1) % L]
        # print upper_count
    return upper_count

# count of lower neighbors of a live cell's Moore neighborhood


def number_of_lower_neighbors(x, y):
    lower_count = 0
    for dx in range(-1, 2):
        lower_count += c[(x + dx) % L, (y - 1) % L]
        # print lower_count
    return lower_count

# count of right neighbors of a live cell's Moore neighborhood


def number_of_right_neighbors(x, y):
    right_count = 0
    for dy in range(-1, 2):
        right_count += c[(x + 1) % L, (y + dy) % L]
        # print right_count
    return right_count

# count of left neighbors of a live cell's Moore neighborhood


def number_of_left_neighbors(x, y):
    left_count = 0
    for dy in range(-1, 2):
        left_count += c[(x - 1) % L, (y + dy) % L]
        # print left_count
    return left_count

# count of von Neumann neighbors of a live cell


def number_of_Neumann_neighbors(x, y):
    Vertical_count = 0
    Horizontal_count = 0
    for dy in range(-1, 2):
        Vertical_count += c[x, (y + dy) % L]
        # print Vertical_count
    for dx in range(-1, 2):
        Horizontal_count += c[(x + dx) % L, y]
        # print Horizontal_count
    return Vertical_count + Horizontal_count - c[x, y]

# count of Moore neighbors of an alive cell


def number_of_Moore_neighbors(x, y):
    Moore_count = 0
    for dx in range(-1, 2):
        for dy in range(-1, 2):
            Moore_count += c[(x + dx) % L, (y + dy) % L]
            # print Moore_count
    return Moore_count - c[x, y]


def step():
    global c, nc, array, array0, array1, count, count0, count1, ratio, ratio1, slope0, slope1, delta, o
    count0 = 0
    count1 = 0
    count = 0
    ratio1 = 0
    ratio = 0
    i = 0
    j = 0
    array = []
    array0 = []
    array1 = []
    for x in xrange(L):
        for y in xrange(L):
            if c[x, y] == 1:
                array.append(c[x, y])
            g = number_of_Moore_neighbors(x, y) #CA tuning
            if c[x, y] == 0:
                nc[x, y] = 0 if g <= 6 else 1
                array0.append(c[x, y])
            elif c[x, y] == 1:
                array1.append(c[x, y])
                for z in range(-1, 2):
                    # block generation from randomly distributed points
                    
                    #neighbor updating from cell(x,y)
                    m = number_of_upper_neighbors(x, y)
                    if m == 1:
                        nc[x, (y + 1) % L] = 1

                    n = number_of_lower_neighbors(x, y)
                    if n == 1:
                        nc[x, (y - 1) % L] = 1

                    k = number_of_right_neighbors(x, y)
                    if k == 0 and (m <= 1 or n <= 1):
                        nc[(x + 1) % L, (y + z) % L] = 1

                    l = number_of_left_neighbors(x, y)
                    if l == 1 and (m > 1 or n > 1):
                        nc[(x - 1) % L, (y + z) % L] = 0

                    h = number_of_Neumann_neighbors(x, y) #CA tuning
                    if h >= 1:
                        nc[x, y] = 1 if g <= 6 else 0

                    if g / 8 > (1 - p) * p:  # coupling function
                        nc[(x + 1) % L, y] = 1
                    elif g / 8 < (1 - p) * p:
                        nc[(x - 1) % L, y] = 1
                    else:
                        nc[x, y] = 1
            i += 1
            j += g
    #count = len(array)
    count0 = len(array0)  # total count of cells with value 0 in each step
    count1 = len(array1)  # total count of cells with value 1 in each step
    print count1
    o += 1
    if o == 1:
        slope0.append(float(count0))
        slope1.append(float(count1))
        delta.append(float(j))
    elif o > 1:
        slope0.append(float(count0))
        slope1.append(float(count1))
        delta.append(float(j))
        ratio = count0 / float(count1)
        ratio0 = (j / i)
        ratio1 = ratio0 / ratio
        ratio2 = (slope0[o - 1] / float(slope1[o - 1])) - \
            (slope0[o - 2] / float(slope1[o - 2]))
        ratio3 = (delta[o - 2] - delta[o - 1]) / i
        
        #cotangent generator #for coupled and uncoupled probabilities
        if ratio1 != 1:
            #print (ratio3 / float(ratio1 * ratio1) + (1 / float(ratio1)) - ratio2)
            print (- ratio3 / float(ratio1 * ratio1) - (1 / float(ratio1)) + ratio2)
            
    c, nc = nc, c

import pycxsimulator
pycxsimulator.GUI(title='My Simulator', interval=0,
                  parameterSetters=[]).start(func=[init, draw, step])
