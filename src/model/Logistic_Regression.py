import streamlit as st
import pandas as pd
import sys
sys.path.insert(0, 'datacleaning')
import  datacleaning.Cleaned_DataFrame_Description as c
from sklearn import metrics
from sklearn.linear_model import LogisticRegression

#remove comments for following lines if null value error
# st.bar_chart(c.X_train.isnull().sum())
# st.bar_chart(c.y_train.isnull().sum())

log = LogisticRegression()
log.fit(c.X_train,c.y_train)
predicted = log.predict(c.X_test)
st.info(f"Accuracy Score = {metrics.accuracy_score(predicted,c.y_test)} ")
st.info(f"F1 Score = {metrics.f1_score(predicted,c.y_test)} ")
st.info(f"Recall Score = {metrics.recall_score(predicted,c.y_test)} ")

mat = metrics.confusion_matrix(predicted,c.y_test);

st.write(f"Confusion Matrix {mat}")




