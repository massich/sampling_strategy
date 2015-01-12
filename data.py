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

    def get_range(self):
        """ get_samples_range retoruns [xmin, xmax, ymin, ymax] of the samples
        TODO: This should be done as nDimension[(min,max) tuple]
        """
        return [min(self._samples[:, 0]), max(self._samples[:, 0]),
                min(self._samples[:, 1]), max(self._samples[:, 1])]

    def get_samples_dim(self, dimension):
        """Retruns one dimension values of the samples.

        :dimension: Data dimension of interest
        :returns: returns one column of data representing one dimension of the
        data.
        """

        if self._samples.shape[1] > dimension:
            return self._samples[:, dimension]
        else:
            return np.array([])


class DataSimulation(object):
    """Docstring for DataSimulation.
    This should be a subclass of a generic Data class.
    """
    def __init__(self, randomSeed=140589, n=3):
        """
        :randomSeed: TODO
        :models: TODO parametrize
        :numSamplesPerModel: TODO different num of saples per model.
        """
        np.random.seed(randomSeed)
        self._randomSeed = randomSeed

        # Creates two classes (hardcoded?) super hard coded
        classes = DataClasses()
        numSamplesPerModel = [n] * len(classes)
        MVGaussMod = MultiVariatedGaussianModel
        models = [MVGaussMod(0, 1, 1.2, 1, 0.8, dataClass=classes[0]),
                  MVGaussMod(0, 0, 1.3, 0.7, 0.3, dataClass=classes[1])]
        # end build parameters

        buildParam = zip(classes, models, numSamplesPerModel)
        data = []
        for currentClass, currentModel, nSamples in buildParam:
            data.append(
                DataContainer(dataClass=currentClass,
                              dataModel=currentModel,
                              dataSamples=currentModel.generate_data(nSamples))
            )
        self._data = data

    def __str__(self):
        modelsInfoString = "\t{0}_({1})_________________________\n\t\tmodel:: {2}\n \t\tsamples:: {3}\n \t\trange:: {4}\n"
        modelsInfo = ""
        for d in self._data:
            modelsInfo += modelsInfoString.format(
                d._class._name,
                d._class._color,
                d._model.get_model_information(),
                d._numOfSamples,
                d.get_range())
        return 'Real-Data simulation ({0} Models):\n{1}'.format(
            len(self._data), modelsInfo)

    def get_range(self):
        """ get_range returns the [xmin xmax ymin ymax] needed to display the
        data
        """
        # I don't understand how to do this whithout numpy.
        cBoundaries = np.asarray([c.get_range() for c in self._data])
        return [min(cBoundaries[:, 0]), max(cBoundaries[:, 1]),
                min(cBoundaries[:, 2]), max(cBoundaries[:, 3])]

    def draw_samples(self, axisId):
        """Draws 2D points on the axis

        :axisId: axis to draw on
        TODO: I guess this should be done by the samples itself
        """
        for d in self._data:
            axisId.scatter(d.get_samples_dim(0),
                           d.get_samples_dim(1),
                           c=d._class._color,
                           linewidths=0,
                           alpha=0.7)

    def draw_models(self, axisId):
        """Draws all the models as 2D probability isomap

        :axisId: axis to draw on

        """
        for d in self._data:
            d._model.draw(axisId)

    def get_all_data(self):
        return np.concatenate(
            list(d._samples for d in self._data),
            axis=0
        )


def main():

    import matplotlib.pyplot as plt

    fig, ax0 = plt.subplots(nrows=1)

    my_data = DataSimulation(n=10)
    print(my_data)
    print(my_data.get_all_data())
#    ax0.axis(my_data.get_range())
    ax0.axis([-3, 3, -3, 3])
    my_data.draw_samples(ax0)
    my_data.draw_models(ax0)

    plt.show()

if __name__ == '__main__':
    main()
