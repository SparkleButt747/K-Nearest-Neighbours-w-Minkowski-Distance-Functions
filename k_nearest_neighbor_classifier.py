import distance_functionsv2
import numpy as np

class KNN:
    def __init__(self, k=3, p=1):
        if k==0:
            self.k = 1
        else:
            self.k = k
        self.p = p
        self.predictions = []
        self.probabilities_results = []

    def fit(self, X, Y):
        self.X_train_dataset = X
        self.Y_train_dataset = Y

    def predict(self, x_test=[]):

        for point_loc in range(len(x_test)):
            self.x_test = x_test[point_loc].flatten()
            self.distances = []
            self.nearest_neighbors = []

            # we know that the range+1 of the Y_train_dataset is the number of labels in the dataset
            self.probabilities = [0] * int((np.max(self.Y_train_dataset) - np.min(self.Y_train_dataset)) + 1)

            for i in range(len(self.X_train_dataset)):
                self.distances.append(
                    [distance_functionsv2.minkowski_distance(point_a=self.X_train_dataset[i], point_b=self.x_test, p=self.p),
                     self.Y_train_dataset[i]])

            self.distances.sort(key=lambda x: x[0], reverse=False)

            self.nearest_neighbors = self.distances[:self.k]

            neighbor_classes = []

            for point_location in range(len(self.nearest_neighbors)):
                neighbor_classes.append(int(self.nearest_neighbors[point_location][1]))

            for q in range(len(self.probabilities)):
                for labels in neighbor_classes:
                    if labels == q:
                        self.probabilities[q] += 1

            self.probabilities=np.array(self.probabilities)/self.k

            self.predictions.append(np.argmax(self.probabilities))
            self.probabilities_results.append(list(self.probabilities))

        return self.predictions, self.probabilities_results