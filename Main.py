import streamlit as st
import pandas as pd
import numpy as np
LOGO_URL_LARGE="resources/logo/logo.png"
st.logo(LOGO_URL_LARGE,size="large")
train = pd.read_csv("resources/csv/titanic_train.csv")
st.title(":blue[Titanic Ship Survival Prediction System]:")
pages = {

    "Data" : [st.Page("src/Data/DataFrame_Description.py"),st.Page("src/Data/visualization.py"),st.Page("src/Data/analysis.py")],
    "Data Cleaning" :[st.Page("src/datacleaning/Cleaned_DataFrame_Description.py"),st.Page("src/datacleaning/Data_Cleaning_Visualization.py")],
    "Models" :[st.Page("src/model/Name_of_Model.py")],
    "Result Comparison" :[st.Page("src/Results/Result_table.py"),st.Page("src/Results/Model_selection_and_justification.py")],
    "Parameter Tuning" :[st.Page("src/modelTuning/Parameter_list_for_tuning.py"),st.Page("src/modelTuning/Result_after_parameter_tuning.py")],
    "Test on Live Data" :[st.Page("src/Test/Form_to_submit_data.py")]
   
}

pg = st.navigation(pages)
pg.run()




