#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
"""
PRACTICE PROGRAM FOR PYTORCH
"""
# pylint: disable=W0311
#
# Imports
#
import urllib
import numpy as np
import torch
import torchvision
from torchvision import transforms, datasets
import matplotlib.pyplot as plt

#
# Global Functions
#
def print_array(string, array):
  """
  Print out array name and array value
  """
  print(f"{string}:\n{array}\n")

#
# https://stackoverflow.com/questions/60548000/getting-http-error-403-forbidden-error-when-download-mnist-dataset
# Get around MNIST Download error
#
opener = urllib.request.build_opener()
opener.addheaders = [('User-agent', 'Mozilla/5.0')]
urllib.request.install_opener(opener)

#
######################################################################
#
# The Basics
#
# Simple array
x = torch.Tensor([5,3])
y = torch.Tensor([2,1])
print_array("x*y", x*y)

# Zeros array in 3x2 matrix
x = torch.zeros([3,2])
print_array("x", x)
print_array("x's shape", x.shape)

# Random array
y = torch.rand([2,5])
print_array("y", y)
print_array("y's shape", y.shape)

# Reshaping array
y = y.view([1,10])
print_array("y", y)
print_array("y's new shape", y.shape)

#
######################################################################
#
# Accessing MNIST datasets
#
# pylint: disable=C0301
train = datasets.MNIST(root="./", train=True, download=True, transform=transforms.Compose([transforms.ToTensor()]))
test = datasets.MNIST(root="./", train=False, download=True, transform=transforms.Compose([transforms.ToTensor()]))
# pylint: enable=C0301

# Load data sets into batches
trainset = torch.utils.data.DataLoader(train, batch_size=10, shuffle=True)
testset = torch.utils.data.DataLoader(test, batch_size=10, shuffle=True)

# Print the first 10 data from trainset
for data in trainset:
  print(data)
  break

print_array("data[0][0]'s shape", data[0][0].shape)

# Show image of data[0][0]
plt.imshow(data[0][0].view(28,28))
# plt.show()

# Show that the data set is balanced
# NOTE: unbalanced data set can lead to a deadlock local minima in the network
total = 0
counter_dict = {0:0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0}

for data in trainset:
  Xs, Ys = data
  for y in Ys:
    counter_dict[int(y)] += 1
    total += 1

print(f"Data counter: {counter_dict}")

for item in counter_dict:
  percentage = round(((counter_dict[item]/total)*100),2)
  print(f"{item}: {percentage}%")
