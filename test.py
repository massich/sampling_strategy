import numpy as np
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
from sklearn.decomposition import PCA
from abc import ABCMeta, abstractmethod, abstractproperty

import math
from data import *
from random_sampling import *
import matplotlib.pyplot as plt

x = DataSimulation(randomSeed=15031984)
yy = x._models.pop('blue')
print yy

print yy.data_model_information()
print x

# print 'From the Datasimulation Default'
# x = DataSimulation()
# print x._models[0]
# print x._models[1]
#
# print 'From a created string'
# xx = ' '
# for puta in self._models:
#     xx.join('{0} \n in colour {1} with {2} samples'.format(
#              puta.__str__, 'red',
#              self._numSamplesPerModel))
# print xx
