from math import ceil

n_max = 1_000_000

divisor_sums = [-_ for _ in range(n_max)]

for divisor in range(1, n_max):
    for mult in range(1, ceil(n_max / divisor)):
        divisor_sums[divisor * mult] += divisor

print(divisor_sums)

# longest chain was 29 elt, so cut the loop early lol
for i in range(1, n_max):
    current = divisor_sums[i]
    chain = [str(i)]
    for _ in range(40):
        chain.append(str(current))
        if current >= n_max:
            # print("exceeded!", " -> ".join(chain))
            break
        elif current == i:
            if len(chain) > 20:
                print("amicable!", " -> ".join(chain))
            break
        else:
            current = divisor_sums[current]
