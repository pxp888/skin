
# Skin Cancer Detection

## Introduction
This project aims to leverage data analysis and machine learning techniques to develop a system that can automatically classify skin lesions based on digital images.

## Business Requirements
__Automated Classification__: The client desires an automated system to classify skin lesions into specific categories. This will assist medical professionals in diagnosis by identifying the type of lesion present (e.g., melanoma, benign nevus).

__Improved Diagnostic Workflow__: The client seeks to integrate this system into their existing diagnostic workflow, enabling faster and more efficient triage of patients.

## Hypothesis and Validation
We hypothesize that different skin lesions exhibit distinct visual characteristics in digital images. By analyzing these features, we can develop a model to accurately classify lesions into predefined categories. This hypothesis will be validated through experimentation with various machine learning models and evaluation on unseen test data.

### Data Visualization and Machine Learning Tasks
Data Exploration: Explore the image dataset to understand the distribution of different lesion types and potential challenges.

### Machine Learning

Develop a multi-class classification model to predict the type of skin lesion present in an image.
Generate classification reports summarizing model performance for each lesion class.


### Objective:
Develop a machine learning model to classify skin lesions into predefined categories based on digital images. This supervised learning model will be a multi-class classifier, with each class representing a specific type of cancer or lesion.

### Desired Outcome:

Equip medical staff with a tool that can assist in the diagnosis of skin lesions. The model should achieve a high accuracy (ideally above 65%) on unseen test data, particularly for differentiating between cancerous and benign lesions.

#### Model Output:
Predicted class label corresponding to the type of skin lesion present (e.g., melanoma, benign nevus).
Probability scores for each lesion class, indicating the model's confidence in its prediction.

#### Benefits:
Improve diagnostic accuracy and efficiency by leveraging machine learning for lesion classification.

Assist medical professionals in prioritizing cases and making informed decisions.

Reduce reliance on subjective visual assessment, potentially leading to a more consistent diagnostic approach.

#### Heuristics:
Current skin lesion diagnosis often relies on visual examination by medical professionals.  This approach can be time-consuming and subjective, leading to potential for misdiagnosis.

### Data Acquisition:
The training data will be sourced from the National Institutes of Health (NIH) website, specifically a subset of 5643 images downloaded for efficient model training. This dataset will contain images of various skin lesions with corresponding labels indicating their type.

### Features and Target Variables:

Features: Image data representing skin lesions.

Target Variable: Categorical label indicating the specific type of skin lesion present.



Next Steps:


* Data exploration and pre-processing.
* Feature engineering (if necessary).
* Model selection and training.
* Model evaluation and optimization.
* Deployment and integration into a diagnostic tool.



<br>



## Dataset Content

A training set for academic machine learning can be created using the dataset, which comprises of 10015 images. Several diagnostic categories for cancers or lesions are represented in the dataset:

* Actinic keratoses and intraepithelial carcinoma / Bowen's disease (__akiec__)
* basal cell carcinoma (__bcc__)
* benign keratosis-like lesions (solar lentigines / seborrheic keratoses and lichen-planus like keratoses, __bkl__)
* dermatofibroma (__df__)
* melanoma (__mel__)
* melanocytic nevi (__nv__)
* vascular lesions (angiomas, angiokeratomas, pyogenic granulomas and hemorrhage, __vasc__).

These classes are not evenly represented in the dataset, as the table below shows.

### Class Distribution

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

  <br>

## Caveat
### This is a difficult data set.
While I was able to get a network to converge, the final results were never close to what I would consider usable in practice.

I'm using a relatively small CNN, which is fast to train so it makes experimentation easy, but the final test accuracy is too low to be useful for an application as serious as cancer.

However, when studying the work others have done with the same dataset on Kaggle, it becomes clear that this is a common problem even with much larger networks.

The most successful approach I saw was written by someone who seems to be an especially knowledgable author. He used a very large pre-trained model as a base model, extensive data preparation, and managed to achieve a final F1 score of 73%.

This is lower than what the same author has achieved with similar techniques on other datasets, and to my knowledge his approach represents the current state-of-the-art.

This is linked to here: [https://www.kaggle.com/code/gpiosenka/skin-cancer-f1-score-73](https://www.kaggle.com/code/gpiosenka/skin-cancer-f1-score-73)

### Possible Causes

**Uneven Class Representation**

While the dataset contains roughly ten thousand images, they are not evenly divided over the classes of interest, with some classes having as little as one hundred images.

**Possible mislabeling?**
I don't have the knowledge to check this, but it is possible that some of the samples are mislabeled which could cause issues.