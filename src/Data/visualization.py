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
    h = sns.heatmap(main.train1.isnull(),yticklabels=False,cbar=False,cmap='viridis')
    fig=h.get_figure()
    st.write(fig)
with CountPlot:
    chart1, chart2= st.columns([1,1],gap="small",vertical_alignment='center')
    with chart1 : 
        plt.figure(figsize=(6,4))
        plt.title("Count plot for survived vs not survived 0-Not survived 1 - Survived")
        h = sns.countplot(main.train1, x=main.train1['Survived'])
        fig=h.get_figure()
        st.write(fig)
    with chart2 : 
        plt.figure(figsize=(6,4))
        plt.title("Count plot for survived vs not survived 0-Not survived 1 - Survived")
        h = sns.countplot(main.train1, x=main.train1['Survived'],hue='Sex')
        fig=h.get_figure()
        st.write(fig)
    chart3, chart4= st.columns([1,1],gap="small",vertical_alignment='center')
    with chart3 : 
        plt.figure(figsize=(6,4))
        plt.title("Count plot for survived vs not survived 0-Not survived 1 - Survived Pclass")
        h = sns.countplot(main.train1, x=main.train1['Survived'],hue='Pclass')
        fig=h.get_figure()
        st.write(fig)
    with chart4 : 
        plt.figure(figsize=(6,4))
        plt.title("Count plot for survived vs not survived 0-Not survived 1 - Survived Pclass")
        h = sns.countplot(main.train1, x=main.train1['Survived'],hue='SibSp')
        fig=h.get_figure()
        st.write(fig)
with BoxPlot:
    chart1, chart2= st.columns([1,1],gap="small",vertical_alignment='center')
    with chart1 : 
        plt.figure(figsize=(6,4))
        plt.title("BoxPlot Age Count")
        h= sns.boxplot(x='Pclass',y='Age',data=main.train1,palette='winter')
        fig=h.get_figure()
        st.write(fig)
    with chart2 : 
        plt.figure(figsize=(6,4))
        plt.title("BoxPlot Gender Wise Age Count")
        h= sns.boxplot(x='Pclass',y='Age',data=main.train1,palette='winter',hue='Sex')
        fig=h.get_figure()
        st.write(fig)
    