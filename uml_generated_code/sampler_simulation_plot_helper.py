"""random thoughts - sampling_strategy, plotting support code"""

# from multipledispatch import dispatch
from data_base import *
from data_base_creator import *
from i_data_model import *


def plot_realData_model_isolines_in_dbSpace(ax, model, param_dict={}):
    """ A helper function to make a graph

    Args:
      ax (axes): The axes to draw to
      model (IDataModel): model to display as isolines
      param_dict (dict, optional): Dictionary of kwargs to pass to ax.plot

    Returns:
      list: list of artists added

    :rtype: list
    :version: 0.0.1
    :author: sik
    """
    return model.draw_2Disoc(ax, param_dict)


def scatterPlot_realData_nparray_in_dbSpace(ax, data, param_dict=dict()):
    """ A helper function to make a graph

    Args:
        ax (axes): The axes to draw to.
        data (np.array): Data points in [[x1, y1], [x2, y2] .. [xn, yn]] form.
        param_dict (dict, optional): Dictionary of kwargs to pass to ax.plot

    Returns:
        A list of artists added to **ax** while plotting

    :rtype: list
    :version: 0.0.1
    :author: sik
    """
    return ax.scatter(data[:, 0], data[:, 1], **param_dict)


def _test():
    """ test function to call when executing this file directly """

    import matplotlib.pyplot as plt

    d = DataSimulation()
    myDataBaseExample = d.generate_default2MVGM_testcase()
    print myDataBaseExample

    xx1 = myDataBaseExample['blue'].dbeSamples
    mm1 = myDataBaseExample['blue'].dbeModel
    xx2 = myDataBaseExample['red'].dbeSamples
    mm2 = myDataBaseExample['red'].dbeModel

    fig, ax = plt.subplots()
    scatterPlot_realData_nparray_in_dbSpace(ax, xx1, {'marker': 'x'})
    scatterPlot_realData_nparray_in_dbSpace(ax, xx2)

    plot_realData_model_isolines_in_dbSpace(ax, mm1)
    plot_realData_model_isolines_in_dbSpace(ax, mm2, {'colors': 'g'})

    plt.show()

if __name__ == '__main__':
    _test()
