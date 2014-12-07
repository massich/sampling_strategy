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
        # information in pytonic constructors:
        #  http://tinyurl.com/3758j8u
        #  http://tinyurl.com/424tbt7
        #  http://tinyurl.com/lrownat
        pass

    def __str__(self):
        pass

    def generate_data(self, numSamples):
        pass

    def draw_model(self, axisId):
        pass


class MultiVariatedGaussianModel(DataSimulationModel):
    """ This is the real data D class for the case of a single 2D Gaussian
    multivariate simulation process.

    Attributes:
        modelMuX     -- x mean value of the model     (modelMuX     = 0)
        modelMuY     -- y mean value of the model     (modelMuY     = 0)
        modelSigmaX  -- variance of the model along x (modelSigmaX  = 1)
        modelSigmaY  -- variance of the model along y (modelSigmaY  = 1)
        modelSigmaXY -- x,y covariance of the model   (modelSigmaXY = 0)
    """
    def __init__(self, modelMuX, modelMuY, modelSigmaX, modelSigmaY,
                 modelSigmaXY, *args, **kwargs):
        """ The following parameters can be specified in order to define define
        a multivariate 2D Gaussian model. Otherwise, defaults my apply. Any
        other argument would create an exception.

        Example:
            MultiVariatedGaussianModel( modelMuX=0,
                                        modelMuY=0,
                                        modelSigmaX=1,
                                        modelSigmaY=1,
                                        modelSigmaXY=0,
                                        )
    """
        # args -- tuple of anonymous arguments
        # kwargs -- dictionary of named arguments
        diff = kwargs.viewkeys() - {'modelSigmaXY', 'modelSigmaX',
                'modelSigmaY', 'modelMuY', 'modelMuX'}
        if diff:
            raise Exception("Invalid args: " + ', '.join(diff))
        else:
            self.modelMuX     = kwargs.pop(modelMuX,     0)
            self.modelMuY     = kwargs.pop(modelMuY,     0)
            self.modelSigmaX  = kwargs.pop(modelSigmaX,  1)
            self.modelSigmaY  = kwargs.pop(modelSigmaY,  1)
            self.modelSigmaXY = kwargs.pop(modelSigmaXY, 0)

    def __str__(self):
        return 'Real-Data simulation (2D multi-variated Model):\n' \
               '\tmean x:{0}, y:{1}\n' \
               '\tstd  x:{2}, y:{3}, xy:{4}' \
               '\n'.format(self.modelMuX, self.modelMuY, self.modelSigmaX, 
                      self.modelSigmaY, self.modelSigmaXY)

    def generate_data(sef, numSamples):
        pass

    def draw_model(self, axisId):
        pass
