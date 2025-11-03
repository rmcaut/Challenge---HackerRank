def classify_char(c):
    if c.isalpha():  # Checks if it's a letter [a-zA-Z]
        if c.lower() in 'aeiou':
            return 'vowel'
        else:
            return 'consonant'
    else:
        return 'not a letter'


print(classify_char('A'))  # 'vowel'



def max_string(idx):
    for in range()