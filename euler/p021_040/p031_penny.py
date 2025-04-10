from math import ceil


def find_way_coin(pennies, coins):
    num_ways = 0
    for c in range(0, ceil(pennies / coins[0]) + 1):
        leftover = pennies - c * coins[0]
        if leftover < 0:
            break
        elif leftover == 0:
            num_ways = num_ways + 1
            break
        elif coins[0] == 1:
            return 1
        else:
            num_ways = num_ways + find_way_coin(leftover, coins[1:])
    return num_ways


print(find_way_coin(200, [200, 100, 50, 20, 10, 5, 2, 1]))
