# Enter your code here. Read input from STDIN. Print output to STDOUT
import itertools

S=str(input())

data = list(S)

duples = []

for key, group in itertools.groupby(data):
    duples.append("({1}, {0})".format(key, len(list(group))))

#print(duples)   
print(" ".join(duples))

