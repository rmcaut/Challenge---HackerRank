# Generate an alphabet list
# alph = list(map(chr, range(97, 123)))
# for c in alph:
#     print(c.lower(), end='')


# open a file to write results from function
import os
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    s = input()
    result = myfunction(s)
    fptr.write(result + '\n')
    fptr.close()


#