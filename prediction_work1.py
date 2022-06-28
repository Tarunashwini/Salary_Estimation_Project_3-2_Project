# -*- coding: utf-8 -*-
"""
Created on Fri Jan 28 16:16:52 2022

@author: Tarun
"""
import pickle
import pandas as pd
import streamlit as st
from sklearn.model_selection import train_test_split

with open('rfmodel_pickle','rb') as f1:
    ml = pickle.load(f1)
    

############################################S###########################################################################

def web_page_works():
    
    st.title('  Salary Estimation Project  ')
    
    st.write('Enter your 10 Grade percentage :    ')
    
    _10 =st.number_input(' ',min_value=1, max_value=600)
    _10 = int(_10)
    
    st.write('Enter your 12 Grade percentage :    ')
    _12 = st.number_input(' ',min_value=1, max_value=900)
    _12 = int(_12)
    
    st.write('Enter your Graduation year(2015 - 2020):    ')
    Graduation =st.number_input(' ',min_value=1, max_value=2345)
    Graduation = int(Graduation)
    
    st.write('Enter your Quant score: (100 - 1000)   ')
    Quant =st.number_input(' ',min_value=1, max_value=1000)
    Quant = int(Quant)
    
    st.write('Enter your experince: (0 - 3) ')
    exp =st.number_input(' ',min_value=0, max_value=3)
    exp = int(exp)
    
    
    y_pred = ml.predict([[_10, _12, Graduation, Quant, exp]])
    
    bt = st.button('Submit')
    
    if bt:
        st.write('The Estimated value is:  ')
        st.header(int(y_pred))
        
        
        
        
        
    
    
    
   