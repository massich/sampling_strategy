"""random thoughts - sampling_strategy, support code"""

import collections
# from data_class_instance import *
# from i_data_model import *

DataClassInstance = collections.namedtuple('DataClassInstance', 'name color')
"""DataClassInstance defininition as a namedtuple to store data identifying
   info.

This information describing the data in hand is further used in plots or to
retrieve the data based on the data class attributes.

Attributes:
    name (str): Human readable string to identify the data in hand.
    color (str): color code to identify the data when plotting. The color
        should be specified in hexacode as '#00ff00'.

Note:
  In ordrder to see the expansion of the class code execute it with the
  `verbose=True` parameter.

:version: 0.0.1
:author: sik
"""

DBElement = collections.namedtuple('DBElement', 'dbeClass dbeModel dbeSamples')
"""DBElement defininition as a namedtuple to store all the information
   regarding a particular data class

Attributes:
    dbeClass (DataClassInstance): data base element class indentification \
                                  information.
    dbeModel (IDataModel): data base element model
    dbeSamples (nparray): data base element samples

Note:
  In ordrder to see the expansion of the class code execute it with the
  `verbose=True` parameter.

:version: 0.0.1
:author: sik
"""


class DataBase(dict):
    """DataBase is a (class, model, samples) triplet diccionary that can be
    accessed using the class name of the data.

    Note:
      * the names of the data class **must** be unique, since they are used \
        the dictionary key.

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

        .. todo:: [code] this method should be overloaded in order to take \
                  diferent instanciations

        :version: 0.0.1
        :author: sik
        """
        super(self.__class__, self).__init__(
            zip([e.dbeClass.name() for e in dbelementList],
            dbelementList))

    def __str__(self):
        """
        formated console print of the DataBase object

        .. todo:: [code][to Impl.] This is a copy-paste of the previous code\
                                   structure
        :version: 0.0.1
        :author: sik
        """
        return self.__class__
        # "{1}-class DataBase\n".format(len(self))
        # elementInfo = "\t<{1}> class: {2}, {3}\n \
        #                \t<{1}> model: {4}\n \
        #                \t<{1}> shape: {5}\n\n"
        # return "{1}-class DataBase\n{2}".format(len(self),
        #     [elementInfo.format(dKey, dElement.dbeClass.get_name(),
        #                         dElement.dbeClass.get_color(),
        #                         dElement.dbeModel.get_model_information(),
        #                         dElement.dbeSamples.shape())
        #         for dKey, dElement in self.iteritems()])
        
#        modelsInfoString="\t{0}_({1})_________________________\n\t\tmodel:: {2}\n \t\tsamples:: {3}\n \t\trange:: {4}\n"
#        modelsInfo=""
#        for d in self._data:
#            modelsInfo+=modelsInfoString.format(
#            d._class._name,d._class._color,d._model.get_model_information(),d._numOfSamples,d.get_range())
#
#        return'Real-Data simulation ({0} Models):\n{1}'.format(
#        len(self._data),modelsInfo)

    def get_range(self):
        """
        get_range returns the [xmin xmax ymin ymax] needed to display the data

        Return:
            Array of (min, max) tuples of all the data dimensions
        :rtype: array of tuples
        :version: 0.0.1
        :author: sik

        .. # I don't understand how to do this whithout numpy.
        .. todo:: [code][to Impl.] This is a copy-paste of the previous code structure
        """
        # cBoundaries=np.asarray([c.get_range()for c in self._data])
        # return[min(cBoundaries[:,0]),max(cBoundaries[:,1]),
        # min(cBoundaries[:,2]),max(cBoundaries[:,3])]

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

    xx = [DBElement(DataClassInstance('c1','#ffffff'), dbeModel='model', dbeSamples=[0, 1]),
          DBElement(DataClassInstance('c2','#ffffff'), dbeModel='model', dbeSamples=[0, 1]),
          DBElement(DataClassInstance('c3','#ffffff'), dbeModel='model', dbeSamples=[0, 1]),
          DBElement(DataClassInstance('c4','#ffffff'), dbeModel='model', dbeSamples=[0, 1]),
          DBElement(DataClassInstance('c5','#ffffff'), dbeModel='model', dbeSamples=[0, 1]),
          DBElement(DataClassInstance('c6','#ffffff'), dbeModel='model', dbeSamples=[0, 1])]

#    myDBElementDictionary = dict(zip([x.dbeClass for x in xx], xx))
    dd = DataBase(xx)
    print dd

#    for k in myDBElementDictionary.iterkeys():
#        assert dd[k] == myDBElementDictionary[k]

if __name__ == '__main__':
    _test()
