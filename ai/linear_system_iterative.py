#  jacobi
from typing import Callable, List


def jacobi(update_val: list[Callable[[list[float]], float]],
           tolerance: float = 1e-6, max_iter: int = 1000,
           initial_val: List[float] = None):
    if initial_val is None:
        current_val = [0] * len(update_val)
    elif len(update_val) != len(initial_val):
        raise RuntimeError("the length of update_val and initial_val must match")
    else:
        current_val = initial_val
    for i in range(max_iter):
        new_val = [fn(current_val) for fn in update_val]
        error = max([abs(old - new) for old, new in zip(new_val, current_val)])
        print(i, current_val, error)

        current_val = new_val
        if error < tolerance:
            break
    print(current_val)


jacobi([lambda vals: (8 - (1 * vals[1]) + (2 * vals[2])) / 4,
        lambda vals: (-4 - (2 * vals[0]) + (1 * vals[3])) / -4,
        lambda vals: (1 - (1 * vals[0]) + (1 * vals[1])) / 3,
        lambda vals: (5 - (1 * vals[2]) + (2 * vals[1])) / 3],
       tolerance=1e-9)
