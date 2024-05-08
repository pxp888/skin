import streamlit as st
import os
import random as rn
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style("white")
from matplotlib.image import imread
from src.classify import classifyImage


def Finder():
    st.info(
        f"## Random Sample\n"
        f"Pressing the button below will display a random image from the test dataset along with it's class label.\n\n"
        f"You can drag or save this image to test the classifier model. \n"
    )

    if st.button("Show Random Sample"):
        
        base_dir = 'inputs/work/test'
        subdirs = os.listdir(base_dir)
        sub = rn.choice(subdirs)
        base_dir = os.path.join(base_dir, sub)
        imfiles = os.listdir(base_dir)
        imfile = rn.choice(imfiles)
        path = os.path.join(base_dir, imfile)
        
        img = imread(path)
        st.write(f'Class Label: ')
        st.write(f"### {sub}")
        st.image(img)


    st.write("## Upload Image")

    uploaded_file = st.file_uploader("Choose an image...", type="jpg")
    if uploaded_file is not None:
        img = imread(uploaded_file)
        st.image(img)
        out = classifyImage(img)
        
        classes = ['akiec', 'bcc', 'bkl', 'df', 'mel', 'nv', 'vasc']

        st.write(f"Prediction: \n")
        st.success( f"## {classes[np.argmax(out)]}" )

        st.write("Actual output from the model: ")
        df = pd.DataFrame(out, columns=classes)
        st.write(df)
        

    
