#in this sample, I showed the use of different pre-defined functions in pythons
# instead of using if statements to check if each character is alphabetic character in the following lists
# uppercase = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
# lowercase = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

#you can use the function isapha() can check if character is alphabeta

# cipher
message = "attack"
key = 1
translated = ''

for symbol in message:
    if symbol.isalpha(): #check if alphabet
        num = ord(symbol)
        num += key

        if symbol.isupper(): # you can use # if symbol in uppercase: ...
            if num > ord('Z'): # use can use if symbol > 'Z' without converting symbol to number
                num -= 26
            elif num < ord('A'):
                num += 26
        elif symbol.islower(): # if symbol in lowercase: ....
            if num > ord('z'):
                num -= 26
            elif num < ord('a'):
                num += 26

        translated += chr(num)
    else:
        translated += symbol

print(translated)

# decipher
converted = ''

for symbol in translated:
    if symbol.isalpha():
        num = ord(symbol)
        num -= key

        if symbol.isupper():
            if num > ord('Z'):
                num -= 26
            elif num < ord('A'):
                num += 26
        elif symbol.islower():
            if num > ord('z'):
                num -= 26
            elif num < ord('a'):
                num += 26

        converted += chr(num)
    else:
        converted += symbol

print(converted)