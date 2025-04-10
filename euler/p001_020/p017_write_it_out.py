import math

spelled = {1: "one", 2: "two", 3: "three", 4: "four", 5: "five",
           6: "six", 7: "seven", 8: "eight", 9: "nine", 10: "ten",
           11: "eleven", 12: "twelve", 13: "thirteen", 14: "fourteen", 15: "fifteen",
           16: "sixteen", 17: "seventeen", 18: "eighteen", 19: "nineteen"}
spelled_ty = {2: "twenty", 3: "thirty", 4: "forty", 5: "fifty", 6: "sixty", 7: "seventy", 8: "eighty", 9: "ninety"}


def write_it_out(num):
    try:
        return spelled[num]
    except KeyError:
        if num >= 1000:
            word = spelled[math.floor(num / 1000)] + " thousand"
            if num % 1000 > 0 and num % 100 == 0:
                word = word + " and " + write_it_out(num % 1000)
            elif num % 1000 > 0 and num % 100 > 0:
                word = word + " " + write_it_out(num % 1000)
        elif num >= 100:
            word = spelled[math.floor(num / 100)] + " hundred"
            if num % 100 > 0:
                word = word + " and " + write_it_out(num % 100)
            else:
                word = word
        else:
            word = spelled_ty[math.floor(num / 10)]
            if num % 10 > 0:
                word = word + " " + write_it_out(num % 10)
        spelled[num] = word
        return word


total = 0
for i in range(1, 1001):
    s = write_it_out(i)
    print(i, s)
    total = total + len(s.replace(" ", ""))
print(total)
