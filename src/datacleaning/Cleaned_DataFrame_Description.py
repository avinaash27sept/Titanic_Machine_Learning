import streamlit as st
import pandas as pd
import numpy as np
import Main as m
import sys 
sys.path.insert(0,'src/')

st.write("Clean data frame")
train = pd.read_csv("resources/csv/titanic_train.csv")
train['Age'].mean()
train['Age'][train['Pclass']==1].mean()
train['Age'][train['Pclass']==2].mean()
train['Age'][train['Pclass']==3].mean()

with st.expander("DataFrame",expanded=False,icon=":material/table:") :
    st.dataframe(m.train)

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
        train['Age']=train[['Pclass','Age']].apply(replaceAge,axis=1)
        train.to_csv("agemodified.csv")
        X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.3, random_state=42)
