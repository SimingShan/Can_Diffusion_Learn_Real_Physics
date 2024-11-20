### This script is for training the Kolmogorov diffusion model ###
### Created by Siming Shan & Eric Chen ###
import torch
import numpy as np
from denoising_diffusion_pytorch import Unet, GaussianDiffusion
from script.denoising_diffusion_pytorch_modified import Trainer
# Load and prepare data
data_path = 'data/train.npy'
np_data = np.load(data_path)
res = 256
resized_data = np_data.reshape(-1, 1, res, res)

# Convert to float16 and normalize
tensor_data = torch.as_tensor(resized_data, dtype=torch.float16)
min_val = tensor_data.min()
max_val = tensor_data.max()
training_images = (tensor_data - min_val) / (max_val - min_val)

# Initialize model
model = Unet(
    dim=64,
    dim_mults=(1, 2, 4, 8),
    flash_attn=False,
    channels=1
)

# Setup diffusion
diffusion = GaussianDiffusion(
    model,
    image_size=res,
    timesteps=1000,
    sampling_timesteps=250,
    objective='pred_noise'
)

# Initialize trainer
trainer = Trainer(
    diffusion,
    training_images,
    train_batch_size=8,
    train_lr=0.0002,
    train_num_steps=300000,
    gradient_accumulate_every=2,
    ema_decay=0.995,
    amp=True,
    calculate_fid=False,
    results_folder='./models/kf/'
)

trainer.train()