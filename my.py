#!/usr/bin/env python
# coding: utf-8

# In[2]:
#utility packages
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.feature_selection import *
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import LinearRegression
from sklearn import metrics
from streamlit_lottie import st_lottie
import shap
import streamlit.components.v1 as components
import requests
import joblib
# Core Pkgs
import streamlit as st 
import os
from PIL import Image
shap.initjs()
# Loading model to compare the results
lin_reg_explainer1 =joblib.load('shaply.sav')
# X_test = pickle.load(open('xtest.pkl','rb'))
# listing2 = pickle.load(open('listing.pkl','rb'))

def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()
lottie_hello = load_lottieurl("https://assets3.lottiefiles.com/packages/lf20_2hYese.json")

def st_shap(plot, height=None):
    shap_html = f"<head>{shap.getjs()}</head><body>{plot.html()}</body>"
    components.html(shap_html, height=height)
    
def main():
    """A Simple NLP app with Spacy-Streamlit"""
    st_lottie(lottie_hello, speed=1, loop=True, reverse=False, quality="medium", height=250, width=250)
    st.title("MVP Price Suggestion")
    

    menu = ["Model_general","Single_predict"]
    choice = st.sidebar.selectbox("Menu",menu)

    if choice == "Model_general":
        st.subheader("Metrics")
        #raw_text = st.text_area("Your Text","Enter Text Here")
        st_shap(shap.force_plot(lin_reg_explainer1.expected_value,lin_reg_explainer1.shap_values(X_test[0]),
                feature_names=listing2.drop(['price'], axis = 1).columns,out_names="Price($)"))
        sample_idx = 0

        shap_vals = lin_reg_explainer1.shap_values(X_test[sample_idx])

        st.text(f'Base Value : {lin_reg_explainer1.expected_value}')
        
        st.text(f'Shap Values for Sample %d: {sample_idx} {shap_vals}')
        print("\n")
        #print("Prediction From Model                            : ", lm.predict(X_test[sample_idx].reshape(1,-1))[0])
        print("Prediction From Adding SHAP Values to Base Value : ", lin_reg_explainer1.expected_value + shap_vals.sum())
        
        
        
        
#         if st.button("Tokenize"):
            

    elif choice == "Single_predict":
        st.subheader("Named Entity Recognition")
        


if __name__ == '__main__':
    main()
