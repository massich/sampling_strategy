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


class PMIdentity(IProjectionModel):
    """PMIdentity does no projection of the data, so that the projected space \
       is exaclty the same as the original one.
    """

    def __init__(self, *argv, **kwargs):
        pass

    def display_base(sefl, ax, param_dict={}):
        """ Display in **ax** the projection base in the original DataBase space.

        Args:
          ax (axes): The axes to draw to
          param_dict (dict, optional): Dictionary of kwargs to pass to ax.plot

        Returns: list of artists added to **ax**

        :rtype: list
        :version: 0.0.1
        :author: sik
        """
        aLimit = ax.axis()
        out1 = ax.plot(aLimit[:2], [0, 0], param_dict)
        out2 = ax.plot([0, 0], aLimit[-2:], param_dict)
        return out1, out2


class PModelSingleFeat(IProjectionModel):
    """PModelSingleFeat takes a single feature of the data
    
    TODO: right now only handles 2D data and everything is hardcoded
    """

    def __init__(self, featureIndx=0, *argv, **kwargs):
        if featureIndx > 1:
            raise 'featureIndx should be 0 or 1'
        self._featureIndx = featureIndx

    def display_base(self, axisId, lineW=2):
        aLimit = axisId.axis()
        if self._featureIndx == 0:
            yCoord = ((aLimit[3]-aLimit[2]) / 2) + aLimit[2]
            axisId.plot(aLimit[:1],
                        [yCoord]*2,
                        'k-', linewidth=lineW)
        else:
            xCoord = ((aLimit[3]-aLimit[2]) / 2) + aLimit[2]
            axisId.plot([xCoord]*2,
                        aLimit[:1],
                        'k-', linewidth=lineW)

    def project_data(self, dataPoints):
        return dataPoints[:, self._featureIndx]


class PModelPCA(object):
    """Docstring for fiterPCL. """

    def __init__(self, data, *argv, **kwargs):
        """TODO: to be defined1. """
        num_dims_to_keep = 2
        self._transformation = PCA(n_components=num_dims_to_keep).fit(data)

    def project_data(self, data):
        return self._transformation.transform(data)

    def display_base(self, axisId, lineW=2):
        base = np.array([[-1, 1, 0, 0], [0, 0, -1, 1]]).T
        base_projected = self._transformation.transform(6*base)

        x, y = base_projected.T
        axisId.plot(x[0:2], y[0:2], 'k-', linewidth=lineW)
        axisId.plot(x[2:4], y[2:4], 'k-', linewidth=lineW)


class PModelLDA(IProjectionModel):
    """Docstring for PModelLDA. """

    def __init__(self):
        raise NotImplemented

    def display_base(self, axisId):
        raise NotImplemented

    def project_data(self, dataPoints):
        raise NotImplemented


def shapeNameGen(n):
    # http://sahandsaba.com/python-iterators-generators.html
    # g = (random.random() < 0.4 for __ in itertools.count())
    types = IProjectionModel.__subclasses__()
    for i in range(n):
        yield random.choice(types).__name__


def _test():
#    from data_base import DataBase
    from data_base_creator import DataSimulation
    import sampler_simulation_plot_helper as spl
    import matplotlib.pyplot as plt

    myDb = DataSimulation().generate_default2MVGM_testcase()
#    myDataBaseExample = d.generate_default2MVGM_testcase()

    myIdentityProj = ProjectionModelFactory.createIProjectionModel('PMIdentity', myDb)

    print myDb
    fig, ax = plt.subplots()
    ax.axis([-3, 3, -3, 3])
    spl.plot_DataBase_in_dbSpace(ax, myDb)
    myIdentityProj.display_base(ax,'k')
    plt.show()

if __name__ == '__main__':
    _test()
