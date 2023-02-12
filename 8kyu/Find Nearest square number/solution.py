import math

def nearest_sq(n):
    root = int(math.sqrt(n))
    if abs(root ** 2 - n) < (root + 1) ** 2 - n:
        return root ** 2
    else:
        return (root + 1) ** 2
        