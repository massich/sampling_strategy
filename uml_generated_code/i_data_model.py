"""random thoughts - sampling_strategy, support code"""

from abc import ABCMeta, abstractmethod
# from data_base_creator import *
# from mplAxis import *


class IDataModel(object):
    """IDataModel is an abstract class to force equal signature between
    generative and fitted data models present in DataBase class

    :version: 0.0.1
    :author: sik
    """
    # information about abstract classes
    #  http://tinyurl.com/l3awj4d
    #  http://tinyurl.com/k8acb9x
    __metaclass__ = ABCMeta

    def __init__(self):
        """ IDataModel.__init__ 
        .. todo::
           [design] should be an abstractmethod to force implementation? or
           should I remove the whole thing?

        :version: 0.0.1
        :author: sik
        """
        # information in pytonic constructors:
        #  http://tinyurl.com/3758j8u
        #  http://tinyurl.com/424tbt7
        #  http://tinyurl.com/lrownat
        pass

    @abstractmethod
    def __str__(self):
        pass

    @abstractmethod
    def draw_2Disoc(self, ax, dataClass=None):
        """draw_2Disoc draws iso-value contours in order to illustrate the
        model distribution.

        Note:
            * pre-condition: The axis limits should be appropiated to carry the ploting
            * post-condition: the distribution iso-value contours are displayed in axisId

        Args:
            ax (axes): The axes to draw to
            dataClass (DataClassInstance): The data class associated to the model

        Returns:
            A list of artists added to **ax**

        .. todo::
           [design] who should belong to the drawing signature?
        Note:
            I'm not sure if this function should belong to:

            * the object, since the model knows all the information about itself
            * :mod:`sampler_simulation_plot_helper`, since is the collection of
              plotting functions


        :version: 0.0.1
        :author: sik
        """
        # TODO(sik) test
        pass
