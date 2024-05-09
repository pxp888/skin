import streamlit as st
import matplotlib.pyplot as plt

def performance():
    st.write("## Model Performance")
    

    st.write("#### Train, Validation and Test Set: Labels Frequencies")
    st.write("Before Augmentation:")

    ### Class Distribution

    
    st.write("After Augmentation:")

    
    st.write("#### Model Performance Metrics")

    train1 = plt.imread("assets/images/train1.png")
    st.image(train1, use_column_width=True)

    con1 = plt.imread("assets/images/con1.png")
    st.image(con1, use_column_width=True)
