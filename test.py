import numpy as np
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
from sklearn.decomposition import PCA
from abc import ABCMeta, abstractmethod, abstractproperty

    def draw_model(self, axisId):
        pass


class MultiVariatedGaussianModel(DataSimulationModel):
    def __init__(self, *args, **kwargs):
        # args -- tuple of anonymous arguments
        # kwargs -- dictionary of named arguments
        print "this is the Child class constructor"
        print 'args: ', args, ' kwargs: ', kwargs

    def generate_data(sef, numSamples):
        pass

    def draw_model(self, axisId):
        pass
=======
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
>>>>>>> feature/abstractSimulationModel
