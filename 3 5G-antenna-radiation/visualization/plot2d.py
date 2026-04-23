import numpy as np
import matplotlib.pyplot as plt

def plot_2d(theta, gain, title="Patrón 2D"):
    plt.figure()
    ax = plt.subplot(111, polar=True)
    ax.plot(theta, gain)
    ax.set_title(title)
    plt.show()