def merge_the_tools(string, k):
    # your code goes here
    string_list = [c for c in string]
    print(k)
    num_blocks = len(string_list) // k
    print(num_blocks)
    for i in range(num_blocks):
        block_list = string_list[i*k:(i+1)*k]
        print(block_list)
        block_substring = ''.join(block_list)
        print(block_substring)

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)