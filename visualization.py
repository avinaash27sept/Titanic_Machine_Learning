import streamlit as st
import pandas as pd
import numpy as np
import DataFrame_Description as data
Heatmap, CountPlot, BoxPlot = st.tabs(['Heat Map','Count Plot','Box Plot'])
with Heatmap:
    st.title("Heat Map")    
    st.image("graphs/heatmap.png") 
