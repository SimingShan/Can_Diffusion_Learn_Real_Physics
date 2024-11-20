### This script is for converting velocity map into seismic data ###
### Created by Siming Shan & Eric Chen ###
import numpy as np
import matplotlib.pyplot as plt

def plot_single(data, path):
    nz, nx = data.shape
    plt.rcParams.update({'font.size': 18})
    vmin, vmax = np.min(data), np.max(data)
    fig, ax = plt.subplots(1, 1, figsize=(8, 6))
    im = ax.matshow(data, aspect='auto', cmap='gray', vmin=-1, vmax=2)

    # Set the aspect ratio to maintain correct stretching
    ax.set_aspect(aspect=nx / nz)

    # Configure x-axis to span from 0 to 700 meters with matching ticks and labels
    num_ticks = 5  # Adjust this based on the desired number of ticks
    x_ticks = np.linspace(0, nx - 1, num_ticks).astype(int)
    x_labels = np.linspace(0, 700, num_ticks).astype(int)

    ax.set_xticks(x_ticks)
    ax.set_xticklabels(x_labels)
    ax.xaxis.set_ticks_position('bottom')  # Move x-axis ticks to the bottom
    ax.set_xlabel('Length (m)')

    # Configure y-axis (Time in milliseconds)
    ax.set_yticks(range(0, nz, int(200 // (1000 / nz)))[:5])
    ax.set_yticklabels(range(0, 1000, 200))
    ax.set_ylabel('Time (ms)', fontsize=18)

    # Save the plot with zero margin
    plt.savefig(path, bbox_inches='tight', pad_inches=0)
    plt.close(fig)