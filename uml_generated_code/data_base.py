"""random thoughts - sampling_strategy, support code"""
import collections
from data_class_instance import *
from i_data_model import *


DBElement = collections.namedtuple('DBElement', 'class model samples')
"""Defininition of (class, model, samples) triplet as a nametuple

Note:
  In ordrder to see the expansion of the class code execute it with the
  `verbose=True` parameter.
"""


class DataBase(object):
    """DataBase is a (class, model, samples) triplet diccionary that can be
    accessed using the class name of the data.
    
    Note:
      * the names of the data class **must** be unique, since they are used the
      dictionary key.

    Attributes:
      self (dictionary of DBElement): each element corresponds to a different
        group of data within the data base.

    :version: 0.0.1
    :author: sik
    """

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



