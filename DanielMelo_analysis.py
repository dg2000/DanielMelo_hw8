import numpy as np

import math

def normal_dist(x, mean, sigma):

    a = math.sqrt(1/(2*np.pi*sigma*sigma))

    b = ((x - mean)**2)

    return a*np.exp(-b/(sigma*sigma))

def get_fit(filename):
    
    archivo = np.loadtxt(files[i])

        


        

    
