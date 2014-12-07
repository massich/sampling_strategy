import numpy as np
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
from sklearn.decomposition import PCA
from abc import ABCMeta, abstractmethod
import math


class DataSimulationModel(object):
    """ This is the real data D class for the case of simulation.
        The simulated data can be drawn from different models which are
        intended to inherit from this this class. Each model should :
          -understand its own building parameters or through an error.
          -implement the abstractmethods
    """
    __metaclass__ = ABCMeta

    @abstractmethod
    def __init__(self, *args, **kwargs):
        print "this is the abstract class constructor"

    def __str__(self):
        pass

    def generate_data(self, numSamples):
        pass

    def draw_model(self, axisId):
        pass


class MultiVariatedGaussianModel(DataSimulationModel):
    def __init__(self, *args, **kwargs):
        # args -- tuple of anonymous arguments
        # kwargs -- dictionary of named arguments
        print 'args: ', args, ' kwargs: ', kwargs

    def generate_data(sef, numSamples):
        pass

    def draw_model(self, axisId):
        pass
