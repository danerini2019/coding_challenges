# Return column number from excel column name
import string
alphabet = list(string.ascii_lowercase)

def column_number(name):
    
    digit_name = [alphabet.index(letter)+1 for letter in name]
    
    column = 0

    for i in range(len(digit_name)):
        column += digit_name[-(i+1)] * (26**i)
    return column

print(column_number('sheet'))
print(column_number('dead'))
print(column_number('zz'))
print(column_number('vivinguyen'))

