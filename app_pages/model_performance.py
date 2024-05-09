import streamlit as st
import matplotlib.pyplot as plt

def performance():
    st.write("## Model Performance")
    

    st.write("#### Train, Validation and Test Set: Labels Frequencies")

    st.markdown("""
        |Class|Count|
        |-|-|
        |bkl | 1099
        |nv | 6705
        |df | 115
        |mel | 1113
        |vasc | 142
        |bcc | 514
        |akiec | 327
        |TOTAL | 10015  
        """)

    st.write("Before Augmentation:")

    st.markdown("""
        |       | TRAIN | TEST | VALIDATE | TOTAL |
        |-------|-------|------|----------|-------|
        | bkl   | 210   | 60   | 30       | 300   |
        | nv    | 210   | 60   | 30       | 300   |
        | df    | 80    | 23   | 12       | 115   |
        | mel   | 210   | 60   | 30       | 300   |
        | vasc  | 99    | 28   | 15       | 142   |
        | bcc   | 210   | 60   | 30       | 300   |
        | akiec | 210   | 60   | 30       | 300   |
        | TOTAL | 1229  | 351  | 177      |    |
    """)
    

    ### Class Distribution

    
    st.write("After Augmentation:")

    st.markdown(""" 
        |       | TRAIN | TEST | VALIDATE | TOTAL |
        |-------|-------|------|----------|-------|
        | bkl   | 210   | 60   | 30       | 300   |
        | nv    | 210   | 60   | 30       | 300   |
        | df    | 224   | 23   | 12       | 259   |
        | mel   | 210   | 60   | 30       | 300   |
        | vasc  | 198   | 28   | 15       | 241   |
        | bcc   | 210   | 60   | 30       | 300   |
        | akiec | 210   | 60   | 30       | 300   |
        | TOTAL | 1472  | 351  | 177      | 2000  |
                """)


    
    st.write("#### Model Performance Metrics")

    train1 = plt.imread("assets/images/train1.png")
    st.image(train1, use_column_width=True)

    con1 = plt.imread("assets/images/con1.png")
    st.image(con1, use_column_width=True)
