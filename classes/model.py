# -*- coding: utf-8 -*-
"""
Created on Tue Jun 18 10:13:39 2019

@author: Gebruiker
"""
import numpy as np
import math
import matplotlib.pyplot as plt

from classes.population import Population
import helpers.functions as functions

class Model():
    
    def __init__(self):
    
        A,B = 16.5, 5.82
        w1,w2 = 1.487, 0.2223
        self.In = Population(A,w1)
        self.Ex = Population(B,w2)
    
    def bifurcation(self):
        
        xn = math.inf
        Alist = []
        xlist = []
        
        for A in np.arange(0.,40.,0.1):
            
            self.In.coef = A
            xn1 = functions.x_n1(xn,self.Ex,self.In)
            print(self.In.coef)
            Alist.append(A)
            xlist.append(xn1)
            
        plt.figure()
        plt.plot(Alist,xlist)
        plt.show()
    
    def runModel():
        return