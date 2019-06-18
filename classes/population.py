# -*- coding: utf-8 -*-
"""
Created on Tue Jun 18 10:15:46 2019

@author: Gebruiker
"""
import math

class Population:
    
    def __init__(self,coef,weight):
        
        self.coef = coef
        self.weight = weight
        
    def performance(self,xn):
        print(self.coef)
        return self.coef*math.tanh(self.weight*xn)