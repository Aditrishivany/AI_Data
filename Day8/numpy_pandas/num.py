# #arrays using numpy
# import numpy as np
# numbers=[1, 2, 3, 4, 5]
# result = []
# for i in numbers:
#     result.append(i*1000)
# print(result)

# #1d array
# a=np.array([[1, 2, 3, 4, 5]])
# print(a)
# print(a*100)

# #2d array
# b=np.array([[1,2,3],[4,5,6]])
# print(b)
# # rows and columns
# c=np.array([[1,2,3],[4,5,6],[7,8,9]])
# print(c)

# #3d array
# d = np.array([
#     [[1,2,3],[4,5,6]],
#     [[7,8,9],[10,11,12]]
# ])
# print(d.shape)   
# print(d)
# # access elements in 3d array
# d.shape
# [2,3,3]
# #3 layers 4 rows 5 columns
# d=np.ones((3,4,5))
# print(d)
# # create 2x2x3 array of ones
# e=np.ones((2,2,3))
# print(e)

# # array[[layer],[row],[column]]
# f=d[1,0,2]
# print(f)
# #slicing 1d array
# v=d[0,0]
# print(v)
# # slicing 1d array to get all first elements from each layer
# z=d[:,0,0]
# print(z)

# # slicing 2d array
# w=d[:,0,:]
# print(w)
# #slicing 2d array to get all first rows from each layer
# s = np.arange(24)
# s = s.reshape(2,3,4)
# print(s.shape)
# print(s)

# # math operations in 3d array
# print(d+10)
# print(d*2)
# print(d**2)
# #sum of all elements in 3d array
# m=np.sum(d)
# m=np.sum(d,axis=0)
# m=np.sum(d,axis=1)
# m=np.sum(d,axis=2)
# print(m)

# # image data
# image=np.random.randint(0,255,(64,64,3))
# # 64*64 image with 3 color channels (RGB)
# r=image[:,:,0] #red channel
# g=image[:,:,1] #green channel
# b=image[:,:,2] #blue channel
# print(r)
# print(g)
# print(b)


# # use numpy and create 3d array with numbers from 1 to 24 and reshape it into shape (2,3,4)
# import numpy as np
# arr = np.arange(1, 25)
# arr = arr.reshape(2, 3, 4)
# print("Shape:", arr.shape)
# print(arr)

# '''indexing and accessing 
# print the first layer of the array
# print the element
# layer=1,row2 and column=3
# print first row of all layers 
# print the last row of all layers'''
# arr = np.arange(1, 25).reshape(2, 3, 4)
# print(arr[0])
# print(arr[1][2][3])
# print(arr[:, 0, :])
# print(arr[:, -1, :])

# '''boolean filtering 
# print all the elements whic are greater than 10
# count how many elements are even numbers
# replace all values less than 10 with 0'''
# arr = np.arange(1, 25).reshape(2, 3, 4)
# print(arr[arr > 10])
# print(np.sum(arr % 2 == 0))
# arr[arr < 10] = 0
# print(arr)

# marks of the students across multiple subjects and multiple exams. 
# analyse the performance using 3d numpy arrays

import numpy as np

marks = np.array([
    [[78, 82, 80], [65, 70, 68], [90, 92, 88], [72, 75, 74]],
    [[85, 88, 90], [72, 75, 78], [88, 86, 84], [80, 82, 85]],
    [[60, 62, 65], [55, 58, 60], [70, 72, 75], [68, 70, 72]],
    [[90, 92, 94], [85, 88, 87], [92, 94, 96], [88, 90, 89]],
    [[70, 72, 74], [65, 68, 67], [75, 78, 80], [72, 74, 76]]
])

print("Marks (Students × Subjects × Exams):")
print(marks)

student_avg = np.mean(marks, axis=(1, 2))
print("\nAverage marks of each student:")
print(student_avg)

subject_avg = np.mean(marks, axis=(0, 2))
print("\nAverage marks of each subject:")
print(subject_avg)

exam_avg = np.mean(marks, axis=(0, 1))
print("\nAverage marks of each exam:")
print(exam_avg)

print("\nStudents with average marks greater than 75:")
print(student_avg > 75)