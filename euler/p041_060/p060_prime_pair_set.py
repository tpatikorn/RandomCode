from euler.util import is_probable_prime, get_prime_list

prime_list = get_prime_list(limit=10_000)

list1 = prime_list
list2 = []
list3 = []
list4 = []


def check_concat_prime(prime1, prime2):
    return is_probable_prime(int(str(prime1) + str(prime2))) and is_probable_prime(int(str(prime2) + str(prime1)))


print("list1", len(list1))

for i in range(len(list1)):
    for j in range(i + 1, len(list1)):
        p, q = list1[i], list1[j]
        if check_concat_prime(p, q):
            if {p, q} not in list2:
                list2.append({p, q})
print("list2", len(list2))

for i in range(len(list2)):
    for j in range(i + 1, len(list2)):
        s1, s2 = list2[i], list2[j]
        if len(s1.intersection(s2)) == 1:
            if check_concat_prime(list(s1 - s2)[0], list(s2 - s1)[0]):
                if s1.union(s2) not in list3:
                    list3.append(s1.union(s2))
print("list3", len(list3))

for i in range(len(list3)):
    for j in range(i + 1, len(list3)):
        s1, s2 = list3[i], list3[j]
        if len(s1.intersection(s2)) == 2:
            if check_concat_prime(list(s1 - s2)[0], list(s2 - s1)[0]):
                if s1.union(s2) not in list4:
                    list4.append(s1.union(s2))
print("list4", len(list4))

for i in range(len(list4)):
    for j in range(i + 1, len(list4)):
        s1, s2 = list4[i], list4[j]
        if len(s1.intersection(s2)) == 3:
            if check_concat_prime(list(s1 - s2)[0], list(s2 - s1)[0]):
                print("list5:", s1.union(s2))
