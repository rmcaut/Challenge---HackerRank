# # Enter your code here. Read input from STDIN. Print output to STDOUT
# import itertools

# N = int(input())
# lst = input().split(' ')
# K = int(input())

# k_tuples = itertools.combinations(lst, K)

# count_contains_a = 0
# count_tuples = 0

# for tpl in k_tuples:
#     if 'a' in tpl:
#         count_contains_a += 1
#     count_tuples += 1

# print("{:.3f}".format(count_contains_a / count_tuples))

#############

# Enter your code here. Read input from STDIN. Print output to STDOUT

import itertools

K, M = map(int, input().split(' '))

s_max = 0

for _ in range(K):
    i_head_list = map(int, input().split(' '))
    i_list = list(i_head_list)[1:]
    i_lst_sqrt = [x*x for x in i_list]
    s = sum(i_lst_sqrt)
    s_max = max(s, s_max)
    
print(s_max % M)




