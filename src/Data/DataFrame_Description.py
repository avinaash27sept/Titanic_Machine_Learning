import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import sys
sys.path.insert(0, 'src/')
import Main as main


with st.expander("DataFrame",expanded=False,icon=":material/table:") :
    st.dataframe(main.train)
with st.expander("DataFrame Describe",expanded=False,icon=":material/info:") :
    st.write(main.train.describe())
   

