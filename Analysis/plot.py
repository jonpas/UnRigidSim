#!/usr/bin/env python3

import sys
import matplotlib.pyplot as plt

# Object amount
objects = [10, 100, 500, 1000, 5000]

# FPS
cubes = [100, 60, 30, 20, 10]
spheres = [90, 50,  25, 15, 8]
combined = [95, 55, 28, 19, 9]

plt.figure()
plt.plot(objects, cubes, label="Cubes")
plt.plot(objects, spheres, label="Spheres")
plt.plot(objects, combined, label="Combined")
plt.xlabel("Objects")
plt.ylabel("FPS")
plt.legend()

if "-p" in sys.argv:
    plt.show(block=True)
