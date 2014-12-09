def isVariable(obj, varName):
    return not callable(getattr(obj, varName)) and not varName.startswith('__')


def isMethod(obj, varName):
    return callable(getattr(obj, varName))


def getVariablesAndNames(obj):
    return dict(
        (name, getattr(obj, name))
        for name in [
            element for element in dir(obj) if isVariable(obj, element)
            ]
        )


def getMethodNames(obj):
    return [element for element in dir(obj) if isMethod(obj, element)]


class A(object):
    __slots__ = ["aVar", "aMorphVar"]

    def __init__(self):
        self.aVar = 'A'         # This is managed by A class
        self.aMorphVar = 'A'    # Subclass should modify it

    # This method should be able to be called from all children
    def __repr__(self):
        return 'method in class A:\n'  \
            ' - Elements:\n\t{0}\n' \
            ' - Variables:\n\t{1}\n'\
            ' - Methods:\n\t{2}\n'.format(
                dir(self), getVariablesAndNames(self), getMethodNames(self)
                )

    def __str__(self):
        raise NotImplementedError('__str__')


class B(A):
    def __init__(self):
        pass


class C(A):
    def __init__(self):
        A.__init__(self)


class D(A):
    def __init__(self):
        super(D, self).__init__()


a = A()
b = B()
c = C()
d = D()
