#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from PIL import Image
import numpy as np

#vd=open('volumedata.txt','a')
#vd.write('Particles Volumes(um^3)'+'\n')

sand_path='/Users/ZachRatliff/Documents/Important_Documents/Guven Work/writeup_april2016/particle'
def untilted(path):
    data=[]
    listing=sorted(os.listdir(path))
    for file in listing:
        if '.bmp' in file:
            im=Image.open(os.path.join(path,file),'r')
            data.append(im)
            
    white=[]; x=[]; y=[]; z=[]
    width, height=data[0].size
    grid_scale=6.1 #Measurements in micrometers
    
    for k in range(len(data)):
        for w in range(width):
            for h in range(height):
                white_pix=data[k].getpixel((w,h))
                if white_pix==255:
                    white.append((w*grid_scale,h*grid_scale,k*grid_scale))
                    x.append(w*grid_scale)
                    y.append(h*grid_scale)
                    z.append(k*grid_scale)
                
    if i<10:
        print 'Particle0%s %s'%(str(i),str(len(white)))
    else:
        print 'Particle%s %s'%(str(i),str(len(white)))
    volume=len(white)*grid_scale**3
    pfile=open(name,'a')
    pfile.write('Number of Voxels: %s' %str(len(white))+'\n')
    pfile.write('Volume is %s um^3' %str(volume)+'\n')
    for q in range(len(white)):
        pfile.write(str(white[q])+'\n')
    pfile.close()


    
listing2=sorted(os.listdir(sand_path))
i=1
for files in listing2:
    if i<10:
        name='p0%s'%str(i)+'.txt'
        name2='p0%s'%str(i)+'tilted.txt'
    else:
        name='p%s'%str(i)+'.txt'
        name2='p%s' %str(i)+'tilted.txt'
    path=sand_path+'/'+files
    untilted(path)
    i+=1

#vd.close()
