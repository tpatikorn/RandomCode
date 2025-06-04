import random
from math import sqrt, sin, cos

random.seed(912)


def target_function(x_val):
    return (x_val * x_val + +2 * x_val + 2) * (-0.4 * x_val * x_val - 0.1 * x_val + 10)


def bonus_function(x_val):
    return (sqrt(abs(1 / (150 + x_val)))) * (2 / (x_val + 420) ** 2) * (sin(x_val / 4)) * 4 ** (cos(x_val / 3))


x_min = -50
x_max = 50
step_size_max = 5
step_size_min = 0.001
step_reduce = 1.0005
step_reduce_every = 1

for x in [_ / 10 for _ in range(x_min * 10, x_max * 10, 1)]:
    # print(x, target_function(x))
    pass

# hill climbing
initial_state = 3
count_global = 0
count_local = 0
step_global = 0
step_local = 0
for i in range(0, 100):
    initial_state = random.random() * (x_max - x_min) + x_min
    current_state = initial_state
    step_count = 0
    step_size = step_size_max
    while True:
        changed = False
        new_states = [current_state - step_size, current_state - step_size / 2,
                      current_state + step_size, current_state + step_size / 2]
        best_new_state = current_state
        best_new_value = -999999999
        for s in new_states:
            if x_min <= s <= x_max and target_function(s) > best_new_value:
                best_new_state = s
                best_new_value = target_function(s)
        # print(*list(map(target_function, new_states)))
        if abs(best_new_value - target_function(current_state)) > 0.0001:
            # print(step_count, step_size, current_state, target_function(current_state), best_new_value)
            current_state = best_new_state
            step_count = step_count + 1
            if step_count % step_reduce_every == 0 and step_size > step_size_min:
                step_size = step_size / step_reduce
        else:
            print(step_count, current_state, target_function(current_state))
            break
    if 3 < current_state < 3.2:
        count_global = count_global + 1
        step_global = step_global + step_count
    if -3.9 < current_state < -3.7:
        count_local = count_local + 1
        step_local = step_local + step_count
print(count_global, step_global / count_global)
if count_local > 0:
    print(count_local, step_local / count_local)
else:
    print(0, 0)
