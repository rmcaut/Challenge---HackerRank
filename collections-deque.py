from collections import deque

t = int(input())
d = deque()

for _ in range(t):
    command = str(input()).split(' ')
    match command[0]:
        case "append":
            d.append(command[1])
            #print(*d)
        case "appendleft":
            d.appendleft(command[1])
            #print(*d)
        case "pop":
            d.pop()
            #print(*d)
        case "popleft":
            d.popleft()
            #print(*d)
print(*d)









## How to use deque:
    # d.append('<')
    # print(d)
    # d.appendleft('>')
    # print(d)
    # d.pop()
    # print(d)
    # d.append('<')
    # print(d)
    # d.popleft()
    # print(d)
    # d.append('>')
    # print(d)
    # d.extend('12345')
    # d.append('<')
    # print(d)
    # d.remove('3')
    # d[-1] <- the right most
    # len(d)
    # Convert a list my_list to deque: my_deque = deque(my_list) or a deque to a list: my_list = list(my_deque)
    # Convert a string my_string to deque: my_deque = deque(my_string) or a deque to a string: my_string = ''.join(my_deque)
    # d.extendleft('12345') # adds to the left in reverse order
