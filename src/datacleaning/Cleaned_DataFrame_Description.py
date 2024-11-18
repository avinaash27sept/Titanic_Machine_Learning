import streamlit as st
import pandas as pd
import numpy as np
import Main as m
from sklearn.model_selection import train_test_split
import sys 
sys.path.insert(0,'src/')

m.train['Age'].mean()
m.train['Age'][m.train['Pclass']==1].mean()
m.train['Age'][m.train['Pclass']==2].mean()
m.train['Age'][m.train['Pclass']==3].mean()



def replaceAge(x) :
    age=x[1]
    pclass=x[0]

    if pd.isnull(age):
        if pclass==1:
            return 38.23
        elif pclass==2:
            return 29.87
        else :
            return 25.14
        # print("hi")
    else :
        return age
        # print("bye")
m.train['Age']=m.train[['Pclass','Age']].apply(replaceAge,axis=1)
m.train.to_csv("agemodified.csv")
X= m.train[['Pclass', 'Sex', 'Age', 'SibSp', 'Parch', 'Fare','Embarked']]
Y=m.train[['Survived']]
X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.3, random_state=42)

with st.expander("DataFrame",expanded=False,icon=":material/table:") :
    st.dataframe(m.train)
