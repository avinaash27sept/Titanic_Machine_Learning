import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import sys
sys.path.insert(0, 'src/')
import Main as main
Heatmap, CountPlot, BoxPlot = st.tabs(['Heat Map','Count Plot','Box Plot'])
with Heatmap:
    plt.figure(figsize=(6,4))
    plt.title("Heatmap to check null values")
    h = sns.heatmap(main.train.isnull(),yticklabels=False,cbar=False,cmap='viridis')
    fig=h.get_figure()
    st.write(fig)
with CountPlot:
    chart1, chart2, = st.columns([1,1],gap="small",vertical_alignment='center')
    with chart1 : 
        plt.figure(figsize=(6,4))
        plt.title("Count plot for survived vs not survived 0-Not survived 1 - Survived")
        h = sns.countplot(main.train, x=main.train['Survived'])
        fig=h.get_figure()
        st.write(fig)
    with chart2 : 
        plt.figure(figsize=(6,4))
        plt.title("Count plot for survived vs not survived 0-Not survived 1 - Survived")
        h = sns.countplot(main.train, x=main.train['Survived'],hue='Sex')
        fig=h.get_figure()
        st.write(fig)