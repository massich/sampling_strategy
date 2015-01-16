from data_class_instance import *
from DataModel import *
from DataSimulation import *
from IDataModel import *
from DataBaseCreator import *
from RandomSampler import *
from IProjectionModel import *


class DataBase(object):
    """ DataBase stores the data as 3 dictionaries that can be indexed using
        the class name

    :version:
    :author: sik
    """

    def get_class_names(self):
        """
         

        @return string :
        @author sik
        """
        pass

    def draw_models(self, axisId):
        """
         

        @param mplAxis axisId : 
        @return  :
        @author sik
        """
        pass

    def draw_samples(self, axisId):
        """
         

        @param mplAxis axisId : 
        @return  :
        @author sik
        """
        pass



