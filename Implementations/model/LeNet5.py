# This file regulates the concrete network architecture for cllassification
#
# In: 1*50*50
# conv2d: 1 in channel 
#         16 out channels
#         5*5 kernal
#         1 step per conv
#         1 padding
# Out: 16*48*48
# maxPooling: 2*2 kernal
#             2 step per conv
# Out: 16*24*24
# conv2d: 16 in channel 
#         32 out channels
#         5*5 kernal
#         1 step per conv
#         2 padding
# Out: 32*24*24
# maxPooling: 2*2 kernal
#             2 step per conv
# Out: 32*12*12
# Linear: 32*12*12 -> 4

import torch
import torch.nn as nn
import torch.nn.functional as F

from torch.autograd import Variable
import torch.utils.data as Data
import torchvision

import matplotlib.pyplot as plt

# network architecture

class CNN(nn.Module):    
    # layers
    def __init__(self):
        super(CNN, self).__init__()
        
        self.conv1 = nn.Sequential(
            nn.Conv2d(
                in_channels = 1,
                out_channels = 16,
                kernel_size = 5,
                stride = 1,
                padding = 1,
            ),
            nn.ReLU(),
            nn.MaxPool2d(
                kernel_size = 2,
            ),
        )
        
        self.conv2 = nn.Sequential(
            nn.Conv2d(16, 32, 5, 1, 2),
            nn.ReLU(),
            nn.MaxPool2d(2),
        )
        
        self.out = nn.Linear(32 * 12 * 12, 4)
    
    # connections
    def forward(self, x):
        x = self.conv1(x)
        x = self.conv2(x)
        x = x.view(x.size(0), -1)
        output = self.out(x)
        return output