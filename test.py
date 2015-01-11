import numpy as np
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
from sklearn.decomposition import PCA
from abc import ABCMeta, abstractmethod, abstractproperty

import math
from data import *
from random_sampling import *
from projection_model import *
import matplotlib.pyplot as plt

x = DataSimulation(randomSeed=15031984)

# Show the data
fig = plt.figure()
ax1 = fig.add_subplot(111)
#ax1.axis(x.data_range())
x.draw_sample(ax1)
#fig.show()

all_samples = np.concatenate((x._data[0]._samples,
                             x._data[1]._samples),
                             axis=0)

# Projection model
my_projection_model = ProjectionModel('PCA', all_samples)
my_projection_model.display_base(ax1)

fig.show()

## Calculate the Data projection
#r = RandomSampler(x)
#r.show_projection(ax1)
#ax2 = fig.add_subplot(222)
#r.show_projection_axes(ax2)
#r.show_projected_samples(ax2)
#
## Show selected samples
#ax3 = fig.add_subplot(223)
#r.show_selected_samples(ax3)
