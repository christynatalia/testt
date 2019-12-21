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





hasil = Data()

hasilA = int(hasil.newNilaiA())
hasilB = int(hasil.newNilaiB())
hasilC = int(hasil.newNilaiC())


def discriminant():
    nilaidiskriminan =(((hasilB**2) - (4*hasilA*hasilC)))
    if nilaidiskriminan < 0 :
        print("You can't count because ini akar imaginer")
        quit()
    else:
        akard = math.sqrt(int(nilaidiskriminan))
        global x1
        global x2
        x1 = round((-hasilB+ akard) / (2*hasilA),2)
        x2 = round((-hasilB- akard) / (2*hasilA),2)
        return x1,x2

print(discriminant())



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

if hasilA > 0:   
    x=numpy.linspace(int(x2),int(x1),50);
    y=(hasilA *( x ** 2)) +(( x * hasilB ))+ hasilC
    pyplot.plot(x,y);
    pyplot.title("Parabola curve")
    pyplot.xlabel("x axis")
    pyplot.ylabel("y axis")
    pyplot.grid()
    pyplot.show()
else:
    x=numpy.linspace(int(x2),int(x1),100);
    y= -(hasilA *( x ** 2)) +(( x * hasilB ))+ hasilC
    pyplot.plot(x,y);
    pyplot.title("Parabola curve")
    pyplot.xlabel("x axis")
    pyplot.ylabel("y axis")
    pyplot.grid()
    pyplot.show()
    
