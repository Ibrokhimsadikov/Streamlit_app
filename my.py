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
import matplotlib.pyplot as plt
import streamlit.components.v1 as components
import requests
import joblib
import pickle
# Core Pkgs
import streamlit as st 
import os
from PIL import Image
shap.initjs()
st.set_option('deprecation.showPyplotGlobalUse', False)
import warnings
warnings.filterwarnings("ignore")
# Loading model to compare the results
lin_reg_explainer1 =pickle.load(open('shaply.pkl', 'rb'))
X_test = pickle.load(open('xtest.pkl','rb'))
listing2 = pickle.load(open('listing.pkl','rb'))
lm = pickle.load(open('lm.pkl','rb'))

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
        st.header("Global Model Explonation")
        st.text("")
        st.subheader("Feature Importance")
        st.pyplot(shap.summary_plot(lin_reg_explainer1.shap_values(X_test),
                  feature_names=listing2.drop(['price'], axis = 1).columns,
                  plot_type="bar",
                  color="dodgerblue"
                  ))
        st.text("")
        
        st.subheader("Global Impact")
        st_shap(shap.force_plot(lin_reg_explainer1.expected_value,
                lin_reg_explainer1.shap_values(X_test[0:100]),
                feature_names=listing2.drop(['price'], axis = 1).columns,
                out_names="Price($)", figsize=(25,3),
                link="identity"), 400)
        st.subheader("Feature Impact on output")
        st.pyplot(shap.summary_plot(lin_reg_explainer1.shap_values(X_test),
                  features = X_test,
                  feature_names=listing2.drop(['price'], axis = 1).columns))
       
        
        
        
        
        

            

    elif choice == "Single_predict":
        st.subheader("Local model explanation")
        
        row_index = st.slider('Select any individual observation to run local prediction', 0, 2000, 0)
        st.write(listing2.loc[[row_index]])
        row=listing2.loc[[row_index]].drop(['price'], axis = 1).values
        
        st_shap(shap.force_plot(lin_reg_explainer1.expected_value,lin_reg_explainer1.shap_values(row[0]),
                feature_names=listing2.drop(['price'], axis = 1).columns,out_names="Price($)"))
        sample_idx = 0

        shap_vals = lin_reg_explainer1.shap_values(row[0])

        st.text(f'Base Value : {lin_reg_explainer1.expected_value}')
        
        st.text(f'Shap Values for Sample %d:  {shap_vals}')
        print("\n")
        st.text(f'Prediction From Model                            : {lm.predict(row[0].reshape(1,-1))[0]}' )
        st.text(f'Prediction From Adding SHAP Values to Base Value : {lin_reg_explainer1.expected_value + shap_vals.sum()}' )
        


if __name__ == '__main__':
    main()
