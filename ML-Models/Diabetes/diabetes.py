import os

requirements = ['Flask==1.1.2','numpy','pandas','scikit-learn']
with open('requirements.txt', 'w') as f:
    for line in requirements:
        f.write(line + '\n')
    
os.system('pip install -r requirements.txt')
        
import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import joblib

filepath='ML-Models\diabetes.csv'
tar= 'Outcome'
df=pd.read_csv(filepath)
feature_df = df.drop(tar, axis=1, inplace=False)
for col in feature_df:
    if(feature_df[col].dtype=='object'):
        feature_df[col]=feature_df[col].str.strip()    

data = feature_df.iloc[0].to_json(indent= 2)
with open('data.json', 'w') as f:
    f.write('[')
    f.write(data)
    f.write(']')
# Identifying the categotical columns and label encoding them
le = LabelEncoder()
le1 = LabelEncoder()
number = 1
for col in df:
    if(df[col].dtype=='object'):
        df[col]=df[col].str.strip()      
        if(col==tar):
            df[col] = le1.fit_transform(df[col])
            joblib.dump(le1,"y_encoder.pkl")
        else:
            df[col]=le.fit_transform(df[col])
            temp="x_encoder%s"%number
            temp=temp+".pkl"
            joblib.dump(le,temp)
            number = number + 1

# Identifying the columns with null values and filling them with mean
for col in df:
    if(df[col].isnull().sum()!=0):
        df[col]=df[col].fillna(df[col].dropna().median())

#Train-Test Split
a=df.pop(tar)
df[tar]=a
x=df.iloc[:,:-1].values
y=df.iloc[:,-1].values
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2,random_state=1)

#Scaling
sc=StandardScaler()
x_train[:,:]=sc.fit_transform(x_train[:,:])
x_test[:,:]=sc.fit_transform(x_test[:,:])
joblib.dump(sc,"scaler.pkl")

#Training the model
from sklearn.ensemble import RandomForestClassifier
classifier = RandomForestClassifier()
classifier.fit(x_train,y_train)    
from sklearn.metrics import accuracy_score
y_pred=classifier.predict(x_test)
accuracy=accuracy_score(y_test, y_pred)
print("Accuracy:",accuracy*100,"%")
joblib.dump(classifier, 'model.pkl')