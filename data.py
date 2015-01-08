from data_simulation_model import *


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

        def getClassNames(self):
            list(currentClass._name for currentClass in self)


class DataContainer(object):
    """TODO: Generate separable colors and names for each Data class,
    here are links
    in distinguishable palettes.
    http://tinyurl.com/okr6bmo
    http://tinyurl.com/m89l48u
    http://tinyurl.com/llay7xa
    """
    def __init__(self, dataClass, dataModel, data):
        self._dataClass = dataClass
        self._dataModel = dataModel
        self._data      = data


class DataSimulation(object):
    """Docstring for DataSimulation.
    This should be a subclass of a generic Data class.
    """

    def __init__(self, randomSeed=140589, numSamplesPerModel=100):
        """
        :randomSeed: TODO
        :models: TODO parametrize
        :numSamplesPerModel: TODO different num of saples per model.
        """
        self._randomSeed = randomSeed
        self._numSamplesPerModel = numSamplesPerModel
        self._classes = DataClasses()
        self._models = [MultiVariatedGaussianModel(0, 1, 1.2, 1, 0.8),
                  MultiVariatedGaussianModel(0, 0, 1.3, 0.7, 0.3)]
#        for indx, currentClass in enumerate(self._classes):
#            models[indx].setDataClass(currentClass)
#        data = kk
#        self._models = dict(
#            zip(self._classes.getClassNames(),
#                )
#        )

    def _str__(self):
        return 'This is a fucking shit'
