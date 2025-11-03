# Enter your code here. Read input from STDIN. Print output to STDOUT

data = list(input())

data = [int(x) if x.isdigit() else x for x in data]

ints_even = []
ints_odd = []
uppers = []
lowers = []

# data = [1, 2, 'A', 'B', 'c', 'd', 3, 4, 'E', 'f']

for x in data:
    if isinstance(x, int):
        if int(x) % 2 == 0:
            ints_even.append(x)
        else: ints_odd.append(x)
    elif isinstance(x, str) and x.isupper():
        uppers.append(x)
    elif isinstance(x, str) and x.islower():
        lowers.append(x)
        
ints_odd = sorted(ints_odd)
ints_even = sorted(ints_even)
uppers = sorted(uppers)
lowers = sorted(lowers)

result = lowers + uppers + ints_odd + ints_even
print("".join(map(str, result)))

# print("Even Integers:", ints_even)
# print("Odd Integers:", ints_odd)
# print("Uppers:", uppers)
# print("Lowers:", lowers)

