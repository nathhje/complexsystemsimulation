# -*- coding: utf-8 -*-
"""
Created on Tue Jun 18 10:13:39 2019

@author: Gebruiker
"""
import numpy as np
import matplotlib.pyplot as plt

import helpers.functions_guy as functions

class Model():
    
    def __init__(self):
    
        return
    
    #Running model
    def runModel(self):
        #Initial parameter values and lists to store generated data (messy but works)
        A = 14.47
        B = 5.82
        An = 13.6
        Bn = 5.82
        beta = -1
        x = 0.5
        x_s = [0.5 for i in range(200)]
        y_s = [0 for i in range(2)]
        zk_s = []
        zk_s.append(0)
        outputk_s = []
        outputk_s.append(0)
        n = []
        iext = 0
        counter = 0
        fyk_s = []
        en=0
        mu=0.002

        #Iteratively running the model to produce the output for n days
        for i in range(0, 7500):
        
            counter += 1
            if (counter +1) %100 == 0:
                iext = 0.05
            if counter %100 ==0:
                iext = 0
            
            #Function used to randomly alter the value of B every day
            # if counter %200 == 0:
            #     rand = random.randint(1,101)
            #     if rand <= 30:
            #         B = 7.65
            #     else:
            #         B = 5.82

            #Function used to randomly alter the value of A every two days (this seemed to work better than doing it every day)
            # if counter %400 == 0:
            #     rand = random.randint(1,101)
            #     if rand <= 37:
            #         A = 20
            #     else:
            #         A = 14.47

            #Making mu dependent on the output height
                #This is for manic episodes
            # if outputk_s[i-1] <= 0.01:
            #     if outputk_s[i] >= 1.45:
            #         mu = mu/10
            #         print('no')
            #     else:
            #         mu = 0.002
            #     #This is for depressed episodes
            # if outputk_s[i-1] <= 0.01:
            #     if 1 < outputk_s[i] <=1.3:
            #         mu = mu/ * 2
            #         print('no')
            #     else:
            #         mu = 0.002

            #Recusively applying equation 1
            x = functions.x_n1(x, B, A, 0.2223, 1.487)
            x_s.append(x)

            #Working out the error every day and keeping that error for the entirity of the day
            if counter %101 ==0:
                en = functions.error_estim(0,2, x_s[i], x_s[i+200])

            #application of equation 6
            g = functions.gdelta(0.3, A, An, B, Bn, 1, 0, 2, x_s[i], x_s[i+200])

            #Equation 4
            fyk = functions.fyk(3.2, beta, iext, y_s[i+1], y_s[i])
            fyk_s.append(fyk)

            #Equation 3
            ykp1, zk = functions.Rulkov(3.2, -2.5780, iext, y_s[i+1], y_s[i], zk_s[i], -0.8, 1.3, mu, g)
            zk_s.append(zk)
            y_s.append(ykp1)

            #Equation 5, the output
            outputk = functions.output(An, A, B, Bn, 1, en, zk)

            #Artistic licence, to better represent the differences in episodes and to better match the paper
            # if B == 7.65:
            #     if outputk >1.5:
            #         outputk = outputk *1.15

            # if A == 16.47:
                #if 1 < outputk < 1.35:
                    #outputk = outputk * 0.8

            outputk_s.append(outputk)
            n.append(i)

        #PLotting the output per day
        #Making x axis days
        n = [x / 250 for x in n]

        plt.plot(n, outputk_s[1:], c='blue')
        plt.ylabel('Normalised Circadian Activity')
        plt.xlabel('Time (Days)')
        plt.title('Simmulated Circadian Activity of Bipolar Individual \n in a depressed state')
        textstr = 'A = 14.47B = 5.82' 
        plt.text(20, -0.27, textstr, fontsize=8)
        # plt.scatter(n, x_s[50:], s=0.01)
        # plt.plot(n, zk_s[1:])
        plt.show()

        plt.title("Time Series of Neuronal Activity x(n)")
        plt.xlabel("Iterations (n)")
        plt.ylabel("Neuronal Activity x(n)")
        plt.scatter(n, x_s[200:], s=9, c='r', zorder=1)
        plt.plot(n, x_s[200:], zorder=2, lw = 0.05)
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

        # PLotting the Rulkov map output for our model
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
