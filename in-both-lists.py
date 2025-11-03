from collections import defaultdict

n, m = map(int, input().split())

A_list = [input().strip() for _ in range(n)]
B_list = [input().strip() for _ in range(m)]

B_set = set(B_list)  # O(1) lookups
C = defaultdict(list)

# Record indexes for words in B
for i, val in enumerate(A_list, start=1):
    if val in B_set:
        C[val].append(i)

# Output for each word in B_list
for val in B_list:
    print(" ".join(map(str, C.get(val, [-1]))))