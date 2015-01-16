from object import *
from IDataModel import *
from DataSimulation import *

class IDataSimulationModel (object, IDataModel):

    """
     

    :version:
    :author: sik
    """

    def __init__(self, dataClass):
        """
          information in pytonic constructors:  http://tinyurl.com/3758j8u 
         http://tinyurl.com/424tbt7  http://tinyurl.com/lrownat

        @param string dataClass : 
        @return IDataSimulationModel :
        @author sik
        """
        self._dataClass=dataClass
        


    def __str__(self):
        """
         

        @return string :
        @author sik
        """
        pass
        


    def generate_data(self, numSamples):
        """
         

        @param int numSamples : 
        @return nparray :
        @author sik
        """
        pass
        


    def get_model_information(self):
        """
         This method returns the creation parameters of the object

        @return string :
        @author sik
        """
        pass
        




