import torch

# Assuming xk_ and freqs_cis are tensors
xk_out = torch.view_as_real(xk_ * freqs_cis).flatten(3)
