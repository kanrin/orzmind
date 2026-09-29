import torch

print("cuda", torch.cuda.is_available())
print("mps", torch.mps.is_available())
print("cpu", torch.cpu.is_available())
