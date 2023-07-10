
import math

outer_radius = 10
middle_radius = 5
inner_radius = 1

def score(x, y):
    distance_from_origin = math.sqrt(x**2 + y**2)
    if distance_from_origin > outer_radius:
        return 0
    elif distance_from_origin > middle_radius:
        return 1
    elif distance_from_origin > inner_radius:
        return 5
    else:
        return 10
