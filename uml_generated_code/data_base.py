from data_class_instance import *
from DataModel import *
from DataSimulation import *
from IDataModel import *
from DataBaseCreator import *
from RandomSampler import *
from IProjectionModel import *


class DataBase(object):
    """DataBase is a (class, model, samples) triplet diccionary that can be
    accessed using the class name of the data.
    
    Note:
      * the names of the data class **must** be unique, since they are used the
      dictionary key.

    Attributes:
      self (dictionary of (DataClassInstance, IDataModel, npArray)): each
        element corresponds to a different group of data within the data base.

    :version: 0.0.1
    :author: sik
    """
# >>> t = [(4, 180, 21), (5, 90, 10), (3, 270, 8), (4, 0, 7)]
# >>> dict([ (k, [v, w]) for k, v, w in t ])
# {3: [270, 8], 4: [0, 7], 5: [90, 10]}
#

    def __new__(cls):
        return dict()

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



