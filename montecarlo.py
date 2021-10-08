import math
import numpy as np
from numpy import random

N_in = 0
N_out = 0
N = 2000  # 試行回数
ran_x = random.rand(N)  # Xの乱数
ran_y = random.rand(N)  # Yの乱数
ran_point = np.hypot(ran_x, ran_y)  # X^2 + Y^2の平方根

for i in ran_point:
    if i <= 1:
        N_in += 1
    else:
        N_out += 1

Pie = N_in / N * 4  # パイの近似式

print("IN: {} ".format(N_in))
print("OUT: {} ".format(N_out))
print("ALL: {} ".format(N))

print("Pi: {} ".format(Pie))
