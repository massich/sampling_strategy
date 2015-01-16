from object import *
from DataSet import *

class RandomSampler (object):

    """
     RandomSamplier :
             1 - projects the data into lower dimension space based on a
                 projection model.
             2 - based on a sampling model generates a collection of randomly
                 selected subsets.
     

    :version:
    :author: sik
    """

    def __init__(self, data):
        """
         RandomSampler initalization.
                 :data: TODO
                 :returns: TODO
         

        @param string data : 
        @return string :
        @author sik
        """
        self._projectionModel=ProjectionModelPCA(data)
        


    def display_projection_base(self, axisId, lineW):
        """
         display_projection_base draws the projection axis into axisId handle
                 :axisId: axis to plot on
         

        @param string axisId : 
        @param string lineW : 
        @return string :
        @author sik
        """
        self._projectionModel.display_base(axisId,lineW)
        




