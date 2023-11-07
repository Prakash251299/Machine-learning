import numpy as np
# ######
# arr = np.array([1,2,3,4])
# print(arr)
# print(np.__version__)
# print(type(arr))

# ######
# arr1 = np.array((1,2,3,4,5)) # another method to declare numpy array
# print(arr1)
# print(type(arr1))

# ######
# # 0d array
# arr = np.array(42)
# print(arr)
# print(type(arr))
# print(f"{arr.ndim} dimension")

# ######
# # 1d array
# arr = np.array([1,2,3,4])
# print(arr)
# print(type(arr))
# print(f"{arr.ndim} dimension")

# ######
# # 2d array
# arr = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
# print(arr)
# print(type(arr))
# print(f"{arr.ndim} dimension")

# ######
# # 3d array
# arr = np.array([[[1,2],[3,4]],[[5,6,],[7,8]]])
# print(arr)
# print(arr[0][1][1]) 
# print(arr[0,1,1]) # same as above
# print(type(arr))
# print(f"{arr.ndim} dimension")

# #####
# Creating an nd (n dimensional) array
# arr = np.array([1,2,3,4],ndmin=3)
# print(arr)
# print(type(arr))
# print(arr.ndim)
# # print(arr[0][0][0]) # first element of 3d array
# print(arr[0,0,0]) # first element of 3d array
# print(arr[0,0,-1]) # last element of 3d array

######
# arr = np.array([12,34,53,23])
# print(arr[0])
# print(arr[0]+arr[1])
# print(arr[-1])

######
# slicing 1d array
# print(arr[1:3])
# print(arr[::-1]) # print array in reverse order
# print(arr[2::-1])
# print(arr[-3:-1])
# print(arr[-2:-4:-1])

# slicing 2d array
# arr = np.array([[1,2,3,4,5],[3,4,5,6,7],[5,6,7,8,9]])
# print(arr[0,1:3])
# print(arr[0:2,1])
# print(arr[0:,1])
# print(arr[0:3,1:3])
# print(arr.ndim)


######
# Data type 
arr = np.array([12,34,53,23])
# print(arr.dtype)
# arr = np.array([12,34,53,23],dtype = 'i')
# arr = np.array([12,34,53,'a'],dtype = 'i') # gives error
# arr = np.array([12,34,53,23],dtype = 'i4')
print(arr.dtype)

# convert data type
# arr = arr.astype('S')
# arr = arr.astype(int)
arr = arr.astype(bool)
print(arr.dtype)