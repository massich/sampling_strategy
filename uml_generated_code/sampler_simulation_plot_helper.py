"""random thoughts - sampling_strategy, support code"""

#from multipledispatch import dispatch


def my_plotter(ax, data1, data2, param_dict):
    """ A helper function to make a graph

    Args:
      ax (axes): The axes to draw to
      data1 (array): The x data
      data2 (array): The y data
      param_dict (dict, optional): Dictionary of kwargs to pass to ax.plot

    Returns:
      list: list of artists added

    """
    out = ax.plot(data1, data2, **param_dict)
    return out
