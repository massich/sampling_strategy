"""random thoughts - sampling_strategy, support code"""

from i_data_model import *


class IDataSimulationModel (IDataModel):
    """IDataModel is an abstract class to force equal signature between
    all the data generative models.

    :version: 0.0.1
    :author: sik
    """
    __metaclass__ = ABCMeta

    @abstractmethod
    def __str__(self):
        pass

    @abstractmethod
    def generate_data(self, numSamples):
        """generate_data generate `numSamples` data points that follow the
        model described by `self`.
         
        Args:
          numSamples (int): Number of samples to generate

        Returns:
          nparray: data points in [[x1, y1, ..],[x2, y2, ..]] form

        :version: 0.0.1
        :author: sik
        """
        pass

    @abstractmethod
    def get_model_information(self):
        """get_model_information returns the model parameters dictionary.

        Returns:
          dict: Dictionary of {'parameter':value}

        :version: 0.0.1
        :author: sik
        """
        pass
