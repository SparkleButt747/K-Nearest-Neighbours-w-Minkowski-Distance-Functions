def euclidean_distance(point_a,point_b):
    if len(point_a)!=len(point_b):
        raise ValueError("Dimension Mismatch")
    distance_squared_sum = 0
    for n in range(len(point_b)):
        if point_a[n]>point_b[n]:
            distance_squared_sum += (abs(point_a[n]-point_b[n]))**2
        else:
            distance_squared_sum += (abs(point_b[n]-point_a[n]))**2
    return distance_squared_sum**0.5

def euclidean_distance_old(x,y,z,dimension=3):
    point_b = [x,y,z]
    distance_squared_sum = 0
    for n in range(dimension):
        distance_squared_sum += abs(point_b[n])**2
    return distance_squared_sum**0.5

def manhattan_distance(point_a,point_b):
    if len(point_a)!=len(point_b):
        raise ValueError("Dimension Mismatch")
    distance_sum = 0
    for n in range(len(point_b)):
        if point_a[n]>point_b[n]:
            distance_sum += abs(point_a[n]-point_b[n])
        else:
            distance_sum += abs(point_b[n]-point_a[n])
    return distance_sum

def manhattan_distance_old(x,y,z,dimension=3):
    point_b = [x,y,z]
    distance_sum = 0
    for n in range(dimension):
        distance_sum += abs(point_b[n])
    return distance_sum

def minkowski_distance(point_a,point_b,p):
    if len(point_a)!=len(point_b):
        raise ValueError("Dimension Mismatch")
    minkowski_distance_sum = 0
    for n in range(len(point_b)):
        if point_a[n]>point_b[n]:
            minkowski_distance_sum += (abs(point_a[n]-point_b[n])**p)
        else:
            minkowski_distance_sum += (abs(point_b[n] - point_a[n]) ** p)
    return minkowski_distance_sum**(1/p)

def minkowski_distance_old(x,y,z,p,dimensions=3):
    point_b = [x,y,z]
    minkowski_distance_sum = 0
    for n in range(dimensions):
        minkowski_distance_sum += abs(point_b[n]**p)
    return minkowski_distance_sum**(1/p)

def chebyshev_distance(point_a,point_b):
    if len(point_a)!=len(point_b):
        raise ValueError("Dimension Mismatch")
    chebyshev_distance_sum = 0
    for n in range(len(point_b)):
        if point_a[n]>point_b[n]:
            chebyshev_distance_sum += (abs(point_a[n]-point_b[n])**100)
        else:
            chebyshev_distance_sum += (abs(point_b[n] - point_a[n]) ** 100)
    return chebyshev_distance_sum**(1/100)