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

def foo(bar, baz=None):
    """
    This is a prose description of foo and all the great
    things it does.

    Parameters
    ----------
    bar : (type of bar)
        A description of bar

    baz : (type of baz), optional
        A description of baz

    Returns
    -------
    foobar : (type of foobar)
        A description of foobar
    foobaz : (type of foobaz)
        A description of foobaz
    """
    # some very clever code
    return foobar, foobaz
