#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 21 13:38:02 2019

@author: christynataliaj
"""

class Data():
    def __init__(self):
        self.nilaiA = int(input("Input the A= "))
        self.nilaiB = int(input("Input the B= "))
        self.nilaiC = int(input("Input the C= "))
        
    def newNilaiA(self):
        return self.nilaiA

    def newNilaiB(self):
        return self.nilaiB
    
    def newNilaiC(self):
        return self.nilaiC