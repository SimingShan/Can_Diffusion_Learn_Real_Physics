### This file is for compute the kinetic spectrum given some vorticity fields ###
### Created by Siming Shan & Eric Chen###
import torch
import matplotlib.pyplot as plt
import numpy as np


def compute_kinetic_spectrum(data, device='cpu'):
    """
    Compute kinetic energy spectrum for data of shape [a, b, c, c]
    """
    # Convert to torch tensor if necessary
    if isinstance(data, np.ndarray):
        data = torch.tensor(data, dtype=torch.float32)

    data = data.to(device)

    # Get dimensions
    *batch_dims, N, N = data.shape
    data_flat = data.reshape(-1, N, N)

    # Compute FFT
    w_h_flat = torch.fft.rfft2(data_flat) / (N * N)

    # Prepare k-space coordinates
    k_max = (N // 2) - 15
    k_x = torch.fft.fftfreq(N) * N
    k_y = torch.fft.rfftfreq(N) * N
    k_x, k_y = torch.meshgrid(k_x, k_y, indexing='ij')
    k = torch.sqrt(k_x ** 2 + k_y ** 2).to(device)

    # Binning
    k_bins = torch.arange(1, k_max + 1, 1).to(device)
    E_k_bin = torch.zeros(k_bins.shape[0], device=device)

    # Energy density
    energy_density_flat = 0.5 * torch.abs(w_h_flat) ** 2

    # Compute spectrum
    for i, k_bin in enumerate(k_bins):
        mask = (k >= k_bin - 0.5) & (k < k_bin + 0.5)
        masked_energy = energy_density_flat[:, mask]
        E_k_bin[i] = masked_energy.mean()

    return E_k_bin.cpu().numpy(), k_bins.cpu().numpy()


### Example Usage ###
'''
# Load your data
gt = np.load('train.npy')[39:40,:,:,:]
model1 = np.load('sample_denorm.npy') * 2

# Compute spectra
E_k_gt, k_bins_gt = compute_kinetic_spectrum(gt)
E_k_model1, k_bins_model1 = compute_kinetic_spectrum(model1)

# Plotting
plt.figure(figsize=(8, 6))
plt.loglog(k_bins_gt, E_k_gt, label='Ground Truth', color='blue', linewidth=2)
plt.loglog(k_bins_model1, E_k_model1, '--', label='Diffusion Generated', color='red', linewidth=2)

plt.xlabel('k')
plt.ylabel('E(k)')
plt.legend()
plt.grid(True, which="both", ls="--")
plt.ylim(bottom=1e-9)
# Save the figure
plt.savefig('spectrum.jpg', dpi=300, bbox_inches='tight')
plt.close()
'''