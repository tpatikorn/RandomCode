# can be easily solved using log rule and excel. So I'm going to golf this
# log (base^exp) = exp * log(base)
from math import log

from euler.util import get_euler_data_filepath

with open(get_euler_data_filepath("p099_largest_exponential.txt")) as f:
    log_values = [int(line.split(",")[1]) * log(int(line.split(",")[0])) for line in f]
    print(sorted(range(1, 1001), key=lambda _: log_values[_ - 1], reverse=True)[0])
