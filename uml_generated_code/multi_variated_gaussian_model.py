"""random thoughts - sampling_strategy, support code"""

from i_data_simulation_model import *
import numpy as np
import matplotlib.mlab as mlab


class MultiVariatedGaussianModel (IDataSimulationModel):
    """MultiVariatedGaussianModel implements an IDataSimulationModel as a multi-variate gaussian in order to simulate DataBase samples that behaves as such.

    Attributes:
        _muX (float): x mean value.
        _muY (float): y mean value.
        _sigmaX  (float): variance along x.
        _sigmaY  (float): variance along y.
        _sigmaXY (float): x,y covariance.

    :version:
    :author: sik
    """
    __slots__ = ["_muX", "_muY", "_sigmaX", "_sigmaY", "_sigmaXY"]

    def __init__(self, *args, **kwargs):
        """ The following parameters can be specified in order to define define
        a multivariate 2D Gaussian model. Otherwise, defaults my apply. Any
        other argument would create an exception.

        Attributes:
            muX (float, optional): x mean value. Defaults to 0
            muY (float, optional): y mean value. Defaults to 0
            sigmaX  (float, optional): variance along x. Defaults to 1
            sigmaY  (float, optional): variance along y. Defaults to 1
            sigmaXY (float, optional): x,y covariance. Defaults to 0.

        Example:
            MultiVariatedGaussianModel(muX=0, muY=0,
                                       sigmaX=1, sigmaY=1, sigmaXY=0)

        TODO: this example should be done properly (create model, get samples,
        check that samples follow the expected)
    """
        # args -- tuple of anonymous arguments
        # kwargs -- dictionary of named arguments
        possibleArguments = {'muX', 'muY', 'sigmaX', 'sigmaY', 'sigmaXY'}
        extraNamedArguments = kwargs.viewkeys() - possibleArguments
        if extraNamedArguments:
            raise Exception("Invalid args: " + ', '.join(extraNamedArguments))
        elif len(args) > 6:
            raise Exception("Too many anonymous arguments")
        else:
            defaultValues = [0, 0, 1, 1, 0]
            args = list(args)
            args.extend(defaultValues[len(args):])
            self._muX     = kwargs.pop('muX',     args[0])
            self._muY     = kwargs.pop('muY',     args[1])
            self._sigmaX  = kwargs.pop('sigmaX',  args[2])
            self._sigmaY  = kwargs.pop('sigmaY',  args[3])
            self._sigmaXY = kwargs.pop('sigmaXY', args[4])

    def get_model_information(self):
        """Returns the information of the multi-variate 2D Gaussian Model in as
        a dictionary

        Returns:
          dict: {'xMean':_muX, 'yMean':_muY,
                 'xSTD':_sigmaX, 'ySTD':_sigmaY, 'xySTD':_sigmaXY,}

        :version: 0.0.1
        :author: sik
        """
        return dict(zip(['xMean', 'yMean', 'xSTD', 'ySTD', 'xySTD'],
                        [self._muX, self._muY, self._sigmaX, self._sigmaY,
                         self._sigmaXY]))

    def __str__(self):
        return 'Real-Data simulation (2D multi-variate Model):\n' \
               '\tmean x:{0}, y:{1}\n' \
               '\tSTD  x:{2}, y:{3}, xy:{4}' \
               '\n'.format(self._muX, self._muY, self._sigmaX, self._sigmaY,
                           self._sigmaXY)

    def generate_data(self, numSamples):
        """TODO: import parent documentation, while changing version and author

        Returns:
          nparray:

        :version: 0.0.1
        :author: sik
        """
        return np.random.multivariate_normal(
            [self._muX, self._muY],
            [[self._sigmaX, self._sigmaXY], [self._sigmaXY, self._sigmaY]],
            numSamples)

    def draw_2Disoc(self, axisId, dataClass=None):
        # collect needed parameters: plot color, range, etc.
        try:
            modelColor = dataClass._color
        except Exception:
            modelColor = '#000000'

        aLimits = axisId.axis()
        delta = (aLimits[1] - aLimits[0])/100
        X, Y = np.meshgrid(np.arange(aLimits[0], aLimits[1], delta),
                           np.arange(aLimits[0], aLimits[1], delta))
        Z = mlab.bivariate_normal(X, Y, self._sigmaX, self._sigmaY,
                                  self._muX, self._muY, self._sigmaXY)

#        displayParameters = dict([('linewidths', np.arange(.5, 2, .25)),
#                                  ('colors', modelColor)])
        axisId.contour(X, Y, Z/Z.max(),     # data
                       4,                   # 4 isolines
                       linewidths=np.arange(.5, 2, .25),
                       colors=modelColor)
#                       displayParameters)   # plotting parameters


def _test():
    """ test function to call when executing this file directly """
    import matplotlib.pyplot as plt
    # import numpy as np
    # import matplotlib.mlab as mlab

    m0 = MultiVariatedGaussianModel()
    print m0
    print m0.get_model_information()

    ss = m0.generate_data(1000)
    fig, (ax0, ax1) = plt.subplots(ncols=2)
    ax0.scatter(ss[:, 0], ss[:, 1])
#    m0.draw_2Disoc(ax0)

    m1 = MultiVariatedGaussianModel(muX=1, muY=3, sigmaXY=10)
    ss = m1.generate_data(20)
    ax1.scatter(ss[:, 0], ss[:, 1])
#    m1.draw_2Disoc(ax1)
    m1 = MultiVariatedGaussianModel(3, 1, sigmaXY=10)
    ss = m1.generate_data(20)
    ax1.scatter(ss[:, 0], ss[:, 1])
#    m1.draw_2Disoc(ax1)
    fig.show()

if __name__ == '__main__':
    _test()
