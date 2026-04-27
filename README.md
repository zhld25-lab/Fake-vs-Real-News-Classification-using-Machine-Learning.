# Fake vs Real News Classification using Machine Learning

This repository is the official clean version of a course project for fake vs real news classification. It contains a traditional machine learning pipeline, command-line training and prediction scripts, and an interactive Streamlit website for project review.

## Project Type

<<<<<<< HEAD
- Task: binary text classification
- Fake news label: `0`
- Real news label: `1`
- Methods: traditional machine learning only
- Deep learning is not used: no BERT, Transformer, LSTM, CNN, TensorFlow, or PyTorch
=======
This project develops a machine learning system that classifies news articles as **fake news or real news** based on their textual content. The system processes raw news data, applies text preprocessing, extracts features using **TF-IDF vectorization**, and trains machine learning models to perform binary classification.

The project focuses on classical machine learning methods combined with statistical evaluation techniques to build a reliable and interpretable fake news detection pipeline.

---

## Streamlit Web App

This repository includes a Streamlit web application for interactive fake news prediction.

The app includes these pages:

- Home
- Interactive Prediction
- Model Performance
- Confusion Matrix
- Classification Report
- Bootstrap Confidence Intervals
- Submission Information

Run locally:

```bash
pip install -r requirements.txt
streamlit run app.py
```

For public deployment, use Streamlit Community Cloud:

1. Go to `https://share.streamlit.io`.
2. Create a new app from this GitHub repository.
3. Select branch `main`.
4. Set the main file path to `app.py`.
5. Select Python `3.10`.
6. Deploy and share the generated `streamlit.app` URL.

Prediction requires `final_model.pkl` in the repository root. If it is missing, the app will still open and show a clear warning. Export the trained model from the notebook with:

```python
import joblib
joblib.dump(best_model, "final_model.pkl")
```

---

## Problem Description

The goal of this project is to automatically determine whether a news article is real or fake using machine learning.

This is formulated as a **binary text classification problem**.

Input  
News article text

Output  

1 = Real News  
0 = Fake News

The model learns patterns in textual content that help distinguish legitimate journalism from fabricated or misleading news articles.

---

## Dataset

The dataset used in this project consists of two files:

data/raw/Fake.csv  
data/raw/True.csv

Each dataset contains news articles collected from online news sources.

Typical attributes include:

- title
- text
- subject
- date

The datasets are merged and labeled as follows:

Fake News → label = 0  
Real News → label = 1

The title and text fields are combined to form a single text feature used for model training.

---

## Data Preprocessing

Before training the model, several preprocessing steps are applied to the raw text data.

Text preprocessing includes:

- Convert text to lowercase
- Remove URLs
- Remove punctuation and special characters
- Remove extra whitespace
- Remove empty rows

These steps help clean the text data and improve model performance.

---

## Feature Engineering

Text data is converted into numerical features using **TF-IDF (Term Frequency – Inverse Document Frequency)**.

TF-IDF measures the importance of a word in a document relative to the entire corpus.

The vectorization process includes:

- Stopword removal
- N-gram representation
- Vocabulary size control

TF-IDF converts each document into a numerical feature vector that can be used by machine learning models.

---

## Baseline Solution

A baseline model is used as a reference point for evaluating machine learning performance.

The baseline approach in this project is **Naive Bayes**, which is commonly used for text classification tasks.

Naive Bayes is simple, efficient, and provides a good starting point for evaluating more advanced machine learning models.

---

## Machine Learning Model

The main model used in this project is **Logistic Regression**, which is widely used for binary classification problems.

The model is trained using TF-IDF features extracted from the news articles.

Logistic Regression is chosen because it performs well on high-dimensional text data and provides interpretable results.

---

## Statistical Model Components

To ensure reliable evaluation of model performance, statistical methods are applied.

### Cross Validation

A **5-fold cross validation** strategy is used during training.

This helps estimate the model's generalization performance and reduces the risk of overfitting.

### Evaluation Metrics

Model performance is evaluated using the following metrics:

- Accuracy
- Precision
- Recall
- F1 Score

Among these metrics, **F1 Score** is used as the main evaluation metric because it balances precision and recall.

### Bootstrap Confidence Interval

Bootstrap resampling is used to estimate a **confidence interval for the F1 score**, providing a statistical measure of model reliability.

---
>>>>>>> 510ae17251100941bd544b6b6caf5502af649133

## Project Structure

```text
fake-real-news-ml/
├── app.py
├── train_model.py
├── predict.py
├── requirements.txt
├── README.md
├── .gitignore
├── data/
│   ├── Fake.csv
│   └── True.csv
├── models/
├── outputs/
└── src/
    ├── data_utils.py
    ├── text_preprocessing.py
    ├── model_training.py
    ├── evaluation.py
    └── visualization.py
```

## Dataset

The official dataset files for this version are:

- `data/Fake.csv`
- `data/True.csv`

The loader standardizes the data into a consistent format with `title`, `text`, `subject`, `date`, `label`, `label_name`, and `source_file`.

## Pipeline

The main modeling pipeline is:

```text
load data -> clean text -> train/test split -> TF-IDF vectorization -> model comparison -> final evaluation -> bootstrap confidence intervals
```

TF-IDF is kept inside the scikit-learn `Pipeline`. This matters because cross-validation fits TF-IDF only on each training fold, which helps avoid data leakage.

## Install Dependencies

```bash
pip install -r requirements.txt
```

## Train the Model

```bash
python train_model.py
```

This command trains traditional machine learning models, compares them with cross-validation Macro F1, evaluates the selected model on the test set, and saves:

- `models/final_model.pkl`
- `outputs/model_comparison.csv`
- `outputs/classification_report.txt`
- `outputs/confusion_matrix.csv`
- `outputs/bootstrap_confidence_intervals.txt`
- optional evaluation images

This clean version includes a saved `models/final_model.pkl` so the website prediction page can work after deployment. Re-run `python train_model.py` if you want to regenerate the model from the CSV data.

To also train the stacking ensemble:

```bash
python train_model.py --include-stacking
```

## Predict from Command Line

```bash
python predict.py --text "Your news headline or article text here"
```

The prediction uses the saved `models/final_model.pkl` pipeline.

## Run the Interactive Website

```bash
streamlit run app.py
```

The website includes:

- project overview
- dataset explorer
- methodology explanation
- training and artifact status
- evaluation dashboard
- interactive prediction page
- limitations and future work

If `models/final_model.pkl` is missing, the website still opens and clearly explains how to train and save the model.

## Evaluation Approach

The project reports:

- Accuracy
- Macro F1-score
- Weighted F1-score
- Classification report
- Confusion matrix
- ROC curve and AUC when model scores are available
- Bootstrap confidence intervals for final metrics

High same-dataset performance should be interpreted carefully. Strong results on one dataset do not automatically prove real-world generalization. The model may learn topic, source, or writing-style patterns rather than factual correctness.

## Limitations

This project is a text-pattern classifier, not a factual verification system. It cannot directly check whether claims are true. It may struggle with partially true news, mixed claims, satire, short headlines, and articles from sources that differ from the training data.

Recommended future work includes external dataset testing, source-based or time-based splits, more diverse datasets, non-deep-learning embeddings such as Word2Vec features, and optional fact-checking API integration as a separate evidence layer.

## Removed Outdated Files

The previous repository version included old notebooks, old result images, old text reports, duplicated raw data folders, and temporary outputs. Those files were removed because this version reorganizes the repository into a clean submission structure with reproducible scripts and a complete interactive website.
