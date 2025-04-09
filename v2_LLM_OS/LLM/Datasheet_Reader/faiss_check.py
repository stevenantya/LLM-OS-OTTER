import torch
print(torch.cuda.is_available())
print(torch.cuda.get_device_name(0))  # Should show "NVIDIA GeForce MX450"

import faiss
import numpy as np

# Generate random vectors
d = 128  # Dimensionality
nb = 10000  # Database size
np.random.seed(42)
xb = np.random.random((nb, d)).astype('float32')

# Create a FAISS index on GPU
res = faiss.StandardGpuResources()  # Use GPU
index = faiss.IndexFlatL2(d)  # L2 distance
gpu_index = faiss.index_cpu_to_gpu(res, 0, index)  # Move index to GPU

# Add vectors and search
gpu_index.add(xb)
D, I = gpu_index.search(xb[:5], 5)  # Search for the top 5 nearest neighbors

print("Distances:\n", D)
print("Indices:\n", I)
