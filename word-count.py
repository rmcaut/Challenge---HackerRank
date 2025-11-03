# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import defaultdict

n = int(input())

seen = set()
word_count = defaultdict()

for _ in range (n):
    word = str(input())
    if word in seen:
        word_count[word] += 1
    else: 
        seen.add(word)
        word_count[word] = 1

print(len(seen))
result = ' '.join([str(v) for k, v in word_count.items()])
print(result)








# # Enter your code here. Read input from STDIN. Print output to STDOUT

# n = int(input())

# seen = set()
# word_count = {}

# for _ in range (n):
#     word = str(input())
#     if word in seen:
#         word_count[word] = word_count.get(word, 0) + 1
#     else: 
#         seen.add(word)
#         word_count[word] = 1
    
# print(word_count)


# word_count.get(word, 0) returns 0 if the word isn't present yet.


# from collections import defaultdict

# word_count = defaultdict(int)

# for word in words:
#     word_count[word] += 1  # 
# ✅ Safe — default is 0
