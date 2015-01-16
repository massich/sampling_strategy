"""random thoughts - sampling_strategy, support code"""


class DataClassInstance(object):
    """DataClassInstance stores relevant info to identify the data's class.

    This information describing the data in hand is further used in plots or to
    retrieve the data based on the data class attributes.

    Attributes:
        _name (str): Human readable string to identify the data in hand.
        _color (str): color code to identify the data when plotting. The color
            should be specified in hexacode as '#00ff00'.

    :Date: 2015-01-15
    :version: 0.0.1
    :author: sik
    """

    def __init__(self, name='no_name', color='#555555'):
        """ __init__ initializes the object storing name and color.

        Note:
            Despite having default attributes, no DataClassInstance should be
            initialized this manner since then data classes would be difficult
            to differentiate

        Args:
            name (str, optional): Human readable data identifier. Defaults to
                no_name.
            color (str, optional): data color identifier. Defaults to #555555

        """
        self._name = name
        self._color = color

    def get_name(self):
        """name retrieve function"""
        return self._name

    def set_name(self, value):
        """name setter function"""
        self._name = value

    def get_color(self):
        """color retrieve function"""
        return self._color

    def set_color(self, value):
        """color setter function"""
        self._color = value

    __nameProperty = property(get_name, set_name, None,
                              ['name is the data class name to appear plot'
                               'legends, etc...'])

    __colorProperty = property(get_color, set_color, None,
                               ['color is the data class attribute used to'
                                'represent the class in plots, etc...'])


def _test():
    """ test function to call when executing this file directly """

    my_dclass = DataClassInstance()
    print my_dclass.get_name()
    print my_dclass.get_color()

    my_dclass.set_name('test_name')
    my_dclass.set_color('#caca00')
    print my_dclass.get_name()
    print my_dclass.get_color()

    my_dclass = DataClassInstance('red', '#ff0000')
    print my_dclass.get_name()
    print my_dclass.get_color()

if __name__ == '__main__':
    _test()
