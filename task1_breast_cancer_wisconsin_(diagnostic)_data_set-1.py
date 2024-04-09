# -*- coding: utf-8 -*-
"""Task1-Breast Cancer Wisconsin (Diagnostic) Data Set.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1WxqA8sc2YHvvG1VRpt-hEj2rz_TEsRos

# Breast Cancer Wisconsin (Diagnostic)

### ABOUT DATASET

---



### Attribute Information:

1) ID number

2) 32 independent features

Ten real-valued features are computed for each cell nucleus:

a) radius (mean of distances from center to points on the perimeter)

b) texture (standard deviation of gray-scale values)

c) perimeter

d) area

e) smoothness (local variation in radius lengths)

f) compactness (perimeter^2 / area - 1.0)

g) concavity (severity of concave portions of the contour)

h) concave points (number of concave portions of the contour)

i) symmetry

j) fractal dimension ("coastline approximation" - 1)

### Output:

Diagnosis: The target variable which predicts the person is M = malignant or B = benign.

**LOADING** **DATASET**
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df=pd.read_csv('/content/data.csv')
df

df.head()

df.tail()

df.info()

for i in df:
  a=df[i].value_counts()
  print(a)

df.drop(['id','Unnamed: 32'],axis=1,inplace=True)

df.isna().sum()

df.dtypes

df.duplicated().sum()

"""**DATA VISUALIZATION**"""

Diaganosis=df['diagnosis'].value_counts()
plt.pie(x=Diaganosis,labels=['Benign','Malignant'],autopct='%1.1f%%')
plt.title('Chart of Cancer Diagnosed')

"""**OUTLIER DETECTION**"""

for i in df.select_dtypes(include='number').columns:
  sns.boxplot(x=i,data=df,color='c')
  plt.show()

"""**CORRELATION BETWEEN FEATURES**"""

from sklearn.preprocessing import LabelEncoder
end=LabelEncoder()
df['diagnosis']=end.fit_transform(df['diagnosis'])
plt.figure(figsize=(20,20))
sns.heatmap(df.corr(),annot=True)

x=df.iloc[:,1:].values
x

y=df.iloc[:,0].values
y

"""**SPLITTING DATASET TO TRAINING DATA AND TESTING DATA**"""

from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.30,random_state=42)
x_train

x_test

y_train

y_test

"""**NORMALIZATION**"""

from sklearn.preprocessing import MinMaxScaler
scaler=MinMaxScaler()
scaler.fit(x_train)
x_train=scaler.transform(x_train)
x_test=scaler.transform(x_test)
x_train

x_test

"""**MODEL CREATION**"""

from sklearn.neighbors import KNeighborsClassifier
model1=KNeighborsClassifier(n_neighbors=7)
from sklearn.tree import DecisionTreeClassifier
model2=DecisionTreeClassifier(criterion='entropy',random_state=42)
from sklearn.ensemble import RandomForestClassifier
model3=RandomForestClassifier(n_estimators=100,criterion='entropy',random_state=42)
lst=[model1,model2,model3]
from sklearn.metrics import accuracy_score,confusion_matrix,classification_report

"""**PERFORMANCE EVALUATION**"""

for i in lst:
  i.fit(x_train,y_train)
  y_pred=i.predict(x_test)
  print(y_pred)
  print('score=',accuracy_score(y_test,y_pred))
  print('matrix:',confusion_matrix(y_test,y_pred))
  print('Report:',classification_report(y_test,y_pred))
  print('-'*1000)

from sklearn.metrics import ConfusionMatrixDisplay
cm=confusion_matrix(y_test,y_pred)
lab=['Benign','Malignant']
cmd=ConfusionMatrixDisplay(cm,display_labels=lab)
cmd.plot()
