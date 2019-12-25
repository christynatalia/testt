#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 21 13:39:41 2019

@author: christynataliaj
"""

from fungsikuadrat import Data

import matplotlib.pyplot as plt

import math

import numpy

from matplotlib import pyplot

from setttings import Introduction

import sys

a = []
b = []
c = []

while True:
    intro = Introduction()
    intromsg = intro.programintro()
    intromsg = intromsg.title()
    if intromsg == 'Yes':
        print("The formula is Ax^{2} + Bx + C")
        hasil = Data()
        hasilA = int(hasil.newNilaiA())
        hasilB = int(hasil.newNilaiB())
        hasilC = int(hasil.newNilaiC())
    elif intromsg == 'No':
        print("bye")
        sys.exit()
    else:
       print("Error. Please restart this program")
       sys.exit()
       
       
    if hasilA != 0:
        def discriminant():
            global nilaidiskriminan
            nilaidiskriminan =(((hasilB**2) - (4*hasilA*hasilC)))
            return nilaidiskriminan
            
            
        def akard():
            if nilaidiskriminan < 0 :
                print("can't count because it is imaginary(non-real)roots" )
                sys.exit()
            else:
                akard = math.sqrt(int(nilaidiskriminan))
                global x1
                global x2
                x1 = round((-hasilB+ akard) / (2*hasilA),2)
                x2 = round((-hasilB- akard) / (2*hasilA),2)
                return x1,x2
        
        print("The discriminant of this graph is =",discriminant())
        print("X1,X2 = ",akard())
        
        def highestpoint():
            global highx
            global highy
            highx = (-hasilB) / (2 * hasilA)
            highy = -((hasilB**2) - (4*hasilA*hasilC))/ (4*hasilA)
            return highx,highy
        
        print("The highest point of this graph is = ",highestpoint())
        
        
        def conclusion():
            if (nilaidiskriminan > 0 and hasilA > 0) or (nilaidiskriminan > 0 and hasilA < 0):
                value = ("The conclusion is = Grafik memotong sumbu x ")
            elif (nilaidiskriminan == 0 and hasilA > 0) or (nilaidiskriminan == 0 and hasilA < 0):
                value = ("The conclusion is = Grafik menyinggung sumbu x ")
            elif (nilaidiskriminan < 0 and hasilA > 0) or (nilaidiskriminan < 0 and hasilA < 0):
                value = ("The conclusion is garis tidak memotong sumbu x ")
            return value
        
        print(conclusion())
        
        def history():
            a.append(hasilA)
            b.append(hasilB)
            c.append(hasilC)
            return a,b,c
        
        print("History = ",history())
        
         
        
        #AT FIRST, I USED THIS ONE BUT IT DIDN'T WORK REALLY WELL. IT'S NOT SAME LIKE THE 
        #REAL QUADRATIC EQUATIONS'S GRAPH.
        #a = []
        #b = [] 
        
        #for x in range(int(x2),int(x1+1),1):
            #y= (hasilA *( x ** 2)) +(( x * hasilB ))+ hasilC
            #a.append(x)
            #b.append(y)
        
        
        #fig= plt.figure()
        #axes=fig.add_subplot(111)
        #axes.plot(a,b)
        #plt.show()
        
    
        x=numpy.linspace(float(x2),float(x1),50);
        y=(hasilA *( x ** 2)) +(( x * hasilB ))+ hasilC
        pyplot.plot(x,y);
        plt.scatter(float(highx),float(highy),s=10, c= "blue",label = 'HP=' + '('+ str(highx) + ',' + str(highy)+')')
        plt.scatter(float(x1),float((hasilA *( x1 ** 2)) +(( x1 * hasilB ))+ hasilC), s = 20, c= 'red', label = 'x1('+ str(x1)+ str(')'))
        plt.scatter(float(x2),float((hasilA *( x2 ** 2)) +(( x2 * hasilB ))+ hasilC), s = 20, c= 'black', label = 'x2('+ str(x2)+ str(')'))
        plt.legend()
        pyplot.title("Parabola curve")
        pyplot.xlabel("x axis")
        pyplot.ylabel("y axis")
        pyplot.grid()
        pyplot.show()
        plt.show()
        
    else:
        print("You can't assign 0 as A. Please try again.")
    


    
 
