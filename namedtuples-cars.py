# Enter your code here. Read input from STDIN. Print output to STDOUT

from collections import namedtuple

N = int(input()) # Total number of students

column_headers = input().split()

i_marks = column_headers.index('MARKS')

# print(i_marks)

sum_marks = 0

for _ in range(N):
    row = input().split()
    mark = int(row[i_marks])
    sum_marks += mark

average_marks = sum_marks / N
print(f'{average_marks:.2f}')



