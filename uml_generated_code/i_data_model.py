from DataBaseCreator import *
from mplAxis import *

class IDataModel(object):

    """
     IDataModel is an abstract class to access all the data models both synthetic
     models used to generate data or those calculated from data

    :version:
    :author: sik
    """

    def __init__(self):
        """
         information in pytonic constructors:  http://tinyurl.com/3758j8u 
         http://tinyurl.com/424tbt7  http://tinyurl.com/lrownat

        @return IDataModel :
        @author sik
        """
        pass


    def __str__(self):
        """
         

        @return string :
        @author sik
        """
        pass


    def draw(self, axisId, color = '#000000'):
        """
         draw iso-value contours in order to illustrate the model distribution.
         
         pre: The axis limits should be appropiated to carry the ploting
         
         post: the distribution iso-value contours are displayed in axisId

        @param mplAxis axisId : 
        @param string color : the iso-value lines are painted acordingly to color
        @return  :
        @author sik
        """
        pass




