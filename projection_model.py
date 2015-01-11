

import numpy as np

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

        elif projection_type == 'PCL':
            self._fiter = fiterPCL()

        else:
            print('are you fucikng kiding me?!')



        self._projection_matrix = self._fiter.get_projection_matrix(data)


    def project_data(self, data):
        """ Project this data with the known projection model

        :data: set of point
        :returns: projected points into an unidimencional space

        """

        return self._projection_matrix * data.T()

