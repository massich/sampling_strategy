import numpy as np
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
from sklearn.decomposition import PCA
from abc import ABCMeta, abstractmethod, abstractproperty

import math
from data import *
from random_sampling import *
import matplotlib.pyplot as plt

x = DataSimulation(randomSeed=15031984)

# Show the data
fig = plt.figure()
ax1 = fig.add_subplot(221)
ax1.axis(x.data_range())
x.show_all_data(ax1)

# Calculate the Data projection
r = RandomSampler(x)
r.show_projection(ax1)
ax2 = fig.add_subplot(222)
r.show_projection_axes(ax2)
r.show_projected_samples(ax2)

# Show selected samples 
ax3 = fig.add_subplot(223)
r.show_selected_samples(ax3)
