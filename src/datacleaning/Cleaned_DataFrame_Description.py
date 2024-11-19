import streamlit as st
import pandas as pd
import numpy as np
import Main as m
from sklearn.model_selection import train_test_split
import sys 
import time
sys.path.insert(0,'src/')

# m.train['Age'].mean()
c1 =  m.train['Age'][m.train['Pclass']==1].mean()
c2 =  m.train['Age'][m.train['Pclass']==2].mean()
c3 =  m.train['Age'][m.train['Pclass']==3].mean()



def replaceAge(x) :
    age=x[1]
    pclass=x[0]

    if pd.isnull(age):
        if pclass==1:
            return c1
        elif pclass==2:
            return c2
        else :
            return c3
        # print("hi")
    else :
        return age
        # print("bye")
m.train['Age']=m.train[['Pclass','Age']].apply(replaceAge,axis=1)
m.train['Embarked'].fillna('S', inplace=True)
m.train.replace({'male':0,'female':1},inplace=True)
m.train.replace({'S':0,'C':1,'Q':2},inplace=True)
time.sleep(2)
X=m.train[['Pclass', 'Sex', 'Age', 'SibSp', 'Parch', 'Fare','Embarked']]
Y=m.train[['Survived']]


X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.3, random_state=42)

with st.expander("DataFrame",expanded=False,icon=":material/table:") :
    st.dataframe(m.train)
