class DataSimulation(object):

    """Docstring for DataSimulation.
    This should be a subclass of a generic Data class.
    """

    def __init__(self, randomSeed=140589, numSamplesPerModel=100):
        """TODO: Generate separable colors for each Data class, here are links
        in distinguishable palettes.
        http://tinyurl.com/okr6bmo
        http://tinyurl.com/m89l48u
        http://tinyurl.com/llay7xa

        :randomSeed: TODO
        :models: TODO
        :numSamplesPerModel: TODO

        """
        self._randomSeed = randomSeed
        self._models = dict(
            zip(['blue', 'red'],
                [MultiVariatedGaussianModel(0, 1, 1.2, 1, 0.8),
                MultiVariatedGaussianModel(0, 0, 1.3, 0.7, 0.3)])
        )
        self._numSamplesPerModel = numSamplesPerModel

    def _str__(self):
        return 'This is a fucking shit'
