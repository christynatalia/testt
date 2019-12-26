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

#Make the lists for the history
a = ['A = ']
b = ['B = ']
c = ['C = ']

#Loop everytime the user type yes on the introduction
while True:
    intro = Introduction()
    intromsg = intro.programintro()
    intromsg = intromsg.title()
    if intromsg == 'Yes':
        print("The formula is Ax^{2} + Bx + C")
        value = Data()
        valueA = int(value.newNilaiA())
        valueB = int(value.newNilaiB())
        valueC = int(value.newNilaiC())
    elif intromsg == 'No':
        print("bye")
        sys.exit()
    else:
       print("Error. Please restart this program")
       sys.exit()
       
       
    if valueA != 0:
        def discriminant():
            global discriminantValue
            discriminantValue =(((valueB**2) - (4*valueA*valueC)))
            return discriminantValue
            
            
        def roots():
            if discriminantValue < 0 :
                print("can't count because it is imaginary(non-real)roots" )
                sys.exit()
            else:
                roots = math.sqrt(int(discriminantValue))
                global x1
                global x2
                x1 = round((-valueB + roots) / (2*valueA),2)
                x2 = round((-valueB - roots) / (2*valueA),2)
                return x1,x2
        
        print("The discriminant of this graph is =",discriminant())
        print("X1,X2 = ",roots())
        
        def highestpoint():
            global highx
            global highy
            highx = (-valueB) / (2 * valueA)
            highy = -((valueB**2) - (4*valueA*valueC))/ (4*valueA)
            return highx,highy
        
        print("The highest point of this graph is = ",highestpoint())
        
        
        def conclusion():
            if (discriminantValue > 0 and valueA > 0) or (discriminantValue > 0 and valueA < 0):
                conclmsg = ("The conclusion is = Grafik memotong sumbu x ")
            elif (discriminantValue == 0 and valueA > 0) or (discriminantValue == 0 and valueA < 0):
                conclmsg = ("The conclusion is = Grafik menyinggung sumbu x ")
            elif (discriminantValue < 0 and valueA > 0) or (discriminantValue < 0 and valueA < 0):
                conclmsg = ("The conclusion is garis tidak memotong sumbu x ")
            return conclmsg
        
        print(conclusion())
        
        def history():
            a.append(valueA)
            b.append(valueB)
            c.append(valueC)
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
        
        
        #Make the graph 
        x=numpy.linspace(float(x2),float(x1),50);
        y=(valueA *( x ** 2)) +(( x * valueB ))+ valueC
        pyplot.plot(x,y);
        plt.scatter(float(highx),float(highy),s=10, c= "blue",label = 'HP=' + '('+ str(highx) + ',' + str(highy)+')')
        plt.scatter(float(x1),float((valueA *( x1 ** 2)) +(( x1 * valueB ))+ valueC), s = 20, c= 'red', label = 'x1('+ str(x1)+ str(')'))
        plt.scatter(float(x2),float((valueA *( x2 ** 2)) +(( x2 * valueB ))+ valueC), s = 20, c= 'black', label = 'x2('+ str(x2)+ str(')'))
        plt.legend()
        pyplot.title("Quadratic Equations Curve")
        pyplot.xlabel("x axis")
        pyplot.ylabel("y axis")
        pyplot.grid()
        pyplot.show()
        plt.show()
        
    else:
        print("You can't assign 0 as A. Please try again.")
    


    
 
