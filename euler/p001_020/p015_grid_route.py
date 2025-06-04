# the number of routes are (h + w)! / (h! * w!)
# where h and w are the height and width of the grid
# because you can think of it as the path
# path has to compose of
# going down: h times
# going right: w times
# the number of different ways you can arrange them are (h+w)!
# but all the "going downs" are the same, each "same" setting can have duplicate h! mutations
# but all the "going right" are the same, each "same" setting can have duplicate w! mutations
# so, the number of routes are (h + w)! / (h! * w!)

import math

w = 20
h = 20
print(math.factorial(h + w) / (math.factorial(20) * math.factorial(20)))
