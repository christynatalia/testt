#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 21 13:38:02 2019

@author: christynataliaj
"""

class Data():
    def __init__(self):
        self.__nilaiA = int(input("Input the A= "))
        self.__nilaiB = int(input("Input the B= "))
        self.__nilaiC = int(input("Input the C= "))
        
    def newNilaiA(self):
        return self.__nilaiA

    def newNilaiB(self):
        return self.__nilaiB
    
    def newNilaiC(self):
        return self.__nilaiC