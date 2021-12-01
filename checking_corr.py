import numpy as np
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import model_selection as ms
from sklearn import preprocessing as sklpp

df = pd.DataFrame(pd.read_csv("/Users/brndy.747/Documents/Maths_I.A_Final/archive/data.csv"))

df = df.drop(['tempo','beats','filename','mfcc1','mfcc2','mfcc3','mfcc4','mfcc5','mfcc6','mfcc7','mfcc8','mfcc9','mfcc10','mfcc11','mfcc12','mfcc13','mfcc14','mfcc15','mfcc16','mfcc17','mfcc18','mfcc19','mfcc20'],axis=1)
# df = df.drop(['filename','tempo', 'beats', 'chroma_stft', 'rmse', 'spectral_centroid' , 'spectral_bandwidth', 'rolloff', 'zero_crossing_rate'],axis=1)
df = pd.DataFrame(df)
df.drop(df.index[800:1000],0,inplace=True) ##Removes Rock+Reggae Music
df.drop(df.index[0:100],0,inplace=True) ##Removes blues Music
df.drop(df.index[200:300],0,inplace=True) ##Removes disco Music
df.drop(df.index[200:300],0,inplace=True) ##Removes hip-hop Music
df.drop(df.index[100:200],0,inplace=True) ##Removes country Music
df.drop(df.index[100:200],0,inplace=True) ##Removes jazz Music

def normalize(df):
    result = df.copy()
    for feature_name in df.columns:
        max_value = df[feature_name].max()
        min_value = df[feature_name].min()
        try:
            result[feature_name] = (df[feature_name] - min_value) / (max_value - min_value)
        except:
            result[feature_name] = df[feature_name]
    return result

better_norm_df = normalize(df)
better_norm_df['label'] = better_norm_df['label'].replace(['classical','metal','pop'],[0,1,2])
print(better_norm_df)

# pp = sns.pairplot(data=better_norm_df,
#                   x_vars=['chroma_stft', 'rmse', 'spectral_centroid' , 'spectral_bandwidth', 'rolloff', 'zero_crossing_rate'],
#                   y_vars=['chroma_stft', 'rmse', 'spectral_centroid' , 'spectral_bandwidth', 'rolloff', 'zero_crossing_rate'],
#                   hue='label')
# plt.show()

train, test = ms.train_test_split(better_norm_df, train_size=0.8 ,test_size=0.2, random_state=32, shuffle=True)
print("Train Dataset")
print(len(train))
print(train)
train_df = pd.DataFrame(train)
train_df.to_csv('train.csv')
print("Test Dataset")
print(len(test))
print(test)
test_df = pd.DataFrame(test)
test_df.to_csv('test.csv')