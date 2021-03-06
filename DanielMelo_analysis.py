import numpy as np

import math

import scipy

def normal_dist(x, mean, sigma):

    #La constante de normalizacion

    a = math.sqrt(1/(2*np.pi*sigma*sigma))

    # el exponente de la gaussiana

    b = ((x - mean)**2)

    return a*np.exp(-b/(sigma*sigma))

def get_fit(filename):
    
    archivo = np.loadtxt(files[i])

    freqs, bins = np.histogram(archivo, named=true)

    y = freqs

    x = 0.5*(bins[:-1] + bins[1:])

    #q son mis parametros optimizados

    q, w = scipy.optimize.curve_fit(normal_dist, y, x)

    print "El ajuste de prom es " + str(q[0]) + " y el ajuste de sigma es " + w[0]




        


        

    
