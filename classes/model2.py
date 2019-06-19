# -*- coding: utf-8 -*-
"""
Created on Tue Jun 18 10:13:39 2019

@author: Gebruiker
"""
import numpy as np
import math
import matplotlib.pyplot as plt
from sympy.solvers import solve
from sympy import Symbol, tanh


from classes.population import Population
import helpers.functions as functions

class Model():
    
    def __init__(self):
    
        A,B = 10., 5.82
        w1,w2 = 1.487, 0.2223
        self.In = Population(A,w1)
        self.Ex = Population(B,w2)
    
    def bifurcation(self):
        Alist = []
        xlist = []
        x = Symbol('x')
        
        for A in np.arange(0.,4.,0.1):
            
            self.In.coef = A
            #xs = solve(functions.x_n1(x,self.Ex,self.In),x)
            xs = solve(x,A*x*(1-x))
            print(xs)
            
        for y in np.arange(-20,20,0.1):
            Alist.append(y)
            xlist.append(functions.x_n1(y,self.Ex,self.In))
        plt.figure()
        plt.plot(Alist,xlist)
        plt.plot(Alist,Alist)
        plt.show()
    
    def runModel():
        return