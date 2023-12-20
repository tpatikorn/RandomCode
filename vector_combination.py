import itertools

n = 6
m = 2
c = ["c0", "c1", "c2", "c3", "c4", "c5", "c6", "c7"]  # can provide more. n tells you to use the first n elements
s = ["s0", "s1", "s2", "s3", "s4", "s5", "s6", "s7"]

for digit_index in itertools.combinations(range(n), m):
    # digits is a list of indexes to be included in the final vector
    # if an index k appears, it means "the final vector includes c_k or s_k"
    # if an index k does not appear, it means "the final vector does NOT include c_k and s_k"
    print(digit_index)
    for k in range(2 ** m):
        # c_and_s is a list of m elements of 0s and 1s
        # 1 at position k means "the final vector has s_k"
        # 0 at position k means "the final vector has c_k"
        c_and_s = list((bin(k))[2:].zfill(m))  # zfill to front-pad with 0
        vec = list(map(lambda _: c[digit_index[_]] if c_and_s[_] == '0' else s[digit_index[_]], range(m)))
        print(vec)
