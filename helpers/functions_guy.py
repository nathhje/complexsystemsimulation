import math
import numpy as np

def x_n1(xn, B, A, w1, w2):
    x_n1 = B*(math.tanh(w2*xn)) - A*(math.tanh(w1*xn))
    return x_n1

def error_estim(n1, n2, xn, xp): 
    en = (1/(n2-n1+1))*(abs((xn-xp) - xn))
    return en

def gnorm(A, An, B, Bn):
    Adiff = ((A/An) -1)* np.sign((A/An) - 1)
    Bdiff = ((B/Bn) -1)* np.sign((B/Bn) - 1)
    gnorm = Adiff - Bdiff
    return gnorm

def output(An, A, B, Bn, w3, n1,n2,xn,xp, zk):
    output = (1.1- (gnorm(A, An, B, Bn)) * np.tansig(w3 * error_estim(n1,n2,xn,xp)))*zk
    return output

def gdelta(gopt, A, An, B, Bn, wd, n1,n2,xn,xp):
    delta = np.tanh(wd* error_estim(n1,n2,xn,xp))
    Adiff = ((A/An) -1)* np.sign((A/An) - 1) * delta 
    Bdiff = ((B/Bn) -1)* np.sign((B/Bn) - 1) * delta 
    g = gopt + (Adiff - Bdiff)
    return g

def fyk(alpha, beta, Iext, yk, ykm1):
    u = beta + Iext
    if yk <= 0:
        return alpha/(1-yk) + u
    elif 0 < yk < alpha + u and ykm1 <= 0:
        return alpha + u 
    elif yk >= alpha + u or ykm1 > 0:
        return -1


def Rulkov(alpha, beta, Iext, yk, ykm1, zk, yp, zs, mu, gopt, A, An, B, Bn, wd, n1,n2,xn,xp):
    def epsilon(y, yth):
        return np.heaviside(y - yth)
    
    ykp1 = (1- epsilon(zk, yth)) * fyk(alpha, beta, Iext, yk, ykm1) + epsilon(zk, yth)*yp
    
    if yk > alpha + u or ykm1 > 0:
        zkp1 = zs
    else:
        zkp1 = (1-mu) * zk - gdelta(gopt, A, An, B, Bn, wd, n1,n2,xn,xp) * zk * ((1-zk)**2)

    return ykp1, zkp1 

