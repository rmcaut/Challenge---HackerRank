# Frequency sort with a tie-breaker: if multiple letters have the same count, 
# the alphabetical order should determine which ones are included in the top 3.


from collections import Counter

def top_three_letters(s):
    c = Counter(s)
    
    # Sort by frequency (descending) and then alphabetically
    sorted_items = sorted(c.items(), key=lambda item: (-item[1], item[0]))
    
    # Take top 3
    return sorted_items[:3]

# Example
s = "abracadabraddddfffffcccc"
result = top_three_letters(s)

print(result)
# Output: [('a', 5), ('b', 2), ('r', 2)]




# from collections import Counter

# a = ['c', 'b', 'c', 'a', 'b', 'a', 'b', 'b', 'c', 'c','c','a', 'b', 'a', 'c', 'a', 'd', 'd', 'd', 'd']
# counter_dict = Counter(a)
# ordered_count = counter_dict.most_common()

# first = str()
# second = str()  
# third = str()





