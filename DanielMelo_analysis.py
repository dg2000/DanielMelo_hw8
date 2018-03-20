import numpy as np

import math

import scipy

def normal_dist(x, mean, sigma):

    a = math.sqrt(1/(2*np.pi*sigma*sigma))

    b = ((x - mean)**2)

    return a*np.exp(-b/(sigma*sigma))

def get_fit(filename):
    
    archivo = np.loadtxt(files[i])

    freqs, bins = np.histogram(archivo, named=true)

    y = freqs

    x = 0.5*(bins[:-1] + bins[1:])

    q, w = scipy.optimize.curve_fit(normal_dist, y, x)

    print "El ajuste de prom es " + str(q) + " y el ajuste de sigma es " + w




        


        

    
