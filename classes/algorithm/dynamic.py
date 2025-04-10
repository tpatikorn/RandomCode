import math

rod_price = {
    1: 1, 2: 5, 3: 8, 4: 9, 5: 10,
    6: 17, 7: 17, 8: 20, 9: 24, 10: 30
}

best_price = {}
best_cut = {}


def bottom_up(target):
    for this_length in range(1, target + 1):
        try:
            best_so_far = rod_price[this_length]
            this_best_cut = [this_length]
        except KeyError:
            best_so_far = 0
            this_best_cut = []

        for left_side in range(1, math.ceil((this_length + 1) / 2)):
            right_side = this_length - left_side
            this_price = best_price[left_side] + best_price[right_side]
            if this_price > best_so_far:
                best_so_far = this_price
                this_best_cut = best_cut[left_side] + best_cut[right_side]
        best_price[this_length] = best_so_far
        best_cut[this_length] = this_best_cut
    return best_price[target], best_cut[target]


def top_down(target):
    try:
        return best_price[target], best_cut[target]
    except KeyError:
        try:
            best_so_far = rod_price[target]
            this_best_cut = [target]
        except KeyError:
            best_so_far = 0
            this_best_cut = []

        for left_side in range(1, math.ceil((target + 1) / 2)):
            right_side = target - left_side
            best_price_left, best_cut_left = top_down(left_side)
            best_price_right, best_cut_right = top_down(right_side)

            this_price = best_price_left + best_price_right
            if this_price > best_so_far:
                best_so_far = this_price
                this_best_cut = best_cut_left + best_cut_right

        best_price[target] = best_so_far
        best_cut[target] = this_best_cut
        return best_price[target], best_cut[target]


if __name__ == "__main__":
    while True:
        input_number = int(input("rod length? "))
        print(top_down(input_number))
