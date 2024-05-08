import streamlit as st
import matplotlib.pyplot as plt


def summary_body():

    st.write("### Quick Project Summary")

    st.info(
        f"# Skin Cancer Classifier\n" 
        f"## Quick Project Summary \n"
        f"**General Information** \n"
        f"*	Skin cancer presents in many ways, etc.\n"
        f"*	blah blah blah\n"
        )

    st.write(
        f"* For additional information, please visit and **read** the "
        f"[Project README file](https://github.com/pxp888/skin/blob/main/README.md).")
    

    st.success(
        f"The project has 2 business requirements:\n"
        f"* 1 - The client is interested in having a study to differentiate "
        f"between types of skin cancers.\n"
        )
