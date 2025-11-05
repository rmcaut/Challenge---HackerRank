# Generate an alphabet list
# alph = list(map(chr, range(97, 123)))
# for c in alph:
#     print(c.lower(), end='')

# Rangoli
def print_rangoli(size):
    alph = list(map(chr, range(97, 123)))
    alph_lower = [c.lower() for c in alph]
    for rows_upper in range(1, size - 1): 
        print('-'*2*(size - rows_upper), end='')
        for l in range(1, rows_upper):
            print(alph_lower[size - l]+'-', end='')
        
     
if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
