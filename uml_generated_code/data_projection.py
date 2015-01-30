"""random thoughts - sampling_strategy, DataBase projection support code.

   This module projects DataBase objects into a different space where to \
   perform the sampling
"""
from abc import ABCMeta, abstractmethod
from sklearn.decomposition import PCA
import numpy as np


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
                            Valid type names are:\n\t{1:s}""".format(argv[0],
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
        """ __init__ is the compulsory constructor method to be implemented \
            by subclasses, since it is called from \
            `ProjectionModelFactory._create()`. 

            Note: 
                If the projection model needs some fitting, here is where \
                it should take place.
        """
        pass

    @abstractmethod
    def display_base(self, ax, param_dict={}):
        """ Display, into the **ax** handle, the projection model base in the
            original DataBase space reference frame.

            Args:
              ax (mpl:axis): The axis to plot on
              param_dict (dict, optional): Dictionary of kwargs to pass to ax.plot

            Returns: list of artists added to **ax**

        :rtype: list
        :version: 0.0.1
        :author: sik
        """
        pass


class PMIdentity(IProjectionModel):
    """PMIdentity does no projection of the data, so that the projected space \
       is exaclty the same as the original one.
    """

    def __init__(self, *argv, **kwargs):
        pass

    def display_base(sefl, ax, param_dict={}):
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

    def display_base(self, ax, param_dict={}):
        aLimit = ax.axis()
        get_half = lambda minv, maxv: ((maxv-minv)/2)+minv

        if self._featureIndx == 0:
            yCenter = get_half(aLimit[2], aLimit[3])
            return ax.plot(aLimit[:2], [yCenter]*2, param_dict)
        else:
            xCenter = get_half(aLimit[0], aLimit[1])
            return ax.plot([xCenter]*2, aLimit[-2:], param_dict)

    def project_data(self, dataPoints):
        return dataPoints[:, self._featureIndx]


class PModelPCA(IProjectionModel):
    """ Use Principal Component Analysis (PCA) as projection model."""

    def __init__(self, db, *argv, **kwargs):
        numDims2Keep = 2
        data2fit = np.vstack([d.dbeSamples for d in db.itervalues()])
        self._transformation = PCA(n_components=numDims2Keep).fit(data2fit)

    def project_data(self, data):
        return self._transformation.transform(data)

    def display_base(self, axisId, param_dict={}):
        base = np.array([[-1, 1, 0, 0], [0, 0, -1, 1]]).T
        base_projected = self._transformation.transform(6*base)

        x, y = base_projected.T
        axisId.plot(x[0:2], y[0:2], param_dict)
        axisId.plot(x[2:4], y[2:4], param_dict)


class PModelLDA(IProjectionModel):
    """Docstring for PModelLDA. """

    def __init__(self):
        raise NotImplemented

    def display_base(self, axisId):
        raise NotImplemented

    def project_data(self, dataPoints):
        raise NotImplemented


def _test():
    import random
    from data_base_creator import DataSimulation
    import sampler_simulation_plot_helper as spl
    import matplotlib.pyplot as plt

    def shapeNameGen(n):
        # http://sahandsaba.com/python-iterators-generators.html
        # g = (random.random() < 0.4 for __ in itertools.count())
        types = IProjectionModel.__subclasses__()
        for i in range(n):
            yield random.choice(types).__name__

    myDb = DataSimulation().generate_default2MVGM_testcase()
#    myDataBaseExample = d.generate_default2MVGM_testcase()

    myIdentityProj = ProjectionModelFactory.createIProjectionModel(
                     'PModelPCA', myDb)
    # print myDb
    fig, ax = plt.subplots()
    ax.axis([-3, 3, -3, 3])
    spl.plot_DataBase_in_dbSpace(ax, myDb)
    myIdentityProj.display_base(ax, 'k')
    plt.show()

if __name__ == '__main__':
    _test()
