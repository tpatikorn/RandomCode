import datetime
import math

from euler.util import fast_isqrt_check


def areas(side: int):
    results = []
    if fast_isqrt_check((3 * side + 1) * (side - 1)):
        area1 = (side + 1) * math.sqrt((3 * side + 1) * (side - 1)) / 4
        results.append((area1, side, 3*side + 1))
    if fast_isqrt_check((3 * side - 1) * (side + 1)):
        area2 = (side - 1) * math.sqrt((3 * side - 1) * (side + 1)) / 4
        results.append((area2, side, 3*side - 1))
    return results


# found pattern side = 4k + 1 where
# 1) the +1 track
#  C1 = 1
#  C2 = 16
#  C3 = 60
#  840
#  11,704
#  163,020
#  2,270,580
#  31,625,104
# C3 = C2 * 14 + 4 - C1
# the -1 track
#  C1 = 4
#  C2 = 60
#  C3 = 225
#  3,136
#  43,681
#  608,400
#  8,473,921
# C3 = (SQRT(C3) * 4 - SQRT(C1))^2

# so the final answer is the sum of  16
#  50
#  196
#  722
#  2,704
#  10,082
#  37,636
#  140,450
#  524,176
#  1,956,242
#  7,300,804
#  27,246,962
#  101,687,056
#  379,501,250
#  Sum = 518,408,346

