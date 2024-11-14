import streamlit as st
import pandas as pd
import numpy as np

st.title(":blue[Titanic Ship Survival Prediction System]:")
pages = {

    "Data" : [st.Page("DataFrame_Description.py"),st.Page("visualization.py"),st.Page("analysis.py")]
}

pg = st.navigation(pages)
pg.run()




