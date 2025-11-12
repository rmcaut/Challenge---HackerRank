import itertools

N = int(input())
en_string = "".join(input().split())
en_letters = [c for c in en_string]
# print(en_letters)
K = int(input())
combination = itertools.combinations([i for i in range(N)], K)

counter_contains = 0
counter_combo = 0  

for combo in combination:
    # print(combo)
    counter_combo += 1
    for ix in combo:
        # print(ix)
        if en_letters[ix] == 'a':
            counter_contains += 1