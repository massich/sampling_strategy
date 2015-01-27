"""random thoughts - sampling_strategy, plotting support code"""

# from multipledispatch import dispatch
from data_base import *
from data_base_creator import *
from i_data_model import *


def plot_realData_model_isolines_in_dbSpace(ax, model, param_dict):
    """ A helper function to make a graph

    Args:
      ax (axes): The axes to draw to
      model (IDataModel): model to display as isolines
      data1 (array): The x data
      data2 (array): The y data
      param_dict (dict, optional): Dictionary of kwargs to pass to ax.plot

    Returns:
      list: list of artists added

    """
    pass


def scatterPlot_realData_nparray_in_dbSpace(ax, data, param_dict):
    """ A helper function to make a graph

    Args:
        ax (axes): The axes to draw to.
        data (np.array): Data points in [[x1, y1], [x2, y2] .. [xn, yn]] form.
        param_dict (dict, optional): Dictionary of kwargs to pass to ax.plot

    Returns:
        list of artists added

    :rtype: list
    :version: 0.0.1
    :author: sik
    """
    return ax.scatter(data[:, 0], data[:, 1], **param_dict)


def _test():
    """ test function to call when executing this file directly """

#    d = DataSimulation()
#    myDataBaseExample = d.generate_default2MVGM_testcase()
#
#    print myDataBaseExample

    import matplotlib.pyplot as plt
    import numpy as np
    # import matplotlib.mlab as mlab

    d = DataSimulation()
    myDataBaseExample = d.generate_default2MVGM_testcase()

    xx = myDataBaseExample['blue'].dbeSamples
    fig, (ax0, ax1) = plt.subplots(ncols=2)
    scatterPlot_realData_nparray_in_dbSpace(ax0, xx)
    plt.show()

if __name__ == '__main__':
    _test()
