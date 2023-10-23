
import argparse
# 1.      Write a function to return a list of the first n numbers in the Fibonacci string.


print("------------------------1------------------------------")

def return_fibbonaci(n):
    s = []
    if n == 1:
        s.append(1)
        return s
    elif n == 2:
        s.append(1)
        s.append(1)
        return s
    else:
        s = [1, 1]
        for i in range(2, n):
            s.append(s[i - 2] + s[i - 1])
    return s

print(return_fibbonaci(16))

print("------------------------2------------------------------")
#  2. Write a function that receives a list of numbers and returns a list of the prime numbers found in it.

def prime(x):
    for i in (2, x-1):
        if x % i == 0:
            return False
    return True

def prime_numbers(s):
    return_s = []
    for number in s:
        if(number == 2):
          return_s.append(2)
        else:
            if prime(number) != True:
                continue
            else:
                return_s.append(number)
    return return_s

print(prime_numbers([2,3,5,6,4,7,8,9,10,11]))

print("------------------------3------------------------------")

#3.    3. Write a function that receives as parameters two lists a and b and returns:
# (a intersected with b, a reunited with b, a - b, b - a)


def operations(a, b):
    print(f"a= {a}")
    print(f"b= {b}")
    union = a+b
    intersection = [i for i in a if i in b]
    diff_ab = [i for i in a if i not in b]
    diff_ba = [i for i in b if i not in a]
    return union, intersection, diff_ab, diff_ba

ex3 = operations([1,2,3], [2,3,4])
print(f"uniunea : {ex3[0]}, intersectia : {ex3[1]}, diferenta a-b {ex3[2]}, diferenta b-a {ex3[3]}")

print("------------------------4------------------------------")

#4.   4. Write a function that receives as a parameters a list of musical notes (strings),
# a list of moves (integers) and a start position (integer). The function will return the
# song composed by going though the musical notes beginning with the start position and following
# the moves given as parameter.
# Example : compose(["do", "re", "mi", "fa", "sol"], [1, -3, 4, 2], 2)
# will return ["mi", "fa", "do", "sol", "re"]

def compose(notes, positions, start_position):
    song = []
    position = start_position
    song.append(notes[position])
    for i in positions:
        position = (position + i) % len(notes)
        song.append(notes[position])
    return song

print(compose(["do", "re", "mi", "fa", "sol"], [1, -3, 4, 2], 2))

print("------------------------5------------------------------")

#Write a function that receives as parameter a matrix and will return
#the matrix obtained by replacing all the elements under the main diagonal with 0 (zero).

def replace_with_0(matrix):
    matrix_update = matrix
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if i > j:
                matrix_update[i][j] = 0
    return matrix_update

print(replace_with_0([[1,2,3],[4,5,6],[7,8,9]]))

print("------------------------6------------------------------")
#6. Write a function that receives as a parameter a variable number of lists and a whole number x.
# Return a list containing the items that appear exactly x times in the incoming lists.

def x_time (x, *lists):
    return_list = []
    dict = {}
    for list in lists:
        for item in list:
            if(item in dict):
                dict[item] += 1
            else:
                dict[item] = 1
    for key in dict:
        if dict[key] == x:
            return_list.append(key)
    return return_list

print(x_time( 2,[1,2,3], [2,3,4],[4,5,6], [4,1, "test"]))

print("------------------------7------------------------------")

#7.Write a function that receives as parameter a list of numbers (integers) and will return a tuple with 2 elements.
# The first element of the tuple will be the number of palindrome numbers found in the list and the second
# element will be the greatest palindrome number.

def palindrome(x):
    nr = x
    reverse = nr % 10
    nr = nr // 10
    while nr > 0:
        reverse = reverse * 10 + nr % 10
        nr = nr // 10
    return reverse == x


def palindroms(list):
    list_palindroms = [item for item in list if palindrome(item)]
    max_val = max(list_palindroms)
    if not list_palindroms:
        return (0, None)
    return (len(list_palindroms),max_val)

print(palindroms([1,3,6,10,22,23,4567654,678755,6,987]))

print("------------------------8------------------------------")

#8.Write a function that receives a number x, default value equal to 1, a list of strings,
# and a boolean flag set to True. For each string, generate a list containing the characters that have
# the ASCII code divisible by x if the flag is set to True, otherwise it should contain characters
# that have the ASCII code not divisible by x.

def ascii( list, x=1, flag= True ):
    return_list = []
    for item in list:
        ch_list = []
        for ch in item:
            if (ord(ch) % x == 0) == flag:
                ch_list.append(ch)
        return_list.append(ch_list)
    return return_list

print(ascii(["test", "hello", "lab002"],x=2, flag = False ))



print("------------------------9------------------------------")

#9 Write a function that receives as paramer a matrix which
# represents the heights of the spectators in a stadium and will return a list of tuples (line, column)
# each one representing a seat of a spectator which can't see the game.
# A spectator can't see the game if there is at least one taller spectator standing in front of him.
# All the seats are occupied. All the seats are at the same level.
# Row and column indexing starts from 0, beginning with the closest row from the field.

def spectators(matrix):
    position = []
    for j in range(len(matrix[0])):
        for i in range(len(matrix)):
            for k in range(i+1, len(matrix)):
                if matrix[k][j] <= matrix[i][j]:
                    if (k, j) not in position:
                        position.append((k, j))
    return position



print(spectators([[1, 2, 3, 2, 1, 1],
                 [2, 4, 4, 3, 7, 2],
                 [5, 5, 2, 5, 6, 4],
                 [6, 6, 7, 6, 7, 5]]))
print("------------------------10------------------------------")

#10. Write a function that receives a variable number of lists and returns a list of tuples as follows:
# the first tuple contains the first items in the lists, the second element contains the items on the position
# 2 in the lists, etc. Ex: for lists [1,2,3], [5,6,7], ["a", "b", "c"]
# return: [(1, 5, "a ") ,(2, 6, "b"), (3,7, "c")].

def ex10(*lists):
    return_list = []
    for i in range(max([len(x) for x in lists])):
        new_tuple = tuple(list[i] if i < len(list) else None for list in lists)
        return_list.append(new_tuple)
    return return_list

print(ex10([1,2,3], [5,6,7,8], ["a", "b", "c"]))

print("------------------------11------------------------------")

#11. Write a function that will order a list of string tuples based on the 3rd
# character of the 2nd element in the tuple.
# Example: ('abc', 'bcd'), ('abc', 'zza')] ==> [('abc', 'zza'), ('abc', 'bcd')]

def order_strings(list):
    return_list = sorted(list, key = lambda li: li[1][2])
    return return_list

print(order_strings([('abc', 'bcd'), ('abc', 'zza')]))

print("------------------------12------------------------------")

#12.Write a function that will receive a list of words  as parameter and will return a list of lists of words,
# grouped by rhyme. Two words rhyme if both of them end with the same 2 letters.

def group_by_rhyme(words):
    sorted_words = sorted(words, key = lambda word: word[-2:])
    rhymes = []
    last_rhyme = sorted_words[0][-2:]
    r = [sorted_words[0]]
    print(sorted_words)
    for i in range(1, len(sorted_words)):
        if sorted_words[i][-2:] == last_rhyme:
            r.append(sorted_words[i])
        else:
            rhymes.append(r)
            r = [sorted_words[i]]
            last_rhyme = sorted_words[i][-2:]

    rhymes.append(r)
    return(rhymes)

word_list = ['ana', 'banana', 'carte', 'arme', 'parte']
result = group_by_rhyme(word_list)
print(result)


