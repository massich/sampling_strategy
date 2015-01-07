from abc import ABCMeta, abstractmethod, abstractproperty


class IDataSimulationModel(object):
    """ This is the real data D abstract class for the case of simulation.
        The simulated data can be drawn from different models which are
        intended to inherit from this this class.
        Each model should :
          -understand its own building parameters or through an error.
          -implement the abstractmethods

        Note: since it is an abstract class it starts with I as IClassName to
              denote ClassName-Interface
    """
    # information about abstract classes
    #  http://tinyurl.com/l3awj4d
    __metaclass__ = ABCMeta
    __slots__ = ["_dataClass"]

    @abstractmethod
    def __init__(self, _dataClass='black', *args, **kwargs):
        # information in pytonic constructors:
        #  http://tinyurl.com/3758j8u
        #  http://tinyurl.com/424tbt7
        #  http://tinyurl.com/lrownat
        self._dataClass = _dataClass
        return self

    def __str__(self):
        pass

    def generate_data(self, numSamples):
        pass

    def draw_model(self, axisId):
        pass

    @abstractproperty
    def data_model_information(self):
        """This method returns the creation parameters of the object"""
        pass

    @classmethod
    @property
    def _dataClass(self):
        """The colour is considered the label of the data"""
        return self._dataClass
#
#    @_dataClass.setter
#    def _dataClass(self, value):
#        self._dataClass = value


class MultiVariatedGaussianModel(IDataSimulationModel):
    """ This is the real data D class for the case of a single 2D Gaussian
    multivariate simulation process.

    Attributes:
        modelMuX     -- x mean value of the model     (modelMuX     = 0)
        modelMuY     -- y mean value of the model     (modelMuY     = 0)
        modelSigmaX  -- variance of the model along x (modelSigmaX  = 1)
        modelSigmaY  -- variance of the model along y (modelSigmaY  = 1)
        modelSigmaXY -- x,y covariance of the model   (modelSigmaXY = 0)
    """
    __slots__ = ["modelSigmaXY", "modelSigmaX", "modelSigmaY", "modelMuY",
                 "modelMuX"]

    def __init__(self, *args, **kwargs):
        """ The following parameters can be specified in order to define define
        a multivariate 2D Gaussian model. Otherwise, defaults my apply. Any
        other argument would create an exception.

        Example:
            MultiVariatedGaussianModel( modelMuX     = 0,
                                        modelMuY     = 0,
                                        modelSigmaX  = 1,
                                        modelSigmaY  = 1,
                                        modelSigmaXY = 0,
                                        [dataClass = None]
                                        )
        TODO: dataClass can't be passed anonymously
    """
        # args -- tuple of anonymous arguments
        # kwargs -- dictionary of named arguments
        extraNamedArguments = kwargs.viewkeys() - {'modelSigmaXY',
                            'modelSigmaX', 'modelSigmaY', 'modelMuY',
                            'modelMuX', 'cataClass'}
        if extraNamedArguments:
            raise Exception("Invalid args: " + ', '.join(extraNamedArguments))
        elif len(args) > 6:
            raise Exception("Too many anonymous arguments")
        else:
            defaultValues = [0, 0, 1, 1, 0]
            args = list(args)
            args.extend(defaultValues[len(args):])
            self.modelMuX     = kwargs.pop('modelMuX',     args[0])
            self.modelMuY     = kwargs.pop('modelMuY',     args[1])
            self.modelSigmaX  = kwargs.pop('modelSigmaX',  args[2])
            self.modelSigmaY  = kwargs.pop('modelSigmaY',  args[3])
            self.modelSigmaXY = kwargs.pop('modelSigmaXY', args[4])

    def data_model_information(self):
        """Returns the information of the multi-variate 2D Gaussian Model in a
        tuple as follows:
        (className, label/colour, xMean, yMean, xSTD, ySTD, xySTD)
        """
        return (
            self.__class__.__name__,
            self._dataClass,
            self.modelMuX,
            self.modelMuY,
            self.modelSigmaX,
            self.modelSigmaY,
            self.modelSigmaXY,
        )

    def __str__(self):
        return 'Real-Data simulation (2D multi-variate Model):\n' \
               '\tmean x:{0}, y:{1}\n' \
               '\tSTD  x:{2}, y:{3}, xy:{4}' \
               '\n'.format(self.modelMuX, self.modelMuY, self.modelSigmaX,
                           self.modelSigmaY, self.modelSigmaXY)

    def generate_data(sef, numSamples):
        pass

    def draw_model(self, axisId):
        pass
