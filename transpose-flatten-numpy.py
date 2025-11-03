# Enter your code here. Read input from STDIN. Print output to STDOUT

import numpy as np

N, M = map(int, input().split(' '))

arr = np.zeros(shape=((N, M)), dtype = int)

for i in range(N):
    arr[i] = list(map(int, input().split(' ')))

tsp_arr = arr.transpose()

# print(arr)
print(tsp_arr)
print(arr.flatten())