import os
import torch

# import numpy as np
import matplotlib.pyplot as plt
from torchvision import datasets, transforms
from torchvision.datasets import MNIST
from torchvision.transforms import ToTensor

# from torch.utils.data import DataLoader
# from torch import dtype


# Load MNIST dataset
def load_MNIST():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    data_path = os.path.join(current_dir, "data")

    train = MNIST(root=data_path, train=True, transform=ToTensor(), download=False)
    test = MNIST(
        root=data_path,
        train=False,
        transform=ToTensor(),
        download=False,
    )
    train.data = train.data.float()
    test.data = test.data.float()

    return train, test


# Normalize data to [0, 1]
def normalizeMinMax(train, test):

    # Get min and max
    min = train.data.min()
    max = train.data.max()

    # Normalize
    train.data.sub_(min).div_(max - min)
    test.data.sub_(min).div_(max - min)

    return train, test


# Normalize data to z-score
def normalizeZScore(train, test):

    # Get mean ad standard deviation
    mean = train.data.mean()
    std = train.data.std()

    # Normalize
    train.data.sub_(mean).div_(std)
    test.data.sub_(mean).div_(std)

    return train, test


# Add Gaussian noise to tensor
def gauss_noise_tensor(train, n, max_sigma=0.5):
    assert isinstance(train.data, torch.Tensor)

    indices = torch.randint(0, len(train.data), (n,))

    min = 0.1
    sigma = torch.rand(n) * max_sigma
    sigma = torch.clamp(sigma, min, max_sigma)

    noise = torch.randn_like(train.data[indices]) * sigma.view(-1, 1, 1)

    # Generate synthetic data
    syntheticData = train.data[indices] + noise
    syntheticTarget = train.targets[indices]

    # Concatenate synthetic data with the original train data
    train.data = torch.cat((train.data, syntheticData), 0)
    train.targets = torch.cat((train.targets, syntheticTarget), 0)

    return train


torch.manual_seed(42)

trainMinMax, testMinMax = load_MNIST()
trainZScore, testZScore = load_MNIST()

trainMinMax, testMinMax = normalizeMinMax(trainMinMax, trainMinMax)
trainZScore, testZScore = normalizeZScore(trainZScore, testZScore)

# testGaussM = gauss_noise_tensor(testMinMax)
# testGaussZ = gauss_noise_tensor(testZScore)

# Add Gaussian noise to the data
trainGaussM = gauss_noise_tensor(trainMinMax, n=10000)
trainGaussZ = gauss_noise_tensor(trainZScore, n=10000)

# # Plot the first 5 examples of synthetic data
# fig, axes = plt.subplots(2, 5, figsize=(10, 5))

# # Plot MinMax synthetic images
# for idx in range(5):  # Plot first 5 synthetic images
#     ax = axes[0, idx]
#     ax.imshow(syntheticGaussM[idx].squeeze(), cmap="gray")
#     ax.axis("off")
#     ax.set_title(f"MinMax Img {idx+1}")

# # Plot ZScore synthetic images
# for idx in range(5):  # Plot first 5 synthetic images
#     ax = axes[1, idx]
#     ax.imshow(syntheticGaussZ[idx].squeeze(), cmap="gray")
#     ax.axis("off")
#     ax.set_title(f"ZScore Img {idx+1}")

# plt.tight_layout()
# plt.show()
