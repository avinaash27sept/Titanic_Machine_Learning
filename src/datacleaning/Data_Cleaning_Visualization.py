import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import sys
sys.path.insert(0, 'src/')
import Main as main
Heatmap,  BoxPlot = st.tabs(['Heat Map','Box Plot'])

with Heatmap:
    plt.figure(figsize=(6,4))
    plt.title("Heatmap to check null values")
    h = sns.heatmap(main.train.isnull(),yticklabels=False,cbar=False,cmap='viridis')
    fig=h.get_figure()
    st.write(fig)

   
with BoxPlot:
    chart1, chart2= st.columns([1,1],gap="small",vertical_alignment='center')
    with chart1 : 
        plt.figure(figsize=(6,4))
        plt.title("BoxPlot Age Count")
        h= sns.boxplot(x='Pclass',y='Age',data=main.train,palette='winter')
        fig=h.get_figure()
        st.write(fig)
    with chart2 : 
        plt.figure(figsize=(6,4))
        plt.title("BoxPlot Gender Wise Age Count")
        h= sns.boxplot(x='Pclass',y='Age',data=main.train,palette='winter',hue='Sex')
        fig=h.get_figure()
        st.write(fig)