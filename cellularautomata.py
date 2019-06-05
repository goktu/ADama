#!/usr/bin/env python

""" AdmaDama: Checkerboard Formation Ising Model """

# Author: Goktug Islamoglu
# 2018- (c) Copyright by Goktug Islamoglu
# License: GPL
# Email: islamoglu@itu.edu.tr

##
# Built on: PyCX 0.3 Realtime Visualization Template
#
# Source:
# http://pycx.sourceforge.net/
#
# PyCX 0.32
# Complex Systems Simulation Sample Code Repository
# 2008-2016 (c) Copyright by Hiroki Sayama
# 2012 (c) Copyright by Chun Wong & Hiroki Sayama
#         Original GUI module and simulation models
# 2013 (c) Copyright by Przemyslaw Szufel & Bogumil Kaminski
#         Extensions to GUI module, some revisions
# All rights reserved.
#

import matplotlib
matplotlib.use('TkAgg')

from pylab import *
import numpy as np

L = 100  # size of 2D lattice: LxL

p = 5 / 9  # Approximation to upper bound of 2nd order phase transition

# p = 4/9 #Approximation to lower bound of 2nd order phase transition

# p = float(0.5 + (1 / (2 * sqrt(2)))) #upper bound of 1st order phase transition
# p = 0.8536

# p = float(0.5 - (1 / (2 * sqrt(2)))) #lower bound of 1st order phase transition
# p = 0.1464466

##
# initializing randomly assigned states with probability p


def init():
    global c, nc, o
    c = zeros([L, L])
    for x in xrange(L):
        for y in xrange(L):
            c[x, y] = 1 if random() < p else 0
    nc = zeros([L, L])
    o = 0

##
# visualizing the content of an array


def draw():
    cla()
    imshow(c)

##
# count of upper neighbors of a live cell's Moore neighborhood


def number_of_upper_neighbors(x, y):
    upper_count = 0
    for dx in range(-1, 2):
        upper_count += c[(x + dx) % L, (y + 1) % L]
        # print upper_count
    return upper_count

##
# count of lower neighbors of a live cell's Moore neighborhood


def number_of_lower_neighbors(x, y):
    lower_count = 0
    for dx in range(-1, 2):
        lower_count += c[(x + dx) % L, (y - 1) % L]
        # print lower_count
    return lower_count

##
# count of right neighbors of a live cell's Moore neighborhood


def number_of_right_neighbors(x, y):
    right_count = 0
    for dy in range(-1, 2):
        right_count += c[(x + 1) % L, (y + dy) % L]
        # print right_count
    return right_count

##
# count of left neighbors of a live cell's Moore neighborhood


def number_of_left_neighbors(x, y):
    left_count = 0
    for dy in range(-1, 2):
        left_count += c[(x - 1) % L, (y + dy) % L]
        # print left_count
    return left_count

##
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

##
# count of Moore neighbors of an alive cell


def number_of_Moore_neighbors(x, y):
    Moore_count = 0
    for dx in range(-1, 2):
        for dy in range(-1, 2):
            Moore_count += c[(x + dx) % L, (y + dy) % L]
            # print Moore_count
    return Moore_count - c[x, y]

##
# step update


def step():
    global c, nc, array, array0, array1, count0, count1, o
    count0 = 0
    count1 = 0
    i = 0
    j = 0
    array = []
    array0 = []
    array1 = []
    for x in xrange(L):
        for y in xrange(L):
            array.append(c[x, y])
            g = number_of_Moore_neighbors(x, y)
            if c[x, y] == 0:
                nc[x, y] = 0 if g <= 6 else 1  # nearest-neightbor parameter
                array0.append(c[x, y])
            elif c[x, y] == 1:
                array1.append(c[x, y])
                for z in range(-1, 2):
                    # bottleneck configuration due to arrested state
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

                    h = number_of_Neumann_neighbors(x, y)
                    if h >= 1:
                        # nearest-neighbor parameter
                        nc[x, y] = 1 if g <= 6 else 0

                    if g / 8 > (1 - p) * p:  # next-nearest neighbor asymptote
                        nc[(x + 1) % L, y] = 1
                    elif g / 8 < (1 - p) * p:
                        nc[(x - 1) % L, y] = 1
                    else:
                        nc[x, y] = 1
            i += 1
            j += g
    count0 = len(array0)  # total count of cells with value 0 in each step
    count1 = len(array1)  # total count of cells with value 1 in each step

    print count1

    c, nc = nc, c

import pycxsimulator
pycxsimulator.GUI(title='My Simulator', interval=0,
                  parameterSetters=[]).start(func=[init, draw, step])
