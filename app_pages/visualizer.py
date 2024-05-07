import streamlit as st
import os
import random as rn
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style("white")
from matplotlib.image import imread


def visualizer():
    st.write("## Sample Visualizer")

    os.chdir(os.path.expanduser('~'))
    os.chdir('Desktop/skin')

    train_dir = 'inputs/work/train'
    test_dir = 'inputs/work/test'
    val_dir = 'inputs/work/validate'

    subdirs = [subdir for subdir in os.listdir(train_dir) if os.path.isdir(os.path.join(train_dir, subdir))]

    for subdir in enumerate(subdirs):
        fig, axs = plt.subplots(1, 5, figsize=(20, 20))
        img_files = [img_file for img_file in os.listdir(os.path.join(train_dir, subdir)) if img_file.endswith('.jpg')]
        for j in range(5):
            img = imread(os.path.join(train_dir, subdir, rn.choice(img_files)))
            axs[0, j].imshow(img)
            axs[0, j].axis('off')
            axs[0, j].set_title(subdir)
        st.write(subdir)
        st.pyplot(fig)