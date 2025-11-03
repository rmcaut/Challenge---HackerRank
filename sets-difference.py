if __name__  == '__main__':
    n = int(input())
    english_roll_set = set(map(int, input().split()))
    print(english_roll_set)

    b= int(input())
    french_roll_set = set(map(int, input().split()))
    print(french_roll_set)

    difference = english_roll_set.difference(french_roll_set)

    print(difference)