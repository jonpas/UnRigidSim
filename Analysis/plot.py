#!/usr/bin/env python3

import sys
import matplotlib.pyplot as plt

# Object amount
objects = [0, 10, 100, 500, 1000, 5000]

# FPS [mode, low error, high error]
cubes = [
    [119, 119, 100, 35, 10, 6],
    [1,     2,  10, 15,  2, 2],
    [1,     1,  10,  5,  8, 1]
]
spheres = [
    [119, 119, 110, 95, 55, 10],
    [1,     2,   4,  5,  5,  2],
    [1,     1,   8,  5,  5,  5]
]
combined = [
    [119, 119, 115, 40, 12, 8],
    [1,     2,  10,  5,  2, 4],
    [1,     1,   3,  8,  4, 4]
]

plt.figure()
plt.errorbar(objects, cubes[0], yerr=[cubes[1], cubes[2]], label="Cubes", capsize=5.0)
plt.errorbar(objects, spheres[0], yerr=[spheres[1], spheres[2]], label="Spheres", capsize=5.0)
plt.errorbar(objects, combined[0], yerr=[combined[1], combined[2]], label="Combined 50/50", capsize=5.0)
plt.xlabel("Objects")
plt.ylabel("FPS")
plt.legend()

if "-p" in sys.argv:
    plt.show(block=True)
