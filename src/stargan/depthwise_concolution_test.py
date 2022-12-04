import numpy as np
import torch
import torch.nn as nn

def Conv2d_depthwise(in_channels, out_channels, kernel_size, stride=1, padding=1,bias=True):
    depth_conv = nn.Conv2d(in_channels=in_channels, out_channels=in_channels, kernel_size=kernel_size, stride=stride,padding=padding,bias=bias,groups=in_channels)
    point_conv = nn.Conv2d(in_channels=in_channels, out_channels=out_channels, kernel_size=1)

    depthwise_separable_conv = torch.nn.Sequential(depth_conv, point_conv)

    return depthwise_separable_conv


conv = nn.Conv2d(in_channels=10, out_channels=32, kernel_size=3)
params = sum(p.numel() for p in conv.parameters() if p.requires_grad)

x = torch.rand(5, 10, 50, 50)
out = conv(x)

depth_conv = nn.Conv2d(in_channels=10, out_channels=10, kernel_size=3, groups=10)
point_conv = nn.Conv2d(in_channels=10, out_channels=32, kernel_size=1)

depthwise_separable_conv = torch.nn.Sequential(depth_conv, point_conv)
params_depthwise = sum(p.numel() for p in depthwise_separable_conv.parameters() if p.requires_grad)
out_depthwise = depthwise_separable_conv(x)

depthwise_separable_conv2 = Conv2d_depthwise(in_channels=10, out_channels=32, kernel_size=3)
params_depthwise2 = sum(p.numel() for p in depthwise_separable_conv.parameters() if p.requires_grad)
out_depthwise2 = depthwise_separable_conv(x)

print(f"The standard convolution uses {params} parameters.")
print(f"The depthwise separable convolution uses {params_depthwise} parameters.")
print(f"The depthwise separable convolution with our function uses {params_depthwise2} parameters.")

assert out.shape == out_depthwise.shape, "Size mismatch"
assert out.shape == out_depthwise2.shape, "Size mismatch our function"