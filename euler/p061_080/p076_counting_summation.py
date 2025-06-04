from euler.util import count_partition

# this function include the sum of 1 number (for convenience of calculation)
# the question ask for sum of at least 2 numbers, so subtract 1 from the answer
print(count_partition(100) - 1)
