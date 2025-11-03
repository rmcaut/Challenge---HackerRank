# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import deque
T = int(input())

for _ in range(T):
    n = int(input())
    sideLenghts = str(input()).split(' ')
    d = deque(sideLenghts)
    check = "Yes"
    upperCube = max(int(d[0]), int(d[-1]))
    while len(d) > 0:
        print(d)
        max_sides = max(int(d[0]), int(d[-1]))
        if max_sides <= upperCube:
            if int(d[0]) == max_sides:
                d.popleft()
            else:
                d.pop()
            upperCube = max_sides         
        else:
            check = "No"
            break
    print(check)