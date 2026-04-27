Fake News Detection Using Machine Learning and TF-IDF Text Features
Authors: Xiaoxi Gao, Zhenzhe Luo

Project Overview
----------------
This project builds a reproducible and interpretable traditional machine learning pipeline to classify news articles as Fake or True.

Label definition:
- Fake = 0
- True = 1

Main modeling choice:
- The main experiment uses article text only (text_only mode).
- The subject and date fields are kept only for bias/generalization analysis and are not used as model features.

Folder Structure
----------------
GaoXiaoxi_LuoZhenzhe/
├── data/
│   └── readme_data.txt
├── ReadMe.txt
├── main.py
└── aux_1.py

Data Setup
----------
1. Download the Fake and Real News Dataset from Kaggle:
   https://www.kaggle.com/datasets/clmentbisaillon/fake-and-real-news-dataset

2. Place the following two files inside the data/ folder:
   - data/Fake.csv
   - data/True.csv

The data files are not included in this zip file to keep the submission small and because the dataset is publicly available.
See data/readme_data.txt for detailed data instructions.

Required Packages
-----------------
Use Python 3.9+.

Install packages with:

pip install numpy pandas matplotlib scikit-learn

How to Run
----------
From inside the project folder, run:

python main.py

This will run the full experiment, including:
- Baseline Dummy Classifier
- Multinomial Naive Bayes
- Logistic Regression
- Linear SVC
- Random Forest
- Stacking Classifier

The full run can take a long time because Random Forest and Stacking are computationally expensive on high-dimensional TF-IDF features.

For a faster test run, use:

python main.py --quick

The quick mode skips Random Forest and Stacking.

Output Files
------------
The program creates an output folder:

final_results_fake_news_v4/

This folder contains model comparison tables, final evaluation reports, confusion matrix, ROC curve, bootstrap confidence intervals, interpretability output, error analysis, and bias analysis.

Model Selection Rule
--------------------
The best model is selected using CV Macro F1 on the training set. The held-out test set is used only once for final evaluation.

Important Notes
---------------
- TF-IDF is fit inside each sklearn Pipeline to avoid data leakage.
- Macro F1 is emphasized because it treats Fake and True classes equally.
- This is a text classification model, not a real fact-checking system.
