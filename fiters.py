
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
        num_dims_to_keep = 1
        self._transformation = PCA(n_components = num_dims_to_keep).fit(data)


    def project_data(self, data):
        return self._transformation.transform(data)



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

if __name__ == '__main__':
    main()


