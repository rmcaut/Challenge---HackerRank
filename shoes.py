from collections import Counter

X = int(input())
shoes = list(map(int, input().split()))

N = int(input())

earned = 0
shoes_count = Counter(shoes)

for i in range(N):
    size, price = map(int, input().split())
    if shoes_count[size] > 0:
        earned += price
        shoes_count[size] -= 1

print(earned)              