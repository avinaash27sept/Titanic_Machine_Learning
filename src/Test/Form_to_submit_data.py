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




with st.form("Titanic survival prediction") : 
    st.title("Titanic survival prediction")
    Pclass = st.radio('Select Passenger Class',[1,2,3])
    Sex = st.radio('Select Sex 0-Male 1-Female',[0,1])
    Age = st.slider('Pick a Age', 1, 100)
    sipsp = st.selectbox('Select a family members',[1,2,3,4,5,6,7])
    parch = st.selectbox('Select a parch value',[0,1,2,3,4,5,6])
    fare = st.slider('Pick a fare',4, 600)
    embarked = st.radio('Select Embarked Sex 0-S 1-C 2 Q',[0,1,2]) 
    st.form_submit_button('Submit')


st.subheader("Confirm your submitted data : ")
st.write("Pclass : ", Pclass)
test = pd.DataFrame([Pclass,Sex,Age,sipsp,parch,fare,embarked]).transpose()
st.dataframe(test)
log = LogisticRegression()
log.fit(c.X_train,c.y_train)
predicted = log.predict(test)
if predicted==1 :
    st.success("You Survived")
    st.balloons()
else :
    st.warning("RIP!!!!!!!!! Not survived")
    st.snow()



