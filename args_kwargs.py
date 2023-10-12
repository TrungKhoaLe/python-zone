# Example 1: unpacking keyword arguments
def my_plotter(ax, data1, data2, param_dict):
    out = ax.plot(data1, data2, **param_dict)
    return out

# call the function
import numpy as np
import matplotlib.pyplot as plt


data1, data2 = np.random.randn(2, 100)
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(5, 2.7))
my_plotter(ax1, data1, data2, {'marker': 'x'})
