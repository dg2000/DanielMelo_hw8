import numpy as np

import matplotlib.pyplot as plt


def sample_1(N):


    P = np.array([0.1, 0.4, 0.2, 0.3], float)

    b = np.array([-10, -5, 3, 9], float)


    return  np.random.choice(a = b, size = N, p = P)


def sample_2(N):

    return np.random.exponential(scale = 0.5,  size = N)

def get_mean(sampling_fun, N, M):

    A = np.zeros(M)

    for i in range(M):

        A[i] = np.mean(sampling_fun(N))

    return A

        

for i in range(6):

    if(i <=2):

        np.savetxt("sample_1_" + str(10**(i+1)) + ".txt", get_mean(sample_1, 10**(i+1), 10000))


    else:

        np.savetxt("sample_2_" + str(10**(i-2)) + ".txt", get_mean(sample_1, 10**(i-2), 10000))





        

            

    
