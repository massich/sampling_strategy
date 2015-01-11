
import numpy as np
from sklearn.decomposition import PCA

class FiterSingleFeat(object):

    """Docstring for FiterSingleFeat. """

    def __init__(self):
        """TODO: to be defined1. """


class FiterLDA(object):

    """Docstring for FiterLDA. """

    def __init__(self):
        """TODO: to be defined1. """


class FiterPCA(object):

    """Docstring for fiterPCL. """

    def __init__(self, data):
        """TODO: to be defined1. """
        num_dims_to_keep = 2
        self._transformation = PCA(n_components = num_dims_to_keep).fit(data)


    def project_data(self, data):
        return self._transformation.transform(data)

    def display_base(self, axisId):
        """Plots one dimensiona line where data is projected

        :axisId: axis to plot on

        """
        base = np.array([[-1,1,0,0], [0,0,-1,1]]).T
        base_projected = self._transformation.transform(6*base)

        print('projected base')
        print(base_projected)

        x,y = base_projected.T
        axisId.plot(x[0:2], y[0:2], 'k-', linewidth=2)
        axisId.plot(x[2:4], y[2:4], 'k-', linewidth=2)


import matplotlib.pyplot as plt

def main():
    """
        Tests
    """

    data = np.array([[1,2,3,4,5], [1,2,3,4,5]]).T
    print(data.shape)
    print(data)

    my_fiter = FiterPCA(data)
    data_projected = my_fiter.project_data(data)

    print('projected data:')
    print(data_projected)


    fig = plt.figure()
    axis = fig.add_subplot(111)
    my_fiter.display_base(axis)
    fig.show()

if __name__ == '__main__':
    main()


