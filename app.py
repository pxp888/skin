import streamlit as st
from app_pages.multipage import MultiPage

from app_pages.page_summary import summary_body
from app_pages.visualizer import visualizer
from app_pages.finder import Finder

# from app_pages.page_cells_visualizer import page_cells_visualizer_body
# from app_pages.page_malaria_detector import page_malaria_detector_body
# from app_pages.page_project_hypothesis import page_project_hypothesis_body
# from app_pages.page_ml_performance import page_ml_performance_metrics

app = MultiPage(app_name= "Skin Cancer Classifier")

app.add_page("Quick Project Summary", summary_body)
app.add_page("Visualizer", visualizer)
app.add_page("Finder", Finder)

# app.add_page("Malaria Detection", page_malaria_detector_body)
# app.add_page("Project Hypothesis", page_project_hypothesis_body)
# app.add_page("ML Performance Metrics", page_ml_performance_metrics)

app.run()