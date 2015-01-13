from data import *
from data_simulation_model import *
from rs_projection_model import *


class DataProjectionInstance(DataSimulation):
    """ DataProjectionInstance takes a Data object and rewrites its generative
    methods in order to output projected data
    """

    def __init__(self, data, projectionModel):
        """TODO: The constructor should validate that the projectionModel has a
        method transform so that the method decorations work as expected.

        :data: TODO
        :projectionModel: TODO

        """
        self._data = data
        self._projectionModel = projectionModel


class RandomSampler(object):
    """ RandomSamplier :
        1 - projects the data into lower dimension space based on a
            projection model.
        2 - based on a sampling model generates a collection of randomly
            selected subsets.

    """

    def __init__(self, data):
        """RandomSampler initalization.

        :data: TODO
        :returns: TODO

        """
        self._projectionModel = ProjectionModelPCA(data)

    def display_projection_base(self, axisId, lineW=2):
        """display_projection_base draws the projection axis into axisId handle

        :axisId: axis to plot on
        """
        self._projectionModel.display_base(axisId, lineW)


def main():

    import matplotlib.pyplot as plt
    fig, ax = plt.subplots(nrows=2, ncols=2)

    my_data = DataSimulation(n=100)
    my_ax = [ax[0][0], ax[0][1], ax[1][0]]
    for ax0 in my_ax:
        ax0.axis(my_data.get_range())
        my_data.draw_samples(ax0)
        my_data.draw_models(ax0)

    severalData = [my_data._data[0]._samples,
                   my_data._data[1]._samples,
                   my_data.get_all_data()]

    for d, ax0, lw in zip(severalData, my_ax, [0.5, 0.5, 1]):
        my_randSampler = RandomSampler(d)
        my_randSampler.display_projection_base(ax0, lw)

    plt.show()

if __name__ == '__main__':
    main()
