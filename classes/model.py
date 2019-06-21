# -*- coding: utf-8 -*-
"""
Created on Tue Jun 18 10:13:39 2019

@author: Gebruiker
"""
import numpy as np
import math
import matplotlib.pyplot as plt
import random


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
        A = 14.5
        B = 8
        An = 13.6
        Bn = 5.82
        beta = -1



        #These cannot be infinity, but then what do we do?!
        x = 10
        x_s = [10 for i in range(5)]
        iext = 0
        y_s = [0 for i in range(2)]
        zk_s = []
        zk_s.append(0)
        outputk_s = []
        n = []
        iext_s = []
        counter = 0
        fyk_s = []
        for i in range(0, 10000):
            # if i %2 != 0:
            #     iext = 0
            # else:
            #     iext = -2
            counter += 1
            if counter %101 == 0:
                iext = 0.01
            if counter %200 ==0:
                iext = 0
            iext_s.append(iext)

            x = functions.x_n1(x, B, A, 0.2223, 1.487)
            x_s.append(x)
            
            en = functions.error_estim(0,20, x_s[i], x_s[i+5])

            g = functions.gdelta(0.3, A, An, B, Bn, 0.1, 0, 100, x_s[i], x_s[i+5])

            fyk = functions.fyk(3.2, beta, iext, y_s[i+1], y_s[i])
            fyk_s.append(fyk)

            ykp1, zk = functions.Rulkov(3.2, -2.5780, iext, y_s[i+1], y_s[i], zk_s[i], -0.8, 1.3, 0.002, g)
            zk_s.append(zk)
            y_s.append(ykp1)


            outputk = functions.output(An, A, B, Bn, 1, en, zk)
            outputk_s.append(outputk)

            n.append(i)

        plt.plot(n, outputk_s)
        # plt.plot(n, zk_s[1:])
        plt.show()





        # #Plotting things from Rulkov paper to see if our results match (and they do, apart from som strange behaviour for plot 2)
        # #PLot 1
        # i_s=[]
        # i_s.append(1.31)
        # fykp = []
        # a =0
        # for i in np.arange(-1.3, 1, 0.01):
        #     i_s.append(i)
        #     fykp.append(functions.fyk(3.2, beta, iext, i_s[a+1], (i_s[a] - 0.7)))
        #     a +=1
        # plt.plot(i_s[1:], fykp)
        # plt.show()

        # #Plot 2
        Iext = 0
        i_s=[]
        i_s.append(-0.21)
        zk_s = []
        zk_s.append(0)
        a =0
        ykp1_s = []
        ykp1_s.append(0)
        ykp1_s.append(0)
        mv_s = []
        a_s =[]
        counter = 0
        for i in np.arange(-0.2, 8.0, 0.01):
            ykp1, zk = functions.Rulkov(3.2, -2.5780, Iext, ykp1_s[a+1], ykp1_s[a], zk_s[a], -0.8, 1.3, 0.002, 0.2)
            ykp1_s.append(ykp1)
            zk_s.append(zk)
            i_s.append(i)
            a +=1
            a_s.append(a)
            mv = -25 + ykp1*80 + zk*85
            mv_s.append(mv)
            counter += 1
            if counter == 298:
                Iext = 0.01
            if counter == 400:
                Iext = 0
                counter = 0
        # plt.plot(a_s, zk_s[1:])
        # plt.show()

        return outputk_s, n
