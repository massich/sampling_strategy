class A():
    def __init__(self):
        self.aVar = 'A'         # This is managed by A class 
        self.aMorphVar = 'A'    # Subclass should modify it

    # This method should be able to be called from all children
    def __repr__(self):
        return 'method in class A:\n' \
               ' - Elements:\n\t{0}\n'
               ' - Variables:\n\t{1}\n'
               ' - Methods:\n\t{2}\n'.format(1,2,3)

    # This should be reimplemented by the subclasses
    def __str__(self):
        return 'A method: (parentVar:{0.parentVar!s}, ' \
               '\tparentVarPoliMorph: {0.parentVarPolimorph!s})'.format(self)


class ChildImplemetnation(A):
    def __init__(self):
        super(ChildImplemetnation,self).__init__()
        self.parentVarPolimorph = 'child modification'
        self.childVar = 'child own variable'
        return None

    def __str__(self):
        return 'Implementation method: (parentVar:{0.parentVar!s}, ' \
               '\tparentVarPoliMorph: {0.parentVarPolimorph!s}' \
               '\tchildVar: {0.childVar})'.format(self)


class Child(ChildImplemetnation):
    def __init__(self):
        super(Child, self).__init__()
        self.parentVarPolimorph = 'child A modification'
        self.childVar = 'child A modification'
        return None

    def __str__(self):
        return 'child method: (parentVar:{0.parentVar!s}, ' \
               '\tparentVarPolimorph: {0.parentVarPolimorph!s}' \
               '\tchildvar: {0.childVar!s})'.format(self)


class ChildExtra(ChildImplemetnation):
    def __init__(self):
        super(ChildExtra, self).__init__()
        self.childExtraVar = 'child B own variable'
        return None

    def __str__(self):
        return 'childExtra method: (\n {1}\n'\
               '\tchildExtraVar: {0.childExtraVar!s})'.format(
                self,
                super(ChildExtra, self).__str__()
                )


p = A()
cI = ChildImplemetnation()
cA = Child()
cB = ChildExtra()

print p.__repr__()
print cI.__repr__()
print cA.__repr__()
print cB.__repr__()

print p
print cI
print cA
print cB


