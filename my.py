#!/usr/bin/env python
# coding: utf-8

# In[2]:


import streamlit as st
import pandas as pd
from sklearn import datasets
import pickle
from sklearn.ensemble import RandomForestClassifier
#from PIL import Image


pickle_in = open("classifier1.pkl","rb")
classifier=pickle.load(pickle_in)

#img=Image.open("example.jpeg")
#st.image(img, width=300)

st.write("""
# Loan Predictor for Lending Club
This app is developed by "23AC", Institute of Advanced Analytics, 2020
""")
html_temp = """
    <div style="background-color:#e61212;padding:10px">
    <h2 style="color:white;text-align:center;">This app predicts the Credit Default Grade for any user </h2>
    </div>
    """
st.markdown(html_temp,unsafe_allow_html=True)
st.sidebar.header('Borrower Information')

def user_input_features():
    Loang = st.sidebar.text_input('Loan Amount', 10000)
    Term = st.sidebar.text_input('Term (0 for 36 months/ 1 for 60 months)', 0 )
    Rateg = st.sidebar.text_input('Interest Rate', 15)
    Empg = st.sidebar.text_input('Employment History', 3)
    Incomeg = st.sidebar.text_input('Annual Income', 25000)
    Purpose = st.sidebar.text_input('Purpose (0 for Debt, 1 other)', 0)
    Dtig = st.sidebar.text_input('Debt to Income', 20)
    Inquiryg = st.sidebar.text_input('Total Inquiries', 0)
    Utiliz = st.sidebar.text_input('Utilization', 55)
    Total = st.sidebar.text_input('Total Lines', 8)
    Total_Balance = st.sidebar.text_input('Total Balance', 0) 
    
    data = {'Loan Amount': Loang,
            'Term (0 for 36 months/ 1 for 60 months)': Term,
            'Interest Rate': Rateg,
            'Employment History': Empg,
            'Annual Income': Incomeg,
            'Purpose (0 for Debt, 1 other)': Purpose,
           'Debt to Income': Dtig,
           'Total Inquiries': Inquiryg,
           'Utilization': Utiliz,
           'Total Lines': Total,
           'Total Balance': Total_Balance}
    
    features = pd.DataFrame(data, index=[0])
    return features

df = user_input_features()

st.subheader('Borrower Information')
st.write(df)

#iris = datasets.load_iris()
#X = iris.data
#Y = iris.target
#clf = RandomForestClassifier()
#clf.fit(X, Y)
prediction = classifier.predict(df)
prediction_proba =classifier.predict_proba(df)
#st.subheader('Class labels and their corresponding index number')
#st.write(iris.target_names)
st.subheader('Result')
#st.write(iris.target_names[prediction])
st.write('GOOD' if prediction==0 else 'BAD')
st.subheader('Prediction Probability')
st.write(prediction_proba)
# In[ ]:





