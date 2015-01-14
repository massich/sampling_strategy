import numpy as np
from sklearn.decomposition import PCA
from abc import ABCMeta, abstractmethod


class IProjectionModel(object):
    """ ProjectionModel is an abstract class in order to force that all
    projection Models share the same signature

        Note: since it is an abstract class it starts with I as IClassName to
              denote ClassName-Interface
    """
    __metaclass__ = ABCMeta

    @abstractmethod
    def __init__(self, *args, **kwargs):
        pass

    @abstractmethod
    def display_base(self, axisId):
        """This method draws the projection base into the axisId axis
        handle
        
        :axisId: axis to plot on

        """
        pass

    @abstractmethod
    def project_data(self, dataPoints):
        """project_data returns the dataPoints in the new coordinate
        system.

        :dataPoints: np.array in the form [[x1, y1, ..],[x2, y2, ..]]
        :returns: np.array in the form [[x1, y1, ..],[x2, y2, ..]]

        """
        pass


class ProjectionModelSingleFeat(object):
    """ProjectionModelSingleFeat takes a single feature of the data
    
    TODO: right now only handles 2D data and everything is hardcoded
    """

    def __init__(self, featureIndx=0):
        if featureIndx > 1:
            raise 'featureIndx should be 0 or 1'
        self._featureIndx = featureIndx

    def display_base(self, axisId, lineW=2):
        aLimit = axisId.axis()
        if self._featureIndx == 0:
            yCoord = ((aLimit[3]-aLimit[2]) / 2) + aLimit[2]
            axisId.plot(aLimit[:1],
                        [yCoord]*2,
                        'k-', linewidth=lineW)
        else:
            xCoord = ((aLimit[3]-aLimit[2]) / 2) + aLimit[2]
            axisId.plot([xCoord]*2,
                        aLimit[:1],
                        'k-', linewidth=lineW)

    def project_data(self, dataPoints):
        return dataPoints[:, self._featureIndx]


class ProjectionModelLDA(object):

    """Docstring for ProjectionModelLDA. """

    def __init__(self):
        """TODO: to be defined1. """

    def display_base(self, axisId):
        pass

    def project_data(self, dataPoints):
        pass


class ProjectionModelPCA(object):

    """Docstring for fiterPCL. """

    def __init__(self, data):
        """TODO: to be defined1. """
        num_dims_to_keep = 2
        self._transformation = PCA(n_components=num_dims_to_keep).fit(data)

    def project_data(self, data):
        return self._transformation.transform(data)

    def display_base(self, axisId, lineW=2):
        base = np.array([[-1, 1, 0, 0], [0, 0, -1, 1]]).T
        base_projected = self._transformation.transform(6*base)

        x, y = base_projected.T
        axisId.plot(x[0:2], y[0:2], 'k-', linewidth=lineW)
        axisId.plot(x[2:4], y[2:4], 'k-', linewidth=lineW)


def main():
    """
        Tests
    """

    import matplotlib.pyplot as plt

    data = np.array([[1, 2, 3, 4, 5], [1, 2, 3, 4, 5]]).T
    print(data.shape)
    print(data)

    my_projMod = ProjectionModelPCA(data)
    data_projected = my_projMod.project_data(data)

    print('projected data:')
    print(data_projected)

    fig = plt.figure()
    axis = fig.add_subplot(111)
    my_projMod.display_base(axis)
    fig.show()

if __name__ == '__main__':
    main()
