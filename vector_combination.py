import itertools

# return a dict mapping from m -> list of all possible vector combinations
# where m is the length of the vectors
def find_vector_combinations_all_m(c, s, n) -> Dict[int, List[List[str]]:
    result = {}
    for _ in range(n+1):
        result[_] = []
    for i in range(2 ** n):
        digits = list(bin(i)[2:].zfill(n))  # zfill to front-pad with 0
        m = sum(map(lambda _: int(_), digits))
        digit_index = list(filter(lambda _: digits[_] == '1', range(n)))
        # print(digit_index)
        for k in range(2 ** m):
            # c_and_s is a list of m elements of 0s and 1s
            # 1 at position k means "the final vector has s_k"
            # 0 at position k means "the final vector has c_k"
            c_and_s = list((bin(k))[2:].zfill(m))  # zfill to front-pad with 0
            vec = list(map(lambda _: c[digit_index[_]] if c_and_s[_] == '0' else s[digit_index[_]], range(m)))
            result[m].append(vec)
    return result

def find_vector_combinations(c, s, n, m):
    result = {m: []}
    for digit_index in itertools.combinations(range(n), m):
        # digits is a list of indexes to be included in the final vector
        # if an index k appears, it means "the final vector includes c_k or s_k"
        # if an index k does not appear, it means "the final vector does NOT include c_k and s_k"
        # print(digit_index)
        for k in range(2 ** m):
            # c_and_s is a list of m elements of 0s and 1s
            # 1 at position k means "the final vector has s_k"
            # 0 at position k means "the final vector has c_k"
            c_and_s = list((bin(k))[2:].zfill(m))  # zfill to front-pad with 0
            vec = list(map(lambda _: c[digit_index[_]] if c_and_s[_] == '0' else s[digit_index[_]], range(m)))
            result[m].append(vec)
    return result

c = ["c0", "c1", "c2", "c3", "c4", "c5", "c6", "c7"]  # can provide more. n tells you to use the first n elements
s = ["s0", "s1", "s2", "s3", "s4", "s5", "s6", "s7"]
print(find_vector_combinations_all_m(n=6, c=c, s=s))
