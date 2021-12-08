import string
import random

lowercaseAlphabets = list(string.ascii_lowercase)
random.shuffle(lowercaseAlphabets)

uppercaseAlphabets = list(string.ascii_uppercase)
random.shuffle(uppercaseAlphabets)

numbers = list(string.digits)
random.shuffle(numbers)

specialChar = list(string.punctuation)
random.shuffle(specialChar)

if __name__ == "__main__":

    length = int(input('Length:'))

    passwordList = []
    upperIndex = 0
    lowerIndex = 0
    numberIndex = 0
    charIndex = 0

    while True:
        passwordList.extend(uppercaseAlphabets[upperIndex])
        passwordList.extend(lowercaseAlphabets[lowerIndex])
        passwordList.extend(numbers[numberIndex])
        passwordList.extend(specialChar[charIndex])

        if upperIndex == 25:
            upperIndex = 0
        else:
            upperIndex += 1

        if lowerIndex == 25:
            lowerIndex = 0
        else:
            lowerIndex += 1

        if numberIndex == 9:
            numberIndex = 0
        elif numberIndex != 9:
            numberIndex += 1

        if charIndex == 31:
            charIndex = 0
        elif charIndex != 31:
            charIndex += 1

        if len(passwordList) > length:
            break
random.shuffle(passwordList)
password = (''.join(passwordList[0:length]))
print('Your Password is',password)
save = input('Save(y/n):')
if save == 'y':
    file = open('Passwords.txt', 'a')
    name = input('Name:')
    file.write(f'{name} = {password}\n')
    file.close()
else:
    pass