# if __name__ == '__main__':
#     s = ['a', 'b', 'a', 'c', '-sufix']
#     substr = []
#     seen = set()
#     for c in s:
#         if c not in seen:
#             seen.add(c)
#             substr.append(c)
#     print(substr)
#     print(''.join(substr))



def merge_the_tools(string, k):
    # your code goes here
    string_list = [c for c in string]
    print(string_list)
    block = len(string) // k
    for i in range(block):
        susbtring_list = string_list[i*k:(i+1)*k]
        # print(susbtring_list)
        print(remove_duplicates(susbtring_list))

def remove_duplicates(susbtring_list):
    seen = set()
    uniques_list = []
    for c in susbtring_list:
        if c not in seen:
            seen.add(c)
            uniques_list.append(c)
    return ''.join(uniques_list)

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)


# merge = merge_the_tools("aabca", 2)

# simple = remove_duplicates(['a', 'a', 'b', 'c', 'a'])
# print(simple)