import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure()
ax = plt.axes(projection='3d')

#The distances are calculated from origin in 3 dimensional space

x_domain = 20
y_domain = 20

def euclidean_distance(x,y,z,dimension=3):
    point_b = [x,y,z]
    distance_squared_sum = 0
    for n in range(dimension):
        distance_squared_sum += abs(point_b[n])**2
    return distance_squared_sum**0.5

def manhattan_distance(x,y,z,dimension=3):
    point_b = [x,y,z]
    distance_sum = 0
    for n in range(dimension):
        distance_sum += abs(point_b[n])
    return distance_sum

def minkowski_distance(x,y,z,p,dimensions=3):
    point_b = [x,y,z]
    minkowski_distance_sum = 0
    for n in range(dimensions):
        minkowski_distance_sum += abs(point_b[n]**p)
    return minkowski_distance_sum**(1/p)

# print(euclidean_distance(1,1,0))
# print(manhattan_distance(14,14,0))
# print(str(minkowski_distance(1,1,0,2))+' Minkowski E')
# print(str(minkowski_distance(14,14,0,1))+' Minkowski M')

# #Euclidean Distance
# x = np.linspace(0, x_domain)
# y = np.linspace(0, y_domain)
# z = euclidean_distance(x,y,0)
# ax.plot3D(x,y,z,'green')
#
# #Manhattan Distance
# x1 = np.linspace(0, x_domain)
# y1 = np.linspace(0, y_domain)
# z1 = manhattan_distance(x1,y1,0)
# ax.plot3D(x1,y1,z1,'red')
#
# #Chebyshev Distance (Minkowski Limit Implementation)
# x2 = np.linspace(0, x_domain)
# y2 = np.linspace(0, y_domain)
# z2 = minkowski_distance(x2,y2,0,100)
# ax.plot3D(x2,y2,z2,'blue')
#
# #Minkowski Distance (2**-2)
# x3 = np.linspace(0, x_domain)
# y3 = np.linspace(0, y_domain)
# z3 = minkowski_distance(x3,y3,0,0.25)
# ax.plot3D(x3,y3,z3,'black')
#
# #Minkowski Distance (2**-1)
# x4 = np.linspace(0, x_domain)
# y4 = np.linspace(0, y_domain)
# z4 = minkowski_distance(x4,y4,0,0.5)
# ax.plot3D(x4,y4,z4,'purple')
#
# ax.set_xlabel('X Coordinate')
# ax.set_ylabel('Y Coordinate')
# ax.set_zlabel('Distance')
#
# p_order_1 = mpatches.Patch(color='black',label='p = 0.25')
# p_order_2 = mpatches.Patch(color='purple',label='p = 0.50')
# p_order_3 = mpatches.Patch(color='red',label='p = 1.00')
# p_order_4 = mpatches.Patch(color='green',label='p = 2.00')
# p_order_5 = mpatches.Patch(color='blue',label='p = ∞')
# plt.legend(handles=[p_order_1,p_order_2,p_order_3,p_order_4,p_order_5])

#Euclidean Space
for x in range(-x_domain,x_domain):
    for y in range(-y_domain, y_domain):
        ax.scatter(x, y, minkowski_distance(x, y, 0, 5), cmap ='viridis', edgecolor ='green', color='purple')

ax.set_xlabel('X Coordinate')
ax.set_ylabel('Y Coordinate')
ax.set_zlabel('Distance')

ax.set_title('P=10 Minkowski Distance')

plt.show()
