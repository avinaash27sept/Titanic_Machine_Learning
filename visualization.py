import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import DataFrame_Description as data
Heatmap, CountPlot, BoxPlot = st.tabs(['Heat Map','Count Plot','Box Plot'])
with Heatmap:
    h = sns.heatmap(data.train.isnull(),yticklabels=False,cbar=False,cmap='viridis')
    fig=h.get_figure()
    st.write(fig)
