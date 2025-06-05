# I = 1
# V = 5
# X = 10
# L = 50
# C = 100
# D = 500
# M = 1000
# Only one I, X, and C can be used as the leading numeral in part of a subtractive pair.
# I can only be placed before V and X.
# X can only be placed before L and C.
# C can only be placed before D and M.
def number_to_roman(n):
    roman = ""
    while n >= 1000:
        roman = roman + "M"
        n -= 1000
    if n >= 900:
        roman = roman + "CM"
        n -= 900
    if n >= 500:
        roman = roman + "D"
        n -= 500
    if n >= 400:
        roman = roman + "CD"
        n -= 400

    while n >= 100:
        roman = roman + "C"
        n -= 100
    if n >= 90:
        roman = roman + "XC"
        n -= 90
    if n >= 50:
        roman = roman + "L"
        n -= 50
    if n >= 40:
        roman = roman + "XL"
        n -= 40

    while n >= 10:
        roman = roman + "X"
        n -= 10
    if n >= 9:
        roman = roman + "IX"
        n -= 9
    if n >= 5:
        roman = roman + "V"
        n -= 5
    if n >= 4:
        roman = roman + "IV"
        n -= 4

    while n >= 1:
        roman = roman + "I"
        n -= 1

    return roman


# assume valid
def roman_to_number(roman):
    number = 0
    roman = roman + "_"
    while roman[0] == "M":
        number += 1000
        roman = roman[1:]
    if roman[0:2] == "CM":
        number += 900
        roman = roman[2:]
    if roman[0] == "D":
        number += 500
        roman = roman[1:]
    if roman[0:2] == "CD":
        number += 400
        roman = roman[2:]

    while roman[0] == "C":
        number += 100
        roman = roman[1:]
    if roman[0:2] == "XC":
        number += 90
        roman = roman[2:]
    if roman[0] == "L":
        number += 50
        roman = roman[1:]
    if roman[0:2] == "XL":
        number += 40
        roman = roman[2:]

    while roman[0] == "X":
        number += 10
        roman = roman[1:]
    if roman[0:2] == "IX":
        number += 9
        roman = roman[2:]
    if roman[0] == "V":
        number += 5
        roman = roman[1:]
    if roman[0:2] == "IV":
        number += 4
        roman = roman[2:]

    while roman[0] == "I":
        number += 1
        roman = roman[1:]

    return number


from euler.util import get_euler_data_filepath

with open(get_euler_data_filepath(filename="p089_roman.txt")) as data:
    char_diff = 0
    for line in data.readlines():
        line = line.strip()
        number = roman_to_number(line)
        best_roman = number_to_roman(number)
        print(line, best_roman, len(line), len(best_roman))
        char_diff += len(line) - len(best_roman)
    print(char_diff)
