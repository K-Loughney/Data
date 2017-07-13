#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun  6 11:12:38 2017

@author: Kerri Loughney
"""

import matplotlib.pyplot as plt
from xml.dom import minidom
          
xmldoc = minidom.parse('/home/shas/Documents/Kerri/Masters/Week_Long.xml')
#xmldoc = minidom.parse('/home/shas/Documents/Kerri/Masters/Coincidence_28_4_17and5_5_17/Coincidence_chris_001.xml')

itemlist = xmldoc.getElementsByTagName('Data') 
print ("Data: ", len(itemlist))

V = []

histmin1 = []
histmin2 = []

events = xmldoc.getElementsByTagName('Event')

for ev in events:
    chn1 = ev.getElementsByTagName('CHN1')[0]
    #print (chn1)
    data1 = chn1.getElementsByTagName('Data')[:]
    mindata1 = 0
    for num in range (0, 1024):
        V1 = float(data1[num].childNodes[0].data.split(',')[1])
        if V1<mindata1:
            mindata1 = V1
        T1 = data1[num].childNodes[0].data.split(',')[0]
        #print (V1)
    #print (mindata1)       
    histmin1.append(mindata1)   
        
    chn2 = ev.getElementsByTagName('CHN2')[0]
   # print (chn2)
    data2 = chn2.getElementsByTagName('Data')[:]
    mindata2 = 0 
    for num in range (0, 1024):
        V2 = float(data2[num].childNodes[0].data.split(',')[1])
        if V2<mindata2:
            mindata2 = V2
        T2 = data2[num].childNodes[0].data.split(',')[0]
    #print (mindata2)
    histmin2.append(mindata2)
    
#print (histmin1)
#print (histmin2)

n, bins, patches = plt.hist(histmin1, 50, normed =1, facecolor='green', alpha=0.75)
plt.xlabel('Voltage/mV'), plt.ylabel(''), plt.title('CH1 Peak-To-Peak Voltages')
ax = plt.axes()    
plt.axis([0,-600, 0, 0.04])  
ax.yaxis.grid(True, linewidth=0.5) 
ax.xaxis.grid(True, linewidth=0.5)
plt.savefig('Coinc_WL_CH1.png')
plt.show()

n, bins, patches = plt.hist(histmin2, 50, normed =1, facecolor='blue', alpha=0.75)
plt.xlabel('Voltage/mV'), plt.ylabel(''), plt.title('CH2 Peak-To-Peak Voltages')
ax = plt.axes()
plt.axis([0,-600, 0, 0.07])          
ax.yaxis.grid(True, linewidth=0.5) 
ax.xaxis.grid(True, linewidth=0.5)
plt.savefig('Coinc_WL_CH2.png')
plt.show()