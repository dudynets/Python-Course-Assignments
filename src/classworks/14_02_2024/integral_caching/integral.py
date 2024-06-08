import time
import numpy as np

class Integral:
    def __init__(self):
        self.cache = {}

    def calculate(self, func, a, b):
        # Create a key for the cache
        key = (str(func), a, b)

        # If the result is in the cache, return it
        if key in self.cache:
            return self.cache[key]

        # Otherwise, calculate the integral and store the result in the cache
        x = np.linspace(a, b, 1000)
        y = func(x)
        result = np.trapz(y, x)
        self.cache[key] = result

        return result

# Usage
integral = Integral()

# benchmark the performance
start = time.time()
for _ in range(10000000):
    integral.calculate(np.sin, 0, np.pi)
print(time.time() - start)

start = time.time()
for _ in range(10000000):
    integral.calculate(np.sin, 0, np.pi)
print(time.time() - start)
