from numpy import random, sqrt

def montecarlo(dim, fs, rang, count=1000000):
    inside = 0
    points = 0
    totalvolume = abs(rang[1]-rang[0])**dim
    while count == -1 or points < count:
        inside+=all(fs(random.uniform(low=rang[0], high=rang[1], size=(dim,))))
        points+=1
        if points%100000 == 0:
            print(inside/points*totalvolume)
    return inside/points*totalvolume
