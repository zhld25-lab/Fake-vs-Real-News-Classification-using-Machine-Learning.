README_DATA.txt
================

Project Title
-------------
Fake and True News Text Classification

Dataset Overview
----------------
This project uses two CSV files for binary news classification:

1. Fake.csv
   - Contains news articles labeled as fake news.
   - In this project, these samples are assigned label 0.

2. True.csv
   - Contains news articles labeled as true news.
   - In this project, these samples are assigned label 1.

The purpose of this dataset is to train and evaluate machine learning models that classify whether a news article is fake or true based on its text content.

Dataset Files
-------------
The dataset should be placed in the following folder:

data/
├── Fake.csv
└── True.csv

Expected Columns
----------------
Each CSV file is expected to contain the following columns:

- title: the headline or title of the news article
- text: the main body content of the news article
- subject: the news category or topic
- date: the publication date of the article

Important Note About Feature Selection
--------------------------------------
Although the dataset includes title, subject, and date columns, the final model in this project only uses the text field for training and prediction.

The subject feature was not used because it may provide overly strong clues about the label and could potentially cause feature leakage. To make the classification task more realistic and fair, the model focuses only on the article text.

Label Definition
----------------
After loading the data:

- Fake.csv articles are labeled as 0
- True.csv articles are labeled as 1

The two datasets are then combined into one binary classification dataset.

Data Preprocessing
------------------
The preprocessing pipeline includes:

1. Loading Fake.csv and True.csv
2. Adding binary labels to each dataset
3. Combining the fake and true news samples
4. Keeping the text column as the main input feature
5. Cleaning and normalizing text when needed
6. Splitting the data into training and testing sets
7. Converting text into numerical features using text vectorization methods
8. Training and evaluating classification models

Usage
-----
To use the dataset, make sure the two CSV files are stored inside the data/ folder before running the training script.

Example project structure:

project/
├── data/
│   ├── Fake.csv
│   └── True.csv
├── src/
├── train_model.py
├── predict.py
├── app.py
├── requirements.txt
└── README_DATA.txt

Dataset Purpose
---------------
This dataset is used for academic and experimental purposes in a fake news detection project. The goal is to compare machine learning models and evaluate their ability to distinguish fake news from true news using textual information.

Model Input
-----------
Final model input:

- text

Excluded columns:

- title
- subject
- date

Reason for excluding subject:
The subject column may be too strongly associated with the class label, which could make the model rely on dataset-specific patterns rather than learning generalizable language features.

Output Label
------------
The target variable is a binary label:

- 0 = Fake news
- 1 = True news

Notes for GitHub Submission
---------------------------
If the data files are too large for regular GitHub upload, consider using Git Large File Storage (Git LFS) or uploading only a small sample dataset. Do not upload unnecessary temporary files, cache files, or model output files into the data folder.

Recommended files to include in data/:

- Fake.csv
- True.csv
- README_DATA.txt

Recommended files not to include in data/:

- model files
- output figures
- cache folders
- temporary files
- notebook checkpoint folders

License and Source
------------------
Please cite the original dataset source if required by the course or dataset provider. This README only describes how the dataset is used in this project.
