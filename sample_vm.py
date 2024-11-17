### This script is for sampling the Velocity Map from pretained model ###
### Created by Siming Shan & Eric Chen ###
import torch
from torch.optim import Adam
from accelerate import Accelerator
from denoising_diffusion_pytorch_modified import Trainer,Unet, GaussianDiffusion
model = Unet(
    dim = 64,
    dim_mults = (1, 2, 4, 8),
    flash_attn = False,
    channels = 1
)

diffusion = GaussianDiffusion(
    model,
    image_size = 72,
    timesteps = 1000,    # number of steps
    sampling_timesteps = 250
)

accelerator = Accelerator(
            split_batches = True,
            mixed_precision = 'fp16'
        )

opt = Adam(diffusion.parameters(), lr = 8e-5, betas = (0.9, 0.99))
diffusion, opt = accelerator.prepare(diffusion, opt)
diffusion = accelerator.unwrap_model(diffusion)
diffusion.load_state_dict(torch.load('models/vm/model-4.pt', map_location='cuda')['model'])
diffusion.eval()
sampled_images = diffusion.sample(batch_size = 25)