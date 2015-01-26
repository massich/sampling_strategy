"""random thoughts - sampling_strategy, support code"""

import collections
from data_class_instance import *
# from i_data_model import *


DBElement = collections.namedtuple('DBElement', 'dbeClass dbeModel dbeSamples')
"""Defininition of (class, model, samples) triplet as a nametuple

Note:
  In ordrder to see the expansion of the class code execute it with the
  `verbose=True` parameter.
"""


class DataBase(dict):
    """DataBase is a (class, model, samples) triplet diccionary that can be
    accessed using the class name of the data.
    
    Note:
      * the names of the data class **must** be unique, since they are used the dictionary key.

    Attributes:
      self (dictionary of DBElement): each element corresponds to a different
        group of data within the data base.

    :version: 0.0.1
    :author: sik
    """

    def __init__(self, dbelementList):
        """__init__ constructs a DataBase from the given parameters.(not fully
        implemnted, yet. Rightnow only accepted parameter is a DBElement list
        to be passed to the dict default __init__)

        TODO: 
          this method should be overloaded in order to take diferent
          instanciations

        :version: 0.0.1
        :author: sik
        """
        super(self.__class__, self).__init__(
            zip([e.dbeClass for e in dbelementList], dbelementList)
        )

    def __str__(self):
        """
        formated console print of the DataBase object

        .. todo:: [code] This is a copy-paste of the previous code structure
        :version: 0.0.1
        :author: sik
        """

        modelsInfoString="\t{0}_({1})_________________________\n\t\tmodel:: {2}\n \t\tsamples:: {3}\n \t\trange:: {4}\n"
        modelsInfo=""
        for d in self._data:
            modelsInfo+=modelsInfoString.format(
            d._class._name,d._class._color,d._model.get_model_information(),d._numOfSamples,d.get_range())

        return'Real-Data simulation ({0} Models):\n{1}'.format(
        len(self._data),modelsInfo)

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


def _test():
    """ test function to call when executing this file directly """
    xx = [DBElement(dbeClass='c1', dbeModel='model', dbeSamples=[0, 1]),
          DBElement(dbeClass='c2', dbeModel='model', dbeSamples=[0, 1]),
          DBElement(dbeClass='c3', dbeModel='model', dbeSamples=[0, 1]),
          DBElement(dbeClass='c4', dbeModel='model', dbeSamples=[0, 1]),
          DBElement(dbeClass='c5', dbeModel='model', dbeSamples=[0, 1]),
          DBElement(dbeClass='c6', dbeModel='model', dbeSamples=[0, 1])]

    myDBElementDictionary = dict(zip([x.dbeClass for x in xx], xx))
    dd = DataBase(xx)

    for k in myDBElementDictionary.iterkeys():
        assert dd[k] == myDBElementDictionary[k]

if __name__ == '__main__':
    _test()
