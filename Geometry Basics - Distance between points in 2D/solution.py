import math

def distance_between_points(a, b):
    x_diff = a.x - b.x
    y_diff = a.y - b.y
    return math.sqrt(x_diff**2 + y_diff**2)
