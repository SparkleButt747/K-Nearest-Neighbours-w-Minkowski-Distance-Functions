import numpy as np
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

df = pd.DataFrame(pd.read_csv("/Users/brndy.747/PycharmProjects/maths_IA_research/data_by_year_o.csv"))
print(df)

pp = sns.pairplot(data=df,
                  x_vars=['year'],
                  y_vars=['acousticness' ,'danceability' ,'duration_ms', 'energy' , 'instrumentalness','liveness' ,'loudness' ,'speechiness' ,'tempo' ,'valence' ,'popularity' ,'key'],
                  hue='mode')
plt.show()

