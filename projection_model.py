

import numpy as np
from fiters import *

class ProjectionModel(object):

    """This class creates a projection function onto a one dimensional space"""

    def __init__(self, projection_type, data):
        """TODO: to be defined1.

        :projection_type: 'SingleFeat' -> Not implemented
                          'LDA' -> I don't know what this is
                          'PCA' -> Projects onto the first principal axis
        :data: Data to generate the model

        """

        if projection_type == 'SingleFeat':
            print('Not implemented')

        elif projection_type == 'LDA':
            print('Not implemented')

        elif projection_type == 'PCA':
            self._fiter = FiterPCA(data)

        else:
            print('are you fucikng kiding me?!')


    def project_data(self, data):
        """ Project this data with the known projection model

        :data: set of point
        :returns: projected points into an unidimencional space

        """
        return self._fiter.project_data(data)


def main():

    """
        Tests
    """

    data = np.array([[1,2,3,4,5], [1,2,3,4,5]]).T
    my_projection_model = ProjectionModel('PCA',data)

    data_projected = my_projection_model.project_data(data)
    print(data_projected)

if __name__ == '__main__':
    main()

