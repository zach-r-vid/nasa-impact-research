#!/usr/bin/env python
# -*- coding: utf-8 -*-

#####################
#!!!!!IMPORTANT!!!!!#
#####################
"""This code scans through a directorty of particles.
The names MUST be in the format pxx.txt, where xx is the particle number
Once the code runs, it will scan ALL the particles. 
i.e. if there are 100 particle files, then it will individually show 100 images
You have to close out of all 100 images each time
It's a commitment. Not for the light of heart.

Simply set the path to the directory containing the particles.
Everything else should run smoothly from there.
Written on Ubuntu 14.04.4
Windows is not recommended (as per usual)
Has yet to be tested on Mac
-Zach (03/29/2016)"""

import os
from PIL import Image
import numpy as np
from itertools import islice
import fnmatch
import argparse
parser=argparse.ArgumentParser()
parser.add_argument("echo")

################################################
# Sets the path to the directory of coordinates#
################################################
path='/Users/ZachRatliff/Documents/Important_Documents/Guven Work/writeup_april2016'
grid_scale=6.1
desirables=[1,11,33]

############################################
#Sorts list and saves only coordinate files#
############################################
counter=1
listing1=sorted(os.listdir(path))
listing=fnmatch.filter(listing1,'p??.txt')


####################################
#Scans through each coordinate file#
#Saves coordinates into x,y,z lists#
#    Visualizes each particle      #
####################################
for files in listing:
    for q in desirables:
        counter=1
        if q<10:
            name='p0%s.txt'%str(q)
        else:
            name='p%s.txt'%str(q)
        if files==name:
            print files
            x=[];y=[];z=[];
            f=open(os.path.join(path,files),'rU')
            A=[]
            for lines in f:
                if counter>=3:
                    A=lines.split(',')
                    x.append(float(A[0][1:]))
                    y.append(float(A[1]))
                    z.append(float(A[2][:-3]))
                    counter+=1
                counter+=1
        
            from mayavi import mlab
            mlab.figure(size=(1200,900))
            mlab.points3d(x,y,z,mode='cube',scale_mode='none',resolution=5,scale_factor=grid_scale)
            mlab.show()
