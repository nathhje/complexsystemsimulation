# -*- coding: utf-8 -*-
"""
Created on Tue Jun 18 10:13:39 2019

@author: Gebruiker
"""
import numpy as np
import math
import matplotlib.pyplot as plt

from classes.population import Population
import helpers.functions_guy as functions
import helpers.functions as functions1

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
            xn1 = functions1.x_n1(xn,self.Ex,self.In)
            print(self.In.coef)
            Alist.append(A)
            xlist.append(xn1)
            
        plt.figure()
        plt.plot(Alist,xlist)
        plt.show()
    
    def runModel(self):

        An = 13.6
        Bn = 5.82

        beta = 1
        iext = 0.5

        x = math.inf 
        x_s = []
        x_s.append(x)
        y_s = []
        y_s.append(0)
        zk_s = []
        zk_s.append(0)
        outputk_s = []
        for i in range(0,100):
            x = functions.x_n1(x, 5.82, 16.47, 0.2223, 1.487)
            x.append(x)
            en = functions.error_estim(0,100, x_s[i-5], x_s[i-1])

            g = functions.gdelta(0.3, 16.47, An, 5.82, Bn, 1, 0, 100, x_s[i-5], x_s[i-1])

            fyk = functions.fyk(3.2, beta, iext, 0.0001, y_s[i-1])
            y.append(fyk)

            zk = functions.Rulkov(3.2, beta, iext, 0.0001, y_s[i-2], zk_s[i-1], -0.8, 1.3, 0.002, 0.3, 16.47, An, 5.82, Bn, 1, 0, 100, x_s[i-5], x_s[i-1])
            zk_s.append(zk)

            outputk = functions.output(An, 16.47, 5.82, Bn, 1, 0,100, x_s[i-5], x_s[i-1], zk)
            outputk_s.append(outputk)


        return outputk_s