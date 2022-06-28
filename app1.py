# -*- coding: utf-8 -*-
"""
Created on Thu Feb 10 22:19:37 2022

@author: Tarun
""" 

import streamlit as st
from prediction_work1 import web_page_works
import MenuBar1 as MN
from Data_vizuals1 import visualization_func

page = st.sidebar.selectbox("Menu", ("Predict", "Test_Data", "Data Visualization"))

if page == "Predict":
    web_page_works()
    
elif page ==  "Test_Data":
    MN.test_data_func()
    
elif page ==  "Data Visualization":
    visualization_func()
    
