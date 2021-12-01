import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d

fig = plt.figure()

# ax = plt.axes(projection='3d')

k_value = np.load("k_value.npy")
p_order = np.load("p_order.npy")
model_acc = np.load("model_acc.npy")

print(k_value)
print(p_order)
print(model_acc)

print("=-------------------------=")

print(np.argmax(model_acc))
print(k_value[125])
print(p_order[125])
print(model_acc[125])

# plt.scatter(k_value, model_acc)
# ax.set_title('Modelling The Accuracy Of The Classifier')
# ax.set_xlabel('Model k Value')
# ax.set_ylabel('Minkowski P Value')
# ax.set_zlabel('Model Accuracy')

# plt.show()
