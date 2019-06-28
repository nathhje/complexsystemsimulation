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
        w1,w2 = 0.2223, 1.478
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
        A = 14.47
        B = 5.82
        An = 13.6
        Bn = 5.82
        beta = -1



        #These cannot be infinity, but then what do we do?!
        x = 0.5
        x_s = [0.5 for i in range(200)]
        y_s = [0 for i in range(2)]
        zk_s = []
        zk_s.append(0)
        outputk_s = []
        outputk_s.append(0)
        n = []
        iext_s = []
        iext = 0
        counter = 0
        fyk_s = []
        en=0
        mu=0.002
        for i in range(0, 7500):
        
            counter += 1
            if (counter +1) %100 == 0:
                iext = 0.05
            if counter %100 ==0:
                iext = 0
            
            
            # if counter %200 == 0:
            #     rand = random.randint(1,101)
            #     if rand <= 30:
            #         B = 7.65
            #     else:
            #         B = 5.82

            # if counter %400 == 0:
            #     rand = random.randint(1,101)
            #     if rand <= 37:
            #         A = 20
            #     else:
            #         A = 14.47

            # if counter %150 == 0:
            #     mu = 0.02
            #     rand = random.randint(1,101)
            #     if rand <=47:
            #         mu = mu * rand/100
            #         print('yes')
            #     elif 47 < rand < 95:
            #         mu = mu * rand/15
            #         print('no')
            #     else:
            #         mu = 0.02
            # mu = 0.002
            # if outputk_s[i-1] <= 0.01:
            #     # mu = 0.002
            #     if outputk_s[i] <=1.2:
            #         mu = mu * 3
            #         print('yes')
                # else: 
                #     mu = 0.002
            if outputk_s[i-1] <= 0.01:
                if outputk_s[i] >= 1.45:
                    mu = mu/10
                    print('no')
                else:
                    mu = 0.002


            x = functions.x_n1(x, B, A, 0.2223, 1.487)
            x_s.append(x)
            if counter %101 ==0:
                en = functions.error_estim(0,2, x_s[i], x_s[i+200])

            g = functions.gdelta(0.3, A, An, B, Bn, 1, 0, 2, x_s[i], x_s[i+200])
            fyk = functions.fyk(3.2, beta, iext, y_s[i+1], y_s[i])
            fyk_s.append(fyk)

            ykp1, zk = functions.Rulkov(3.2, -2.5780, iext, y_s[i+1], y_s[i], zk_s[i], -0.8, 1.3, mu, g)
            zk_s.append(zk)
            y_s.append(ykp1)


            outputk = functions.output(An, A, B, Bn, 1, en, zk)

            if B == 7.65:
                if outputk >1.5:
                    outputk = outputk *1.15
                    # print(outputk)

            outputk_s.append(outputk)
            n.append(i)

        n = [x / 250 for x in n]

        plt.plot(n, outputk_s[1:], c='blue')
        plt.ylabel('Normalised Circadian Activity')
        plt.xlabel('Time (Days)')
        plt.title('Simmulated Circadian Activity of Bipolar Individual \n in a depressed state')
        textstr = 'A = 14.47B = 5.82/7.65' 
        plt.text(20, -0.27, textstr, fontsize=8)
        # plt.scatter(n, x_s[50:], s=0.01)
        # plt.plot(n, zk_s[1:])
        plt.show()

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
