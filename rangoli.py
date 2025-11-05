def print_rangoli(size):
    alph = list(map(chr, range(97, 123)))
    alph_lower = [c.lower() for c in alph]
    for rows_upper in range(0, size): 
        print('-'*2*(size - rows_upper - 1), end='')
        for l in range(size, size - rows_upper, -1):
            print(alph_lower[l - 1]+'-', end='')
        print(alph_lower[size - rows_upper -1], end='')
        for l in range(size - rows_upper + 1, size + 1):
            print('-'+alph_lower[l - 1], end='')
        print('-'*2*(size - rows_upper -1), end='')
        print()
    for rows_lower in range(size - 2, - 1, -1): 
        print('-'*2*(size - rows_lower - 1), end='')
        for l in range(size, size - rows_lower, -1):
            print(alph_lower[l - 1]+'-', end='')
        print(alph_lower[size - rows_lower -1], end='')
        for l in range(size - rows_lower + 1, size + 1):
            print('-'+alph_lower[l - 1], end='')
        print('-'*2*(size - rows_lower -1), end='')
        print() 
     
if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)