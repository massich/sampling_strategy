"""random thoughts - sampling_strategy, DataBase projection support code.

   This module projects DataBase objects into a different space where to \
   perform the sampling
"""
import random
from abc import ABCMeta, abstractmethod
#raise NotImplementedError


class ProjectionModelFactory(object):
    """IProjectionModel Factory"""

    @staticmethod
    def createIProjectionModel(*argv, **kwargv):
        # First parameter is supposed to be the class name to instanciate
        try:
            if issubclass(eval(argv[0]), IProjectionModel):
                # return the subclass factoryMethod
                return eval(argv[0])._create(*argv[1:], **kwargv)
            else:
                raise TypeError
        except (TypeError, NameError):
            validTypeNames = [s.__name__ 
                              for s in IProjectionModel.__subclasses__()]
            raise TypeError("""'{0}' is an invalid IProjectionModel subclass. \
                            Valid type names are:\n\t{1:s}""".format(id,
                            '\n\t'.join(validTypeNames)))


class IProjectionModel(object):
    """IProjectionModel is an abstract class to force equal signature between \
    all the projection model implementations. A projection model takes a \
    DataBase (or DataSet) and determines a new projection of the data.
     
     .. The instances of this class should overwrite its generative methods \ 
     .. in order to output projected data

    :version: 0.0.1
    :author: sik
    """
    # information about abstract classes
    #  http://tinyurl.com/l3awj4d
    #  http://tinyurl.com/k8acb9x
    __metaclass__ = ABCMeta

    @classmethod
    def _create(cls, *argv, **kwargv):
        """_create is method called from `ProjectionModelFactory` to trigger \
           the desired projection model creation.

            Args:
                cls : is the target projection model's class. \
                    It must be a subclass of IProjectionModel.
                *argv (tuple, optional): unnamed arguments to supply to the \
                                         instance creator.
                **kwargv (dict, optional): named arguments to supply to the \
                                           instance creator.
            Returns:
                   An initialized object of class **cls**

            :version: 0.0.1
            :author: sik

            .. todo:: [doc] manage to link ProjectionModelFactory code from \
                      the doc string
        """
        myObj = object.__new__(cls)
        myObj.__init__(*argv, **kwargv)
        return myObj

    # Here follow the methods required for an IProjectionModel implantation
    @abstractmethod
    def __init__(self, *argv, **kwargv):
        pass

    @abstractmethod
    def display_base(self, ax):
        """ This method draws the projection base into the **ax** axis handle

            Args:
                ax (mpl::axis): axis to plot on
        
            Returns:
                A list containing all the artists added into **ax**

        :version: 0.0.1
        :author: sik
        """
        pass

class Circle(IProjectionModel):
    def __init__(self, color='blue', *argv, **kwargv):
        print "{0:<27s} {1}".format("Circle::__init__::", locals())
        self._color = color

    def draw(self):
        print("Circle.draw, in color {}".format(self._color))

    def erase(self):
        print("Circle.erase")

    def display_base(self, ax):
        pass

class Square(IProjectionModel):
    def __init__(self, color='red', *argv, **kwargv):
        print "{0:<27s} {1}".format("Square::__init__::", locals())
        self._color = color

    def draw(self):
        print("Square.draw, in color {}".format(self._color))

    def erase(self):
        print("Square.erase")

    def display_base(self, ax):
        pass


def shapeNameGen(n):
    # http://sahandsaba.com/python-iterators-generators.html
    # g = (random.random() < 0.4 for __ in itertools.count())
    types = IProjectionModel.__subclasses__()
    for i in range(n):
        yield random.choice(types).__name__


def _test():

    assert issubclass(Circle, IProjectionModel)
    assert issubclass(Square, IProjectionModel)

    # Create sublcass instances directly
    for s in [Circle(), Square()]:
        s.draw()
        s.erase()

    print "Start testing the factory"
    shapeObjects = [
        ProjectionModelFactory.createIProjectionModel(next(shapeNameGen(1)), 'purple'),
        ProjectionModelFactory.createIProjectionModel(next(shapeNameGen(1)), color='green'),
        ProjectionModelFactory.createIProjectionModel(next(shapeNameGen(1)), stupidParam='stupid')
        ]

    # shapeObjects = [ProjectionModelFactory.createIProjectionModel(sType)
    #                 for sType in shapeNameGen(N)]

    # print shapeObjects
    for idx, s in enumerate(shapeObjects):
        print "IProjectionModel ({0:d})_________".format(idx)
        s.draw()
        s.erase()

if __name__ == '__main__':
    _test()
