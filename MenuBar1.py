import pickle
import pandas as pd
import streamlit as st
from sklearn.model_selection import train_test_split


test_data = pd.read_csv("C:/Users/Tarun/OneDrive/Desktop/pppp/Testing_Data.csv")

try:
    test_data = test_data.drop(['Unnamed: 0'], axis = 1)
    print(test_data)
except:
    pass




def test_data_func():
    st.dataframe(test_data)
    
import streamlit as st
import base64
    
def documentation_func():
    
    
    st.header('  Working on it... We will be soon with updates.  ')
    

    def show_pdf(file_path):
        with open(file_path,"rb") as f:
            base64_pdf = base64.b64encode(f.read()).decode('utf-8')
            pdf_display = F'<iframe src="data:application/pdf;base64,{base64_pdf}" width="700" height="1000" type="application/pdf"></iframe>'
        st.markdown(pdf_display, unsafe_allow_html=True)
        print('Done')

    show_pdf('C:/Users/Tarun/Downloads/SOFTWARE ENGINEERING NOTES.pdf')

    
    
    
    