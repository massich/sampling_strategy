from data_base_creator import *
from data_base import *
import numpy as np


class DataSimulation (object, DataBaseCreator):
    """
    Datasimulator is the DataBase constructor class for the simulation case.
    This class methods, allow to generate such data in multiple manners.

    :version: 0.0.1
    :author: sik
    """

    def __init__(self, randomSeed=None):
        """
        Initialize the data generation with a particular randomSeed
        """
        #np.random.seed(randomSeed)
        self._randomSeed = randomSeed

    def generate_default2MVGM_testcase(self, numSamples=30):
        """
        Generate a 2 Multi-variated Gaussian class example

        Args:
            numSamples (int,optional): number of samples to generate for each
                class. Defaults to 30.

        Return:
            a **two**-class DataBase object of 2D data. Both classes follow a multivariated Gaussian distribution.

        :rtype: DataBase
        :version: 0.0.1
        :author: sik

        .. todo:: [doc] insert the 2D class ploting

        """
        np.random.seed(self._randomSeed)

        classes = [DataClassInstance('blue', '#9b59b6'),
                   DataClassInstance('red', '#e74c3c')]

        MVGaussMod = MultiVariatedGaussianModel
        models = [MVGaussMod(0, 1, 1.2, 1, 0.8),
                  MVGaussMod(0, 0, 1.3, 0.7, 0.3)]

        samples = [m.generate_data(numSamples) for m in models]

        return DataBase([DBElement(z) for z in zip(classes, models, samples)])
