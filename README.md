# K-Nearest Neighbors (KNN) with Minkowski Distance Functions

This repository contains the code and dataset for the research on K-Nearest Neighbors (KNN) classification using geometric approaches and various Minkowski distance functions. The goal of the research was to explore the effectiveness of different distance functions and the number of nearest neighbors in predicting discrete labels for unlabeled observations.

## Table of Contents

- [Introduction](#introduction)
- [Dataset](#dataset)
- [Preprocessing](#preprocessing)
- [KNN Model](#knn-model)
- [Distance Functions](#distance-functions)
- [Performance Evaluation](#performance-evaluation)
- [Results](#results)
- [Limitations and Future Work](#limitations-and-future-work)
- [References](#references)

## Introduction

This project investigates the application of K-Nearest Neighbors (KNN) classification models using different Minkowski distance functions. The primary objective is to determine the best distance function and the optimal number of nearest neighbors for classifying music genres from audio features.

## Dataset

The dataset used in this research is an open-source collection of music samples from 2000 and 2001. It includes 1000 audio samples across 10 genres: blues, classical, country, disco, hip-hop, jazz, metal, pop, reggae, and rock. Each sample is represented by 27 features extracted from 30-second audio clips.
![Screenshot 2024-07-06 at 7 11 01 PM](https://github.com/SparkleButt747/K-Nearest-Neighbours-w-Minkowski-Distance-Functions/assets/36875086/9a9eee2f-90af-4a6c-8228-27fd76652c7d)

## Preprocessing

To enhance the model's performance, the dataset underwent preprocessing steps, including:

1. **Dimensionality Reduction**: Reduced the number of features from 27 to 6 by visualizing data clusters and removing irrelevant features.
2. **Normalization**: Standardized feature values to ensure uniformity across different metrics (e.g., Hz, dB).

## KNN Model

The KNN model classifies an unknown sample based on the known classifications of its nearest neighbors. Key components include:

- **Training Set**: A dataset with known classifications used to train the model.
- **Test Set**: A dataset used to evaluate the model's performance.
- **Tunable Parameters**: The number of neighbors (k) and the order (p) in the Minkowski distance function.

## Distance Functions

The Minkowski distance function is a generalization of several distance metrics:

1. **Euclidean Distance (p=2)**: Measures straight-line distance.
2. **Manhattan Distance (p=1)**: Measures distance along axes at right angles.
3. **Chebyshev Distance (p=∞)**: Measures maximum distance along any coordinate dimension.

The choice of distance function significantly impacts the model's accuracy, especially in high-dimensional spaces.
![Screenshot 2024-07-06 at 7 12 41 PM](https://github.com/SparkleButt747/K-Nearest-Neighbours-w-Minkowski-Distance-Functions/assets/36875086/b9418700-195c-4511-b99b-79903a11633d)

## Performance Evaluation

The model's performance was evaluated using metrics such as accuracy, precision, recall, and F1-score. A confusion matrix was also used to analyze the model's strengths and weaknesses in classifying different genres.
![Screenshot 2024-07-06 at 7 13 36 PM](https://github.com/SparkleButt747/K-Nearest-Neighbours-w-Minkowski-Distance-Functions/assets/36875086/d7dd69a5-b371-4482-b005-4c5ed89bb408)
![Screenshot 2024-07-06 at 7 14 01 PM](https://github.com/SparkleButt747/K-Nearest-Neighbours-w-Minkowski-Distance-Functions/assets/36875086/0d7ed451-88af-4894-8a77-560c4e59f545)

## Results

The optimized KNN model achieved a high accuracy of 95% for classifying three distinct genres: classical, metal, and pop. Various combinations of k and p values were tested, and the optimal parameters were found to be k=9 and p=1 (Manhattan distance).

## Limitations and Future Work

While the model performed well, several limitations were identified:

- **Dataset Timeliness**: The dataset is from 2000-2001, and music genres have evolved since then.
- **Model Simplicity**: KNN is a basic model; exploring more complex models like neural networks could improve accuracy.

Future work includes updating the dataset with recent music samples and experimenting with advanced classification models.

## References

1. Mucherino, Antonio, et al. *Data Mining in Agriculture*. Springer, 2008.
2. Filipe, Joaquim, and Ana Fred. *Agents and Artificial Intelligence*. Springer, 2013.
3. Olteanu, Andrada. "GTZAN Dataset - Music Genre Classification." Kaggle, 2021.
4. Chatterjee, Aditya. "Manhattan Distance [Explained]." OpenGenus IQ, 2021.
5. Teknomo, Kardi. "Chebyshev Distance." Revoledu, 2021.
6. Mohajon, Joydwip. "Confusion Matrix for Your Multi-Class Machine Learning Model." Medium, 2021.
