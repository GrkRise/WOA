import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import pylab
import os

for filename in os.listdir('data'):
# filename = 'OPPO_CPH1931_2022-12-06T10 55 14.686Z.csv'
    file = pd.read_csv('data/' + filename)
    x = file['X'].tolist()
    y = file['Y'].tolist()
    z = file['Z'].tolist()

    color_map = plt.get_cmap('cividis')

    for k in [x, y, z]:
        i = 0

        fig = plt.figure(figsize=(12, 8))
        axs = fig.add_subplot(111, projection='3d')
        scatter_plot = axs.scatter3D(x, y, z, c=k, cmap = color_map)
        axs.set_xlabel('X Label')
        axs.set_ylabel('Y Label')
        axs.set_zlabel('Z Label')
        plt.colorbar(scatter_plot)
        plt.savefig('images/' + filename + '_' + str(i) + '.png')
        i = i + 1
        plt.show()