#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 27 14:52:12 2017

@author: KL
"""

import matplotlib.pyplot as plt


trig = 0
histch1 = []
histch2 = []
histch3 = []
histch4 = []

with open("Two_Wk_Run2.dat") as d:
    d=[x.strip() for x in d if x.strip()]
    data=[tuple(map(float,x.split())) for x in d[2:]]
    event=[x[0] for x in data]
    ts=[x[1] for x in data]
    
    CH1=[x[2] for x in data]
    ch1_t=[x[3] for x in data]
    ch1_vpp=[x[4] for x in data]
    histch1.append(ch1_vpp)
    
    CH2=[x[5] for x in data]
    ch2_t=[x[6] for x in data]
    ch2_vpp=[x[7] for x in data] 
    histch2.append(ch2_vpp)
    
    CH3=[x[8] for x in data]
    ch3_t=[x[9] for x in data]
    ch3_vpp=[x[10] for x in data]  
    histch3.append(ch3_vpp)
    
    CH4=[x[11] for x in data]
    ch4_t=[x[12] for x in data]
    ch4_vpp=[x[13] for x in data]    
    histch4.append(ch4_vpp)
    
    #print ("Number: ",event)
    #print ("Timestamp: ",ts)
   # print ("CH1 Trig?: ",CH1)
    #print ("CH1 Time/ns: ",ch1_t)
    #print ("CH1 Voltage: ",ch1_vpp)
      

n, bins, patches = plt.hist(histch1, 50, normed =1, facecolor='green', alpha=0.75)
plt.xlabel('Voltage/mV'), plt.ylabel(''), plt.title('CH1 Peak-To-Peak Voltages')
ax = plt.axes()    
#plt.axis([0,500, 0, 0.025])  
ax.yaxis.grid(True, linewidth=0.5) 
ax.xaxis.grid(True, linewidth=0.5)
plt.savefig('Two_WL_R2_CH1.png')
plt.show()

n, bins, patches = plt.hist(histch2, 50, normed =1, facecolor='blue', alpha=0.75)
plt.xlabel('Voltage/mV'), plt.ylabel(''), plt.title('CH2 Peak-To-Peak Voltages')
ax = plt.axes()    
plt.axis([0,250, 0, 0.09]) 
ax.yaxis.grid(True, linewidth=0.5) 
ax.xaxis.grid(True, linewidth=0.5)
plt.savefig('Two_WL_R2_CH2.png')
plt.show()

n, bins, patches = plt.hist(histch3, 50, normed =1, facecolor='red', alpha=0.75)
plt.xlabel('Voltage/mV'), plt.ylabel(''), plt.title('CH3 Peak-To-Peak Voltages')
ax = plt.axes()    
plt.axis([0,250, 0, 0.09])  
ax.yaxis.grid(True, linewidth=0.5) 
ax.xaxis.grid(True, linewidth=0.5)
plt.savefig('Two_WL_R2_CH3.png')
plt.show()

n, bins, patches = plt.hist(histch4, 50, normed =1, facecolor='yellow', alpha=0.75)
plt.xlabel('Voltage/mV'), plt.ylabel(''), plt.title('CH4 Peak-To-Peak Voltages')
ax = plt.axes()    
plt.axis([0,250, 0, 0.08]) 
ax.yaxis.grid(True, linewidth=0.5) 
ax.xaxis.grid(True, linewidth=0.5)
plt.savefig('Two_WL_R2_CH4.png')
plt.show()
