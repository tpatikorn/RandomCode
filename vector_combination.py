n = 6
m = 3
c = ["c0", "c1", "c2", "c3", "c4", "c5", "c6", "c7"]  # can provide more. n tells you to use the first n elements
s = ["s0", "s1", "s2", "s3", "s4", "s5", "s6", "s7"]

for i in range(2 ** n):
    # digits is a list of n elements of 0s and 1s
    # 1 at position k means "this list includes c_k or s_k"
    # 0 at position k means "this list does NOT include c_k or s_k"
    digits = list(bin(i)[2:].zfill(n))  # zfill to front-pad with 0
    # only want cases where there are exactly m elements from c and s
    if sum(map(lambda _: int(_), digits)) == m:
        # convert digits (0s and 1s) into indexes (e.g. 11010 -> [0,1,3]
        digit_index = list(filter(lambda _: digits[_] == '1', range(n)))
        print(digit_index)
        for k in range(2 ** m):
            # c_and_s is a list of m elements of 0s and 1s
            # 1 at position k means "the final vector has s_k"
            # 0 at position k means "the final vector has c_k"
            c_and_s = list((bin(k))[2:].zfill(m))  # zfill to front-pad with 0
            vec = list(map(lambda _: c[digit_index[_]] if c_and_s[_] == '0' else s[digit_index[_]], range(m)))
            print(vec)
