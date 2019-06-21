# -*- coding: utf-8 -*-
"""
Created on Mon Jun 17 11:22:46 2019

@author: Gebruiker
"""

import classes.model as model

def main():
    
    theModel = model.Model()
    print(theModel.In.coef)
    print(theModel.Ex.weight) 
    output = theModel.runModel()

if __name__ == '__main__':
    main()