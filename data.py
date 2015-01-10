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
    here are links
    in distinguishable palettes.
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
            self._samples = []
            self._numOfSamples = 0
            warnings.warn(["the supplied data samples has no len() method. \n"
                           "Therefore, empty list is assumed"], RuntimeWarning)


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
        classes = DataClasses()
        numSamplesPerModel = [3] * len(classes)
        MVGaussMod = MultiVariatedGaussianModel
        models = [MVGaussMod(0, 1, 1.2, 1, 0.8, dataClass=classes[0]),
                  MVGaussMod(0, 0, 1.3, 0.7, 0.3, dataClass=classes[1])]
        buildParam = zip(classes, models, numSamplesPerModel)
        data = []
        for currentClass, currentModel, numSamples in buildParam:
            data.append(
                DataContainer(dataClass=currentClass, dataModel=currentModel,
                              dataSamples=currentModel.generate_data(numSamples))
            )
        self._data = data

    def __str__(self):
        return 'This is a fucking shit'
