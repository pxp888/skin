import streamlit as st
import os
import random as rn
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# import seaborn as sns
# sns.set_style("white")
from matplotlib.image import imread


def visualizer():
    st.write("## Sample Visualizer")

    # os.chdir(os.path.expanduser('~'))
    # os.chdir('Desktop/skin')

    train_dir = 'inputs/work/test'

    fig, axes = plt.subplots(7, 5, figsize=(10, 15))
    subdirs = os.listdir(train_dir)
    for sub in subdirs:
        imfiles = os.listdir(os.path.join(train_dir, sub))
        rn.shuffle(imfiles)
        for i in range(5):
            img = imread(os.path.join(train_dir, sub, imfiles[i]))
            axes[subdirs.index(sub), i].imshow(img)
            axes[subdirs.index(sub), i].axis('off')
            axes[subdirs.index(sub), i].set_title(sub)
    plt.tight_layout()
    st.pyplot(fig)

