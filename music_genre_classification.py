import pandas as pd
import numpy as np

test_df = pd.DataFrame(pd.read_csv("test.csv"))
train_df = pd.DataFrame(pd.read_csv("train.csv"))

train_df.drop(train_df.columns[train_df.columns.str.contains('unnamed',case = False)],axis = 1, inplace = True)
test_df.drop(test_df.columns[test_df.columns.str.contains('unnamed',case = False)],axis = 1, inplace = True)

test_dataset=test_df.to_numpy()
train_dataset=train_df.to_numpy()

X_train = train_dataset[:, [0,1,2,3,4,5]]
Y_train = train_dataset[:, [6]]

x_test = test_dataset[:, [0,1,2,3,4,5]]
y_test = test_dataset[:, [6]]


from k_nearest_neighbor_classifier import KNN

y_test_presentable = []


def calculate_acc(predictions):
    correct = 0
    for point_loc in range(len(predictions)):
        if predictions[point_loc] == y_test[point_loc]:
            correct += 1
        y_test_presentable.append(int(y_test[point_loc]))
    return correct / len(predictions)


clf = KNN(k=9, p=1)
clf.fit(X_train, Y_train)
predictions, probabilities = clf.predict(x_test)

print('Model Accuracy: '+str(calculate_acc(predictions)))
print('Key-> 0:Classical  1:Metal  2:Pop')
print('Model Predictions: '+str(predictions))
print('Actual Labels:     '+str(y_test_presentable))
print('')
print('Probabilities Key->  The position of the probability in the list, is the probability of that particular class (all positions start from 0)')
print('')
print('Probabilities:     '+str(probabilities))

c_c = 0
c_m = 0
c_p = 0
m_c = 0
m_m = 0
m_p = 0
p_c = 0
p_m = 0
p_p = 0
c_tol = 0
m_tol = 0
p_tol = 0

for i in range(len(predictions)):
    if predictions[i]==0 and y_test_presentable[i]==0:
        c_c+=1
    if predictions[i]==1 and y_test_presentable[i]==0:
        c_m+=1
    if predictions[i]==2 and y_test_presentable[i]==0:
        c_p+=1

    if predictions[i]==0 and y_test_presentable[i]==1:
        m_c+=1
    if predictions[i]==1 and y_test_presentable[i]==1:
        m_m+=1
    if predictions[i]==2 and y_test_presentable[i]==1:
        m_p+=1

    if predictions[i]==0 and y_test_presentable[i]==2:
        p_c+=1
    if predictions[i]==1 and y_test_presentable[i]==2:
        p_m+=1
    if predictions[i]==2 and y_test_presentable[i]==2:
        p_p+=1

    if predictions[i]==0:
        c_tol+=1
    if predictions[i]==1:
        m_tol+=1
    if predictions[i]==2:
        p_tol+=1


print('c_c: ' + str(c_c))
print('c_m: ' + str(c_m))
print('c_p: ' + str(c_p))
print('m_c: ' + str(m_c))
print('m_m: ' + str(m_m))
print('m_p: ' + str(m_p))
print('p_c: ' + str(p_c))
print('p_m: ' + str(p_m))
print('p_p: ' + str(p_p))
print("--------")
print('c_tol: ' + str(c_tol))
print('m_tol: ' + str(m_tol))
print('p_tol: ' + str(p_tol))

def calculate_precision(tp, fp):
    return (tp)/(tp+fp)

def calculate_recall(tp, fn):
    return (tp)/(tp+fn)

def calculate_f1_score(tp, fp, fn):
    return (2*tp)/((2*tp)+fp+fn)

def calculate_accuracy(tp, tn, fp, fn):
    return (tp+tn)/(tp+tn+fp+fn)

print('--------------------------------------')

print(str(calculate_precision((c_c), (c_m+c_p)))+' Precision_Classical')
print(str(calculate_recall((c_c), (m_c+p_c)))+' Recall Classical')
print(str(calculate_f1_score((c_c), (c_m+c_p), (m_c+p_c)))+' F1_Score Classical')
print(str(calculate_accuracy((c_c),(m_m+p_p+m_p+p_m),(c_m+c_p),(m_c+p_c)))+' Accuracy Classical')

print('--------------------------------------')

print(str(calculate_precision((m_m), (m_c+m_p)))+' Precision Metal')
print(str(calculate_recall((m_m),(c_m+p_m)))+' Recall Metal')
print(str(calculate_f1_score((m_m), (m_c+m_p), (c_m+p_m)))+' F1_Score Metal')
print(str(calculate_accuracy((m_m), (c_c+p_p+p_c+c_p), (m_c+m_p), (c_m+p_m)))+' Accuracy Metal')

print('--------------------------------------')

print(str(calculate_precision((p_p), (p_c+p_m)))+' Precision Pop')
print(str(calculate_recall((p_p), (m_p+c_p)))+' Recall Pop')
print(str(calculate_f1_score((p_p), (p_m+p_c), (m_p+c_p)))+' F1_Score Pop')
print(str(calculate_accuracy((p_p), (c_c+m_m+c_m+m_c), (p_c+p_m), (m_p+c_p)))+' Accuracy Pop')