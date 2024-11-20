### This script is for convert the vorticity field to velocity field ###
### Created by Siming Shan & Eric Chen ###
import numpy as np
import torch
import matplotlib.pyplot as plt

def vorticity_to_velocity(w, dx=1.0, device='cpu'):
    """
    Convert vorticity field to velocity components using stream function method
    """
    if len(w.shape) != 2:
        raise ValueError(f"Input must be 2D array, got shape {w.shape}")

    if isinstance(w, np.ndarray):
        w = torch.tensor(w, dtype=torch.float32)

    w = w.to(device)

    nx, ny = w.shape
    k_x = 2 * np.pi * torch.fft.fftfreq(nx, dx).to(device)
    k_y = 2 * np.pi * torch.fft.rfftfreq(ny, dx).to(device)
    kx, ky = torch.meshgrid(k_x, k_y, indexing='ij')

    k_square = kx ** 2 + ky ** 2
    k_square[0, 0] = 1.0

    w_hat = torch.fft.rfft2(w)
    psi_hat = -w_hat / k_square

    u_hat = 1j * ky * psi_hat
    v_hat = -1j * kx * psi_hat

    u = torch.fft.irfft2(u_hat, s=w.shape).real
    v = torch.fft.irfft2(v_hat, s=w.shape).real

    return u.cpu().numpy(), v.cpu().numpy()


def create_velocity_plot(vorticity, save_path=None, figsize=(8, 8), skip=8, scale=60):
    """
    Create and save plot of vorticity field with velocity vectors
    """
    n = vorticity.shape[0]
    x = np.linspace(0, 1, n)
    y = np.linspace(0, 1, n)
    X, Y = np.meshgrid(x, y)

    u, v = vorticity_to_velocity(vorticity)

    # Create figure without margins
    fig = plt.figure(figsize=figsize, frameon=False)
    ax = plt.Axes(fig, [0., 0., 1., 1.])
    ax.set_axis_off()
    fig.add_axes(ax)

    # Plot vorticity contour
    ax.imshow(vorticity.T, origin='lower', extent=[0, 1, 0, 1],
              cmap='RdBu_r', aspect='equal')

    # Add velocity vectors
    ax.quiver(X[::skip, ::skip], Y[::skip, ::skip],
              u[::skip, ::skip].T, v[::skip, ::skip].T,
              color='black', scale=scale, width=0.005)

    if save_path:
        plt.savefig(save_path, dpi=300, bbox_inches='tight', pad_inches=0)
        plt.close()
    else:
        plt.show()


def process_multiple_snapshots(data_path, num_samples=4, output_prefix='velocity_plot'):
    """
    Process and plot multiple vorticity snapshots
    """
    data = np.load(data_path)[0]
    print(f"Processing {num_samples} snapshots from data shape: {data.shape}")

    for i in range(num_samples):
        vorticity = data[30 * i]
        save_path = f'{output_prefix}_{i}.png'
        create_velocity_plot(vorticity, save_path)
        print(f"Generated plot {i + 1}/{num_samples}")


### Example Usage ###
'''
DATA_PATH = 'train.npy'
NUM_SAMPLES = 4

process_multiple_snapshots(
    data_path=DATA_PATH,
    num_samples=NUM_SAMPLES,
    output_prefix='velocity_plot'
)
'''