import streamlit as st
import pandas as pd
import numpy as np

st.title(":blue[Titanic Ship Survival Prediction System]:")
pages = {

    "Data" : [st.Page("DataFrame_Description.py"),st.Page("visualization.py"),st.Page("analysis.py")],
    "Data Cleaning" :[st.Page("Cleaned_DataFrame_Description.py"),st.Page("Data_Cleaning_Visualization.py")],
    "Models" :[st.Page("Name_of_Model.py")],
    "Result Comparison" :[st.Page("Result_table.py"),st.Page("Model_selection_and_justification.py")],
    "Parameter Tuning" :[st.Page("Parameter_list_for_tuning.py"),st.Page("Result_after_parameter_tuning.py")],
    "Test on Live Data" :[st.Page("Form_to_submit_data.py")]
   
  
    
}

pg = st.navigation(pages)
pg.run()




