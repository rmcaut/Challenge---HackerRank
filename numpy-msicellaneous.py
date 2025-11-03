import numpy as np

# def arrays(arr):
#     arr = numpy.array(arr, dtype=float)[::-1]
#     return arr  # Return a string, not an array

# arr = input().strip().split(' ')
# result = arrays(arr)
# print(result)


## Reshape
# arr = numpy.array([1,2,3,4,5,6,7,8,9,0])
# print(arr)
# print(arr.reshape(2,5))


## flatettening
arr = np.array([[1, 2, 3], [4, 5, 6]])
newarr = arr.reshape(-1)
print(newarr) 

# # sum and prod
# import numpy

# pair = input().split(' ')
# N = int(pair[0])
# M = int(pair[1])

# # print(N)
# # print(M)

# data= []

# for n in range(N):
#     new_row = list(map(int, input().split(' ')))
#     data.append(new_row)
    
# nparr = numpy.array(data)

# sum_arr = numpy.sum(nparr, axis = 0)
# # print(sum_arr)
# prod = numpy.prod(sum_arr)
# print(prod)