import numpy as np 
import itertools as it
from matplotlib import pyplot as plt

def gen_pop(n, size=6):
    return np.random.choice([0,1], (n,size))

def to_ternary(arr, size=6):
    out = 0
    for i, el in enumerate(arr):
        out += el*3**(size-i-1)
    return out

def count_schemas(pop, size=6):
    schemas = np.zeros((3**size))
    for el in pop:
        for mask in it.product([0, 2], repeat=size):
            schemas[to_ternary(np.maximum(el, mask), size=size)] = 1
    return int(sum(schemas))

plot_axis_6 = []
plot_data_6 = []

for n in range(1,100):
    schemas = 0
    for _ in range(10):
        schemas += count_schemas(gen_pop(n))
    plot_axis_6.append(n)
    plot_data_6.append(schemas/10)
    print(n)

for n in range(100,300,10):
    schemas = 0
    for _ in range(10):
        schemas += count_schemas(gen_pop(n))
    plot_axis_6.append(n)
    plot_data_6.append(schemas/10)
    print(n)

for n in range(300,500,50):
    schemas = 0
    for _ in range(10):
        schemas += count_schemas(gen_pop(n))
    plot_axis_6.append(n)
    plot_data_6.append(schemas/10)
    print(n)

for n in range(500,1001,100):
    schemas = 0
    for _ in range(10):
        schemas += count_schemas(gen_pop(n))
    plot_axis_6.append(n)
    plot_data_6.append(schemas/10)
    print(n)

plt.plot(plot_axis_6, plot_data_6)
# plt.show()

# plot_axis_15 = []
# plot_data_15 = []

# for n in range(1,100):
#     schemas = 0
#     for _ in range(10):
#         schemas += count_schemas(gen_pop(n, size=15), size=15)
#     plot_axis_15.append(n)
#     plot_data_15.append(schemas/10)
#     print(n)

# for n in range(100,300,10):
#     schemas = 0
#     for _ in range(10):
#         schemas += count_schemas(gen_pop(n, size=15), size=15)
#     plot_axis_15.append(n)
#     plot_data_15.append(schemas/10)
#     print(n)

# for n in range(300,500,50):
#     schemas = 0
#     for _ in range(10):
#         schemas += count_schemas(gen_pop(n, size=15), size=15)
#     plot_axis_15.append(n)
#     plot_data_15.append(schemas/10)
#     print(n)

# for n in range(500,1001,100):
#     schemas = 0
#     for _ in range(10):
#         schemas += count_schemas(gen_pop(n, size=15), size=15)
#     plot_axis_15.append(n)
#     plot_data_15.append(schemas/10)
#     print(n)

# plt.plot(plot_axis_15, plot_data_15)
plt.show()