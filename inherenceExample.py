class Parent():
    def __init__(self):
        self.parentVar = 'parent variable to not touch'
        self.parentVarPolimorph = 'parent variable to touch'
        return None

    # This method should be able to be called from all children
    def __repr__(self):
        varNames = []
        methodNames = []
        for element in dir(self):
            if not callable(getattr(self, element)):
                varNames.extend([element])
            else:
                methodNames.extend([element])
        return 'Representation(Parent method):\n' \
               '\tvars:\n\t\t{0}\n' \
               '\tmethods:\n\t\t{1}\n'.format(', '.join(varNames),
                                              ', '.join(methodNames))
#               '\tparentVar:{0.parentVar!r},' \
#               '\tparentVarPoliMorph: {0.parentVarPolimorph!r}'.format(self)

    # This should be reimplemented by the subclasses
    def __str__(self):
        return 'Parent method: (parentVar:{0.parentVar!s}, ' \
               '\tparentVarPoliMorph: {0.parentVarPolimorph!s})'.format(self)


class ChildImplemetnation(Parent):
    def __init__(self):
        Parent.__init__(self)
        self.parentVarPolimorph = 'child modification'
        self.childVar = 'child own variable'
        return None

    def __str__(self):
        return 'Implementation method: (parentVar:{0.parentVar!s}, ' \
               '\tparentVarPoliMorph: {0.parentVarPolimorph!s}' \
               '\tchildVar: {0.childVar})'.format(self)


class Child(ChildImplemetnation):
    def __init__(self):
        Parent.__init__(self)
        self.parentVarPolimorph = 'child A modification'
        self.childVar = 'child A modification'
        return None

    def __str__(self):
        return 'child method: (parentVar:{0.parentVar!s}, ' \
               '\tparentVarPolimorph: {0.parentVarPolimorph!s}' \
               '\tchildvar: {0.childVar!s})'.format(self)


class ChildExtra(ChildImplemetnation):
    def __init__(self):
        Parent.__init__(self)
        self.childExtraVar = 'child B own variable'
        return None

    def __str__(self):
        return 'childExtra method: (parentVar:{0.parentVar!s}, ' \
               '\tparentVarPolimorph: {0.parentVarPolimorph!s}' \
               '\tchildExtraVar: {0.childExtraVar!s})'.format(self)


p = Parent()
cI = ChildImplemetnation()
cA = Child()
cB = ChildExtra()

p
print p
print cI
print cA
print cB
