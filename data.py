from data_simulation_model import *
import numpy as np


class DataClassInstance:
    """ This is a class to define a structure storing information of the data
    class in order to identify such data class.

    The stored fields are:
        name  = 'data identifier name'
        color = '#00ff00'
    """
    def __init__(self, name, color):
        self._name  = name
        self._color = color


class DataClasses(object):
    def __new__(cls):
        return [DataClassInstance('blue', '#9b59b6'),
                DataClassInstance('red', '#e74c3c')]

        def get_class_names(self):
            list(currentClass._name for currentClass in self)


class DataContainer(object):
    """TODO: Generate separable colours and names for each Data class,
    here are links in distinguishable palettes.
    http://tinyurl.com/okr6bmo
    http://tinyurl.com/m89l48u
    http://tinyurl.com/llay7xa
    """
    def __init__(self, dataClass, dataModel, dataSamples):
        self._class = dataClass
        self._model = dataModel
        self._samples = dataSamples
        try:
            self._numOfSamples = len(dataSamples)
        except (TypeError):
            self._samples = np.array([])
            self._numOfSamples = 0
            warnings.warn(["the supplied data samples has no len() method. \n"
                           "Therefore, empty list is assumed"], RuntimeWarning)


    def get_samples_dim(self, dimension):
        """Retruns one dimension values of the samples.

        :dimension: Data dimension of interest
        :returns: returns one column of data representing one dimension of the
            data.
        """

        if self._samples.shape[1] > dimension:
            return self._samples[:,dimension]
        else:
            return np.array([])



class DataSimulation(object):
    """Docstring for DataSimulation.
    This should be a subclass of a generic Data class.
    """
    def __init__(self, randomSeed=140589):
        """
        :randomSeed: TODO
        :models: TODO parametrize
        :numSamplesPerModel: TODO different num of saples per model.
        """
        np.random.seed(randomSeed)
        self._randomSeed = randomSeed

        # Creates two classes (hardcoded?) super hard coded
        classes = DataClasses()
        numSamplesPerModel = [300] * len(classes)
        MVGaussMod = MultiVariatedGaussianModel
        models = [MVGaussMod(0, 1, 1.2, 1, 0.8, dataClass=classes[0]),
                  MVGaussMod(0, 0, 1.3, 0.7, 0.3, dataClass=classes[1])]
        # end build parameters

        buildParam = zip(classes, models, numSamplesPerModel)
        data = []
        for currentClass, currentModel, numSamples in buildParam:
            data.append(
                DataContainer(dataClass=currentClass,
                    dataModel=currentModel,
                    dataSamples=currentModel.generate_data(numSamples))
            )
        self._data = data

    def __str__(self):
        return 'This is a fucking shit'

    def draw_sample(self, axisId):
        """Draws 2D points on the axis

        :axisId: axis to draw on

        """

        print(self._data[0]._class._color)

        for i in range(len(self._data)):
            axisId.scatter(
                    self._data[i].get_samples_dim(0),
                    self._data[i].get_samples_dim(1),
                    c = self._data[i]._class._color,
                    alpha = 0.7)


def main():

    my_data = DataSimulation()
    print(my_data)

    fig = plt.figure()
    ax1 = fig.add_subplot(111)
    my_data.draw_sample(ax1)

    fig.show()

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
from sklearn.decomposition import PCA
from abc import ABCMeta, abstractmethod, abstractproperty

import math
from data import *
from random_sampling import *
import matplotlib.pyplot as plt

if __name__ == '__main__':
    main()
