# python to make gaussian signal
import numpy as np

def g(a,N):
    l = []
    for x in range(-N//2, N//2, 1):
        l.append(np.exp(-a*x**2))
    return l

def normal(mu,std,N):
    l = []
    for x in range(-N//2, N//2, 1):
        l.append(1 / (std*np.sqrt(2*np.pi)) * np.exp(-0.5 * (x - mu)**2 / std**2))
    return l
