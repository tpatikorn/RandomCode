from itertools import permutations


class NGon:
    def __init__(self, n):
        self.n = n
        self.inner = [-1 for _ in range(n)]
        self.outer = [-1 for _ in range(n)]

    def get_sum(self, i):
        return self.inner[i] + self.inner[i + 1 - self.n] + self.outer[i]

    def iterate(self):
        index_min_outer = self.outer.index(min(self.outer))
        self.inner = self.inner[index_min_outer:] + self.inner[:index_min_outer]
        self.outer = self.outer[index_min_outer:] + self.outer[:index_min_outer]
        result = ""
        for i in range(self.n):
            result += str(self.outer[i]) + str(self.inner[i]) + str(self.inner[i + 1 - self.n])
        return result

    def summary(self):
        return self.n, self.iterate(), [self.get_sum(_) for _ in range(self.n)]

    def __repr__(self):
        return f"n {self.n}, {self.iterate()} sum {[self.get_sum(_) for _ in range(self.n)]}"


N = 5
gon = NGon(N)

known = []
max_iterate = 0
for perm in permutations(range(1, N * 2 + 1)):
    gon.inner = perm[:N]
    gon.outer = perm[N:]
    gon_sum = gon.get_sum(0)
    good = True
    for _ in range(1, N):
        if gon_sum != gon.get_sum(_):
            good = False
            break
    if good:
        it = gon.iterate()
        if it not in known:
            print(gon)
            known.append(it)
            if len(it) == 16 and int(it) > max_iterate:
                print(">>>", it)
                max_iterate = int(it)
