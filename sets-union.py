# This is to count each element just once usign s1.union(s2)

if __name__  == '__main__':
    n = input()
    english_roll_str = input()
    english_roll_list = english_roll_str.split(' ')
    english_roll_set = {int(roll) for roll in english_roll_list}
    #print(english_roll_set)
    
    b = input('')
    french_roll_str = input()
    french_roll_list = french_roll_str.split(' ')
    french_roll_set = {int(roll) for roll in french_roll_list}
    #print(french_roll_set)
    
    union = french_roll_set.union(english_roll_set)
    print(len(union))
