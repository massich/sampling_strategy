import random


class ShapeFactory:

    @staticmethod
    def createShape(*argv, **kwargv):
        # First parameter is supposed to be the class name to instanciate
        print "ShapeFactory::createShape:: {}".format(locals())
        try:
            if issubclass(eval(id), Shape):
                # return the subclass factoryMethod
                return eval(argv[0])._create(*argv[1:], **kwargv)
            else:
                raise TypeError
        except (TypeError, NameError):
            validTypeNames = [s.__name__ for s in Shape.__subclasses__()]
            raise TypeError("""'{0}' is an invalid Shape subclass. \
                            Valid type names are:\n\t{1:s}""".format(id,
                            '\n\t'.join(validTypeNames)))


class Shape(object):
    @classmethod  # try it with classmethod at the superclass then cls...
    def _create(cls, *argv, **kwargv):
        print "{0:<27s} {1}".format(
            "{}::_create::".format(cls.__name__), locals())
        myObj = object.__new__(cls)
        myObj.__init__(*argv, **kwargv)
        return myObj


class Circle(Shape):
    def __init__(self, color='blue', *argv, **kwargv):
        print "{0:<27s} {1}".format("Circle::__init__::", locals())
        self._color = color

    def draw(self):
        print("Circle.draw, in color {}".format(self._color))

    def erase(self):
        print("Circle.erase")


class Square(Shape):
    def __init__(self, color='red', *argv, **kwargv):
        print "{0:<27s} {1}".format("Square::__init__::", locals())
        self._color = color

    def draw(self):
        print("Square.draw, in color {}".format(self._color))

    def erase(self):
        print("Square.erase")


def shapeNameGen(n):
    # http://sahandsaba.com/python-iterators-generators.html
    # g = (random.random() < 0.4 for __ in itertools.count())
    types = Shape.__subclasses__()
    for i in range(n):
        yield random.choice(types).__name__


def _test():

    assert issubclass(Circle, Shape)
    assert issubclass(Square, Shape)

    # Create sublcass instances directly
    for s in [Circle(), Square()]:
        s.draw()
        s.erase()
    
    print "Start testing the factory"
    shapeObjects = [
        ShapeFactory.createShape(next(shapeNameGen(1)), 'purple'),
        ShapeFactory.createShape(next(shapeNameGen(1)), color='green'),
        ShapeFactory.createShape(next(shapeNameGen(1)), stupidParam='stupid')
        ]

    # shapeObjects = [ShapeFactory.createShape(sType)
    #                 for sType in shapeNameGen(N)]

    # print shapeObjects
    for idx, s in enumerate(shapeObjects):
        print "Shape ({0:d})_________".format(idx)
        s.draw()
        s.erase()

if __name__ == '__main__':
    _test()
