# -*- coding: utf-8 -*-
"""
Created on Fri Jan 28 20:54:50 2022

@author: Tarun
"""

from PIL import Image
import numpy as np 
import streamlit as st 

# Function to Read and Manupilate Images
def load_image(img):
    im = Image.open(img)
    image = np.array(im)
    return image



def visualization_func():
    st.title('      Data Visualization    !  ')
    
    #===============================1  MUTUAL INFORMATION==========================================================
    st.header('Mutual Information')
   
    uploadFile1 = 'C:/Users/Tarun/OneDrive/Desktop/pppp/Graphs/MI.png'

    if uploadFile1 is not None:
    
        img1 = load_image(uploadFile1)
        st.image(img1)
    
    

    #===============================2  DESC_LEN HIST==========================================================
    
    st.header('Histograph of Quant')
   
    uploadFile2 = 'C:/Users/Tarun/OneDrive/Desktop/pppp/Graphs/quant hist.png'

    if uploadFile2 is not None:
    
        img2 = load_image(uploadFile2)
        st.image(img2)
    
    #===============================3  AGE HIST==========================================================
    
    st.header('Histograph of 12th grade')
   
    uploadFile3 = 'C:/Users/Tarun/OneDrive/Desktop/Salary_Estimate_Proj/project_Docs/age_hist.png'

    if uploadFile3 is not None:
    
        img3 = load_image(uploadFile3)
        st.image(img3)
        
    #===============================4  RATING HIST==========================================================
    
    st.header('Histograph of 10th grade')
   
    uploadFile4 = 'C:/Users/Tarun/OneDrive/Desktop/pppp/Graphs/10hist.png'

    if uploadFile4 is not None:
    
        img4 = load_image(uploadFile4)
        st.image(img4)
        
   
    
        
    #===============================6 Box rating=========================================================
    
    st.header('Boxplot of Quant')
   
    uploadFile6 = 'C:/Users/Tarun/OneDrive/Desktop/pppp/Graphs/10box.png'

    if uploadFile6 is not None:

        img6 = load_image(uploadFile6)
        st.image(img6)
        
    #===============================7 Box Desc_len =========================================================
    
    st.header('Boxplot of 12th grade')
   
    uploadFile7 = 'C:/Users/Tarun/OneDrive/Desktop/pppp/Graphs/12box.png'

    if uploadFile7 is not None:

        img7 = load_image(uploadFile7)
        st.image(img7)
        
    #===============================8 Box Salary =========================================================
     
    st.header('Boxplot of 10th grade')
    
    uploadFile8 = 'C:/Users/Tarun/OneDrive/Desktop/pppp/Graphs/10box.png'

    if uploadFile8 is not None:
        img8 = load_image(uploadFile8)
        st.image(img8)
        
    
    #===============================10 HeatMap =========================================================
     
    st.header("Heatmap between ['age', 'desc_len', 'int_salary', 'Rating']")
    
    uploadFile10 = 'C:/Users/Tarun/OneDrive/Desktop/pppp/Graphs/heat.png'

    if uploadFile10 is not None:
        img10 = load_image(uploadFile10)
        st.image(img10)
        
    
    #===============================11 Scatter Plot ('Desc_len' , 'Age') =========================================================
     
    st.header("Scatter Plot between [ 'Quant', 'GraduationYear',   'experince', '12percentage', '10percentage' ,  'Salary' ]")
    
    uploadFile11 = 'C:/Users/Tarun/OneDrive/Desktop/pppp/Graphs/reg_Quant_salary.png'

    if uploadFile11 is not None:
        img11 = load_image(uploadFile11)
        st.image(img11)
        
    #===============================12 Scatter Plot ('Desc_len' , 'Rating') =========================================================
     
    st.header("Scatter Plot between ['Quant', 'Salary']")
    
    uploadFile12 = 'C:/Users/Tarun/OneDrive/Desktop/Salary_Estimate_Proj/project_Docs/sac_dec_rating.png'

    if uploadFile12 is not None:
        img12 = load_image(uploadFile12)
        st.image(img12)
        
    #===============================13 Scatter Plot ('Desc_len' , 'Salary') =========================================================
     
    st.header("Scatter Plot between ['10th grade', 'Salary']")
    
    uploadFile13 = 'C:/Users/Tarun/OneDrive/Desktop/pppp/Graphs/reg_10_salary.png'

    if uploadFile13 is not None:
        img13 = load_image(uploadFile13)
        st.image(img13)
        
    #===============================14 Scatter Plot ('Age' , 'Salary') =========================================================
     
    st.header("Scatter Plot between ['12th grade', 'Salary']")
    
    uploadFile14 = 'C:/Users/Tarun/OneDrive/Desktop/pppp/Graphs/reg_12_salary.png'

    if uploadFile14 is not None:
        img14 = load_image(uploadFile14)
        st.image(img14)
    