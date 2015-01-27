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


def _test():
    """ test function to call when executing this file directly """

#    d = DataSimulation()
#    myDataBaseExample = d.generate_default2MVGM_testcase()
#
#    print myDataBaseExample
    
    import matplotlib.pyplot as plt
     import numpy as np
    # import matplotlib.mlab as mlab
    N = 50
    x = np.random.rand(N)
    y = np.random.rand(N)
    colors = np.random.rand(N)
    area = np.pi * (15 * np.random.rand(N))**2 # 0 to 15 point radiuses

    plt.scatter(x, y, s=area, c=colors, alpha=0.5)
    plt.show()

if __name__ == '__main__':
    _test()
