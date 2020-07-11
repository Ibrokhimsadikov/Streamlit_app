#!/usr/bin/env python
# coding: utf-8

# In[2]:


import streamlit as st
import pandas as pd
from sklearn import datasets
import pickle
from sklearn.ensemble import RandomForestClassifier


pickle_in = open("classifier.pkl","rb")
classifier=pickle.load(pickle_in)

st.write("""
# Lending Club Credit Grade Predictor App
This app is developed by "Data Wizards Team", to seamlessly use Machine Learning in production level simulation!
""")
html_temp = """
    <div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;">This app predicts the Credit Default Grade for any user </h2>
    </div>
    """
st.markdown(html_temp,unsafe_allow_html=True)
st.sidebar.header('User Input Parameters')

def user_input_features():
    EXT_SOURCE_2 = st.sidebar.text_input('EXT_SOURCE_2', 0.339150)
    EXT_SOURCE_3 = st.sidebar.text_input('EXT_SOURCE_3', 0.510726)
    credit_ration_annuity = st.sidebar.text_input('credit_ration_annuity', 17.832160)
    credit_minus_goods = st.sidebar.text_input('credit_minus_goods', 73417.5)
    credit_ratio_annuity_ratio_employed = st.sidebar.text_input('credit_ratio_annuity_ratio_employed', -0.006078)
    NAME_EDUCATION_TYPE = st.sidebar.text_input('NAME_EDUCATION_TYPE',2)
    income_ration_annuity = st.sidebar.text_input('income_ration_annuity',3.287999)
    employed_ratio_birth = st.sidebar.text_input('employed_ratio_birth',0.195379)
    NAME_CONTRACT_STATUS_mean = st.sidebar.text_input('NAME_CONTRACT_STATUS_mean',1.666667)
    AMT_PAYMENT_sum = st.sidebar.text_input('AMT_PAYMENT_sum',68567.040)
    
    data = {'EXT_SOURCE_2': EXT_SOURCE_2,
            'EXT_SOURCE_3': EXT_SOURCE_3,
            'credit_ration_annuity': credit_ration_annuity,
            'credit_minus_goods': credit_minus_goods,
            'credit_ratio_annuity_ratio_employed': credit_ratio_annuity_ratio_employed,
            'NAME_EDUCATION_TYPE': NAME_EDUCATION_TYPE,
           'income_ration_annuity': income_ration_annuity,
           'employed_ratio_birth': employed_ratio_birth,
           'NAME_CONTRACT_STATUS_mean': NAME_CONTRACT_STATUS_mean,
           'AMT_PAYMENT_sum': AMT_PAYMENT_sum}
    
    features = pd.DataFrame(data, index=[0])
    return features

df = user_input_features()

st.subheader('Client Input parameters')
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
st.subheader('Prediction')
#st.write(iris.target_names[prediction])
st.write(prediction)
st.subheader('Prediction Probability')
st.write(prediction_proba)
# In[ ]:





