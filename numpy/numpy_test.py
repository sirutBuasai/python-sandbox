#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
"""
PRACTICE PROGRAM FOR NUMPY
"""
# pylint: disable=W0311
#
# Imports
#
import numpy as np

#
# Global Functions
#
def print_array(string, array):
  """
  Print out array name and array value
  """
  print(f"{string}:\n{array}\n")

#
######################################################################
#
# The Basics
#
# Simple array
arr = np.array([1,2,3], dtype='int32')
print_array("arr", arr)

# Simple nested arrays
nested_arr = np.array([[8.0,7.0,6.0],
                      [5.0,4.0,3.0]])
print_array("nested_arr", nested_arr)

# Get dimension of an array
print(f"arr's dimesion: {arr.ndim}")
print(f"nested_arr's dimension: {nested_arr.ndim}\n")

# Get shape of an array
print(f"arr's dimesion: {arr.shape}")
print(f"nested_arr's dimension: {nested_arr.shape}\n")

# Get data type
print(f"arr's dtype: {arr.dtype}")
print(f"nested_arr's dtype: {nested_arr.dtype}\n")

# Get data size in byte
print(f"arr's element size: {arr.itemsize} bytes")
print(f"nested_arr's element size: {nested_arr.itemsize} bytes\n")

# Get total array size
print(f"arr's total size: {arr.nbytes} bytes")
print(f"nested_arr's total size: {nested_arr.nbytes} bytes\n")

#
######################################################################
#
# Indexing/Accessing/Changing specific elements, rows, columns
#
arr2 = np.array([[1,2,3,4,5,6,7],
                [8,9,10,11,12,13,14]])
print_array("arr2", arr2)

# Get specific element [row, column]
print(f"arr2's second row, fifth column: {arr2[1,5]}\n")

# Get a specific row/colume [row, :] or [:, column]
print(f"arr2's first row: {arr2[0,:]}\n")
print(f"arr2's second column: {arr2[:,1]}\n")

# Get specific set of elements [start_index:end_index:step_size]
print(f"every other element between 2-6: {arr2[0,1:6:2]}\n")

# Change element value
arr2[1,5] = 20
print_array("arr2", arr2)

arr2[:,2] = 99
print_array("arr2", arr2)

# 3 dimensions array
arr_3d = np.array([[[1,2],[3,4]],
                  [[5,6],[7,8]]])
print_array("arr_3d", arr_3d)

# Get specific element (work outside in)
print(f"arr_3d's element 3: {arr_3d[0,1,0]}")
print(f"arr_3d's elements 4,8: {arr_3d[:,1,1]}\n")

# Replace with same dimensions
arr_3d[:,1,:] = [[99,99],
                [88,88]]
print_array("arr_3d", arr_3d)

#
######################################################################
#
# Types of arrays
#
# All 0s matrix
zeros_matrix = np.zeros((3,3))
print_array("zeros_matrix", zeros_matrix)

# All 1s matrix
ones_matrix = np.ones((4,2,2), dtype='int32')
print_array("ones_matrix", ones_matrix)

# Any other number ((size,size), number, dtype)
ninenines_matrix = np.full((2,2), 99, dtype='float32')
print_array("ninenines_matrix", ninenines_matrix)

# Random decimal numbers (shape)
decimal_rand = np.random.rand(3,2)
print_array("decimal_rand", decimal_rand)

# Random integer numbers (start_num, end_num, shape)
int_rand = np.random.randint(-8,8, size=(3,3))
print_array("int_rand", int_rand)

# Identity matrix
identity_matrix = np.identity(2, dtype='int16')
print_array("identity_matrix", identity_matrix)

# Repeat arrays
arr3 = np.array([[1,2,3]])
rep_arr3 = np.repeat(arr3,3, axis=0)
print_array("arr3", arr3)
print_array("rep_arr3", rep_arr3)

# Copying arrays
a = np.array([1,2,3])
b = a.copy()
b[0] = 99
print_array("a", a)
print_array("b", b)

#
######################################################################
#
# Array arithmetics
#
arr4 = np.array([1,2,3,4,5,6], dtype='float16')
print_array("arr4", arr4)

# Addition
arr4 += 2
print_array("arr4", arr4)

# Subtraction
arr4 -= 2
print_array("arr4", arr4)

# Multiplicaiton
arr4 *= 2
print_array("arr4", arr4)

# Division
arr4 /= 2
print_array("arr4", arr4)

# Square
arr4 **= 2
print_array("arr4", arr4)

# Sine function
arr4 = np.sin(arr4)
print_array("arr4", arr4)

#
######################################################################
#
# Linear Algebra
#
# Matrix multiplicaiton
a = np.ones((2,3))
print_array("a", a)

b = np.full((3,2),2)
print_array("b", b)

c = np.matmul(a,b)
print_array("c", c)

# Matrix determinant
d = np.identity(3)
d_det = np.linalg.det(d)
print_array("d_det", d_det)

#
######################################################################
#
# Statistics
#
stats = np.array([[1,2,3],
                  [4,5,6]])
print_array("stats", stats)

# Minimum in a matrix
stats_min = np.min(stats)
print_array("stats_min", stats_min)

# Maximum in a matrix
stats_max = np.max(stats)
print_array("stats_max", stats_max)

# Sum of elements
stats_sum = np.sum(stats, axis=0)
print_array("stats_sum", stats_sum)

#
######################################################################
#
# Reorganizing arrays
#
# Reshapring matrix
before = np.array([[1,2,3,4],
                  [5,6,7,8]])
after = before.reshape(8,1)
print_array("before", before)
print_array("after", after)

# Vertical stacking vectors
v1 = np.array([1,2,3,4])
v2 = np.array([5,6,7,8])
vertical_stack = np.vstack([v1,v2,v1,v2])
print_array("vertical_stack", vertical_stack)

# Horitzontal stacking vectors
v1 = np.array([1,2,3,4])
v2 = np.array([5,6,7,8])
horizontal_stack = np.hstack([v1,v2,v1,v2])
print_array("horizontal_stack", horizontal_stack)
