import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

train = pd.read_csv("Resources/titanic_train.csv")
with st.expander("DataFrame",expanded=False,icon=":material/table:") :
    st.dataframe(train)
with st.expander("DataFrame Describe",expanded=False,icon=":material/info:") :
    st.write(train.describe())
   

