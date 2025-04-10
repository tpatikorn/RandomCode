from collections import Counter
from euler import util

diff = 3330
for i in range(1001, 10000 - 2 * diff, 2):
    if Counter(list(str(i))) == Counter(list(str(i + diff))) == Counter(list(str(i + diff + diff))):
        if util.is_prime(i) and util.is_prime(i + diff) and util.is_prime(i + diff + diff):
            print(i, i + diff, i + 2 * diff, sep="")