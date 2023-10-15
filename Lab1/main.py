import math

print('******* 1 **********')
# 1.Find The greatest common divisor of multiple numbers read from the console.
numbers = []
user_input = int(input("Enter how many numbers do you want to enter: "))
for i in range(user_input):
    user_input = int(input("Enter number: "))
    numbers.append(user_input)

cmmdc = numbers[0]
for num in numbers[1:]:
    cmmdc = math.gcd(cmmdc, num)

print("Cel mai mare divizor comun al numerelor este:")
print(cmmdc)

print('******* 2 ***********')
# 2. Write a script that calculates how many vowels are in a string.

user_input = str(input("Enter a word to calculate how many vowels are "))
word = user_input
print(user_input)
vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
count = 0
for letter in word:
    if letter in vowels:
        count = count + 1
print(f'Cuvantul {word} contine {count} vocale')

print('******* 3 ***********')
# 3.Write a script that receives two strings
# and prints the number of occurrences of the first string in the second
count = 0
user_input = str(input("Enter a string:"))
string2 = user_input
user_input = str(input("Enter a string to find in the first string:"))
string1 = user_input
lgth = len(string1)
for i in range(len(string2) - lgth + 1):
    if string2[i:i + lgth] == string1:
        count = count + 1
print(f'Contine:{count}')

print('******* 4 ***********')

# 4.Write a script that converts a string of characters written in UpperCamelCase into lowercase_with_underscores.

stri = 'UpperCamelCase'
newstr = ''
pas = 0
for char in stri:
    pas = pas + 1
    if char.isupper():
        if pas == 1:
            newstr = char.lower()
        else:
            newstr += '_' + char.lower()
    else:
        newstr += char

print(newstr)

print('******* 5 ***********')

# 5.Given a square matrix of characters write a script that prints the string obtained
# by going through the matrix in spiral order (as in the example):
# firs      1  2  3  4    =>   first_python_lab
# n_lt      12 13 14 5
# oba_      11 16 15 6
# htyp      10 9  8  7

a = [['f', 'i', 'r', 's'], ['n', '_', 'l', 't'], ['o', 'b', 'a', '_'], ['h', 't', 'y', 'p']]
top, bottom, left, right = 0, len(a) - 1, 0, len(a[0]) - 1
result = ' '
while top <= bottom and left <= right:
    for i in range(left, right + 1):
        result += a[top][i]
    top += 1

    for i in range(top, bottom + 1):
        result += a[i][right]
    right -= 1

    if top <= bottom:
        for i in range(right, left - 1, -1):
            result += a[bottom][i]
        bottom -= 1

    if left <= right:
        for i in range(bottom, top - 1, -1):
            result += a[i][left]
        left += 1

print(result)

print('******* 6 ***********')

# 6.Write a function that validates if a number is a palindrome.
def palindrome(x):
    nr = x
    reverse = nr % 10
    nr = nr // 10
    while nr > 0:
        reverse = reverse * 10 + nr % 10
        nr = nr // 10
    if reverse == x:
        return True
    else:
        return False


print(palindrome(123213))
print(palindrome(123321))

print('******* 7 ***********')

# 7 Write a function that extract a number from a text (for example if the text is
# "An apple is 123 USD", this function will return 123, or if the text is "abc123abc"
# the function will extract 123).
# The function will extract only the first number that is found.

def find_first_number(strg):
    num_str = ""
    found_number = False

    for ch in strg:
        if ch.isdigit():
            num_str += ch
            found_number = True
        elif found_number:
            break

    if num_str:
        return int(num_str)
    else:
        return None


print(find_first_number("An apple is 123 USD"))
print(find_first_number("abc123abc4"))
print(find_first_number("No numbers here"))

print('******* 8 ***********')

# 8.Write a function that counts how many bits with value 1 a number has.
# For example for number 24, the binary format is 00011000, meaning 2 bits with value "1"

def number_of_bites_1(nr):
    count = 0
    while nr:
        if (nr % 2) == 1:
            count = count + 1
        nr = nr // 2
    return count


print(number_of_bites_1(24))

print('******* 9 ***********')

# 9.Write a functions that determine the most common letter in a string. For example if the
# string is "an apple is not a tomato", then the most common character is "a" (4 times).
# Only letters (A-Z or a-z) are to be considered.
# Casing should not be considered "A" and "a" represent the same character.
def most_comm_letter(strg):
    frecventa = {}
    for ch in strg:
        if ch.isalpha():
            if ch in frecventa:
                frecventa[ch] += 1
            else:
                frecventa[ch] = 1

    most_common = max(frecventa, key=frecventa.get)
    return most_common


print(most_comm_letter("An Apple is not A tomAto"))

print('******* 10 ***********')

# 10. Write a function that counts how many words exists in a text. A text is considered
# to be form out of words that are separated by only ONE space. For example: "I have Python exam" has 4 words.

def numbers_of_words(strg):
    count = strg.split(' ')
    return len(count)


print(numbers_of_words("I have Python exam"))


