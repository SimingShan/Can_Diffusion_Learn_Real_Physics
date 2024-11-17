# Physical Field Generation via Diffusion Models

## Dataset and Model Weights Access

### Datasets
- **Kolmogorov Flow Dataset**: [Download Link](https://drive.google.com/file/d/1CUHSF9pUtsrEtHKd07dFuplK7RtVx6ck/view?usp=drive_link)
- **Velocity Map Dataset (Geophysics)**: Available at [OpenFWI Project](https://sites.google.com/site/youzuolin044/openfwi)

### Pre-trained Models
- **Kolmogorov Flow Model**: [Download Weights](https://drive.google.com/file/d/1RRQN71KGJS-pruVhf2kDv0e4Z8Z3ow46/view?usp=sharing)
- **Geophysics Velocity Map Model**: [Download Weights](https://drive.google.com/file/d/1n4Alx2foT0oJ5Ve-wxuBO31-3sLzw508/view?usp=sharing)

## Results Visualization

### 1. Fluid Mechanics Example: Kolmogorov Flow Generation

#### 1.1 Diffusion Process Overview
<div align="center">
    <img src="Github_Plot/diff_process.jpg" alt="Diffusion Process" width="800"/>
</div>
<p align="center">
    <em>Progressive denoising process: From random noise to physically meaningful flow patterns. The visualization demonstrates how our diffusion model gradually constructs coherent fluid structures.</em>
</p>

#### 1.2 Flow Field Generation Results
<div align="center">
    <img src="Github_Plot/generated_vorticity.png" alt="Generated Vorticity Fields" width="800"/>
</div>
<p align="center">
    <em>Generated vorticity fields demonstrating the model's ability to capture complex flow structures and diverse pattern formations in Kolmogorov flow.</em>
</p>

#### 1.3 Flow Analysis
<div align="center">
    <img src="Github_Plot/velocity_field.png" alt="Velocity Field Analysis" width="800"/>
</div>
<p align="center">
    <em>Velocity field spatial distribution analysis showing the characteristic patterns of Kolmogorov flow.</em>
</p>

#### 1.4 Physical Validation
<div align="center">
    <img src="Github_Plot/spectrum.jpg" alt="Spectral Analysis" width="600"/>
</div>
<p align="center">
    <em>Spectral analysis of the generated Kolmogorov flow fields, validating physical consistency through energy distribution across different scales.</em>
</p>

### 2. Geophysics Example: Velocity Map Generation

#### 2.1 Generated Samples
<div align="center">
    <img src="Github_Plot/generated_velocity.png" alt="Generated Velocity Maps" width="800"/>
</div>
<p align="center">
    <em>Sample set of generated geophysical velocity maps, showcasing the model's capability to produce diverse yet physically consistent subsurface velocity distributions.</em>
</p>

#### 2.2 Forward Prediction
<div align="center">
    <img src="Github_Plot/velocity_forward.png" alt="Forward Velocity Prediction" width="800"/>
</div>
<p align="center">
    <em>Forward velocity prediction results for geophysical scenarios. Comparison between model predictions and reference data demonstrates the accuracy of our approach in capturing subsurface structures.</em>
</p>