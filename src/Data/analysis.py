import streamlit as st
import pandas as pd
st.header("Titanic Dataset - Exploratory Data Analysis")

st.markdown("""This dashboard provides an overview of the Titanic dataset, including missing values, 
            key factors for prediction, and feature engineering insights.""")

st.markdown("""We will be working with the Titanic Data Set from Kaggle. This is a very famous data set and very often is a student's first step in machine learning! 
            We'll be trying to predict a classification- survival or deceased. Let's begin our understanding of implementing different Machine Learning Models on this dataset""")
train = pd.read_csv("resources/csv/titanic_train.csv")         
Overview, Missing, Features, Observation= st.tabs(["General Overview", "Missing Values", "Key Features", "Noteworthy Observations"])
with Overview:
    st.write("Overview of the given Dataset")
    st.write("1. Number of Records:")
    st.write(891)
    st.write("2. Number of Features:")
    st.write(12)
with Missing:
    st.write("Overview of missing values across the dataset")
    st.write("1. Age:")
    st.write(177)
    st.write("2. Cabin:")
    st.write(687)
    st.write("3. Embarked:")
    st.write(2)
    st.write("4. Graphical Representation")
    st.bar_chart(train.isnull().sum())
with Features:
    st.write("Explore the distribution of key numerical features")
    st.write("1. Target Variable:")
    st.caption("Not Survived")
    st.caption("Survived")
    st.write("2. Potential Predictors:")
    st.caption("Pclass")
    st.caption("Sex")
    st.caption("Age")       
    st.caption("Fare")       
    st.caption("Embarked")        
    st.caption("SibSp & Parch")
    st.write("3. Graphical Representation of Distribution of Age, Fare and Pclass")
    for col in ['Age', 'Fare', 'Pclass']:
        st.bar_chart(train[col])
with Observation:
    st.write("Categorical Features:")
    st.caption("""Cabin and Age columns has high missing values, possibly useful after encoding 
             (e.g., presence of cabin data). On the other hand
             Embarked has minimal missing values and thus can be neglected since it wont hamper 
             the prediction significantly.""")
    
    st.write("Duplicates:")
    st.caption("No explicit duplicates based on PassengerId can be seen the dataset")