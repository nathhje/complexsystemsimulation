# -*- coding: utf-8 -*-
"""
Created on Tue Jun 18 10:13:39 2019

@author: Gebruiker
"""

from classes.population import Population

class Model():
    
    def __init__(self):
    
        A,B = 16.5, 5.82
        w1,w2 = 1.487, 0.2223
        self.In = Population(A,w1)
        self.Ex = Population(B,w2)
    
    def runModel():
        return