<<<<<<< HEAD
from __future__ import annotations

from pathlib import Path

import joblib
import pandas as pd
import streamlit as st

from src.data_utils import LABEL_NAMES, dataset_summary, load_news_data
from src.evaluation import model_scores
from src.text_preprocessing import clean_text


ROOT = Path(__file__).resolve().parent
DATA_DIR = ROOT / "data"
MODELS_DIR = ROOT / "models"
OUTPUTS_DIR = ROOT / "outputs"
MODEL_PATH = MODELS_DIR / "final_model.pkl"


st.set_page_config(
    page_title="Fake vs Real News Classification",
=======
import re
from pathlib import Path
from typing import Any

import joblib
import numpy as np
import pandas as pd
import streamlit as st


APP_DIR = Path(__file__).resolve().parent
MODEL_PATH = APP_DIR / "final_model.pkl"
ROC_CURVE_PATH = APP_DIR / "roc_curve_final_model.png"
CONFUSION_MATRIX_IMAGE_PATH = APP_DIR / "confusion_matrix_final_model.png"

MODEL_EXPORT_SNIPPET = """import joblib
joblib.dump(best_model, "final_model.pkl")"""

PERFORMANCE = {
    "Final Model": "Stacking",
    "Accuracy": 0.9994,
    "Macro F1-score": 0.9994,
    "Wrong Predictions": "5 / 8935",
}

CONFUSION_MATRIX = pd.DataFrame(
    [[4690, 4], [1, 4240]],
    index=["Actual Fake", "Actual True"],
    columns=["Predicted Fake", "Predicted True"],
)

CLASSIFICATION_REPORT = pd.DataFrame(
    [
        {"Class": "Fake", "Precision": 0.9998, "Recall": 0.9991, "F1-score": 0.9995, "Support": 4694},
        {"Class": "True", "Precision": 0.9991, "Recall": 0.9998, "F1-score": 0.9994, "Support": 4241},
        {"Class": "Accuracy", "Precision": np.nan, "Recall": np.nan, "F1-score": 0.9994, "Support": 8935},
        {"Class": "Macro avg", "Precision": 0.9994, "Recall": 0.9995, "F1-score": 0.9994, "Support": 8935},
        {"Class": "Weighted avg", "Precision": 0.9994, "Recall": 0.9994, "F1-score": 0.9994, "Support": 8935},
    ]
)

BOOTSTRAP_INTERVALS = pd.DataFrame(
    [
        {"Metric": "Accuracy", "Mean": 0.9994, "95% CI Lower": 0.9989, "95% CI Upper": 0.9999},
        {"Metric": "F1 Score", "Mean": 0.9994, "95% CI Lower": 0.9988, "95% CI Upper": 0.9999},
    ]
)

PAGES = [
    "Home",
    "Interactive Prediction",
    "Model Performance",
    "Confusion Matrix",
    "Classification Report",
    "Bootstrap Confidence Intervals",
    "Submission Information",
]


st.set_page_config(
    page_title="Fake vs Real News Detector",
    page_icon="NEWS",
>>>>>>> 510ae17251100941bd544b6b6caf5502af649133
    layout="wide",
    initial_sidebar_state="expanded",
)


<<<<<<< HEAD
st.markdown(
    """
    <style>
    .block-container {
        padding-top: 2rem;
        padding-bottom: 3rem;
        max-width: 1180px;
    }
    h1, h2, h3 {
        letter-spacing: 0;
    }
    .site-note {
        border-left: 4px solid #2563eb;
        padding: 0.75rem 1rem;
        background: #f8fafc;
        color: #334155;
        margin: 1rem 0;
    }
    .small-muted {
        color: #64748b;
        font-size: 0.92rem;
    }
    div[data-testid="stMetric"] {
        background: #ffffff;
        border: 1px solid #e2e8f0;
        border-radius: 8px;
        padding: 0.9rem 1rem;
    }
    </style>
    """,
    unsafe_allow_html=True,
)


@st.cache_data(show_spinner=False)
def load_dataset() -> pd.DataFrame:
    return load_news_data(DATA_DIR / "Fake.csv", DATA_DIR / "True.csv")


@st.cache_resource(show_spinner=False)
def load_model():
    if not MODEL_PATH.exists():
        return None
    return joblib.load(MODEL_PATH)


def page_header(title: str, subtitle: str | None = None) -> None:
    st.title(title)
    if subtitle:
        st.write(subtitle)


def model_status_box(model) -> None:
    if model is None:
        st.warning(
            "No trained model file found yet. Train and save the pipeline first with "
            "`python train_model.py`, then refresh this page."
        )
    else:
        st.success("Loaded `models/final_model.pkl`. The interactive classifier is ready.")


def read_csv_if_exists(path: Path) -> pd.DataFrame | None:
    if not path.exists():
        return None
    try:
        return pd.read_csv(path)
    except Exception:
        return None


def show_home() -> None:
    page_header(
        "Fake vs Real News Classification using Machine Learning",
        "An interactive academic project website for binary news text classification.",
    )
    st.markdown(
        """
        <div class="site-note">
        This project classifies news articles into two labels: <b>Fake News = 0</b>
        and <b>Real News = 1</b>. It uses traditional machine learning only:
        text cleaning, TF-IDF vectorization, cross-validation, model comparison,
        error analysis, and confidence interval reporting.
        </div>
=======
def apply_theme() -> None:
    st.markdown(
        """
        <style>
            .block-container {
                padding-top: 2rem;
                padding-bottom: 2.5rem;
                max-width: 1180px;
            }
            h1, h2, h3 {
                letter-spacing: 0;
            }
            [data-testid="stSidebar"] {
                border-right: 1px solid rgba(49, 51, 63, 0.12);
            }
            [data-testid="stMetric"] {
                background: #ffffff;
                border: 1px solid rgba(49, 51, 63, 0.12);
                border-radius: 8px;
                padding: 1rem;
                box-shadow: 0 1px 2px rgba(0, 0, 0, 0.04);
            }
            div.stButton > button {
                width: 100%;
                border-radius: 8px;
                font-weight: 700;
                padding: 0.65rem 1rem;
            }
            .status-panel {
                border: 1px solid rgba(49, 51, 63, 0.12);
                border-radius: 8px;
                padding: 1rem;
                background: #f8fafc;
            }
            .result-panel {
                border: 1px solid rgba(49, 51, 63, 0.12);
                border-radius: 8px;
                padding: 1.25rem;
                background: #ffffff;
                box-shadow: 0 1px 3px rgba(0, 0, 0, 0.06);
            }
        </style>
>>>>>>> 510ae17251100941bd544b6b6caf5502af649133
        """,
        unsafe_allow_html=True,
    )

<<<<<<< HEAD
    col1, col2, col3 = st.columns(3)
    col1.metric("Task", "Binary Classification")
    col2.metric("Text Features", "TF-IDF")
    col3.metric("Model Type", "Traditional ML")

    st.subheader("Team Members")
    st.write("Xiaoxi Gao and Zhenzhe Luo")

    st.subheader("Motivation")
    st.write(
        "Fake news detection is an important text classification problem because online "
        "news can spread quickly and influence public understanding. This project does "
        "not perform real fact-checking. Instead, it studies whether traditional machine "
        "learning models can learn text-pattern differences between fake and real news "
        "articles in the provided dataset."
    )

    st.subheader("Repository Workflow")
    st.code(
        "pip install -r requirements.txt\n"
        "python train_model.py\n"
        "streamlit run app.py",
        language="bash",
    )


def show_dataset() -> None:
    page_header("Dataset Explorer", "Inspect the official project dataset used by this version.")
    try:
        df = load_dataset()
    except Exception as exc:
        st.error(f"Dataset could not be loaded: {exc}")
        st.info("Expected files: `data/Fake.csv` and `data/True.csv`.")
        return

    summary = dataset_summary(df)
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Rows", f"{summary['rows']:,}")
    col2.metric("Columns", len(summary["columns"]))
    col3.metric("Fake Rows", f"{summary['label_counts'].get('Fake News', 0):,}")
    col4.metric("Real Rows", f"{summary['label_counts'].get('Real News', 0):,}")

    st.subheader("Label Mapping")
    st.dataframe(
        pd.DataFrame(
            [
                {"Label Name": "Fake News", "Numeric Label": 0},
                {"Label Name": "Real News", "Numeric Label": 1},
            ]
        ),
        use_container_width=True,
        hide_index=True,
    )

    st.subheader("Class Distribution")
    counts = df["label_name"].value_counts().rename_axis("Class").reset_index(name="Count")
    st.bar_chart(counts, x="Class", y="Count", use_container_width=True)

    st.subheader("Data Preview")
    label_filter = st.multiselect(
        "Filter by label",
        options=sorted(df["label_name"].unique()),
        default=sorted(df["label_name"].unique()),
    )
    subject_values = sorted([value for value in df["subject"].dropna().unique() if str(value).strip()])
    subject_filter = st.multiselect("Filter by subject", options=subject_values, default=[])
    preview_df = df[df["label_name"].isin(label_filter)]
    if subject_filter:
        preview_df = preview_df[preview_df["subject"].isin(subject_filter)]
    st.dataframe(
        preview_df[["title", "text", "subject", "date", "label_name"]].head(100),
        use_container_width=True,
        hide_index=True,
    )

    with st.expander("Dataset design note"):
        st.write(
            "This cleaned project version keeps the official source files as `data/Fake.csv` "
            "and `data/True.csv`. The training code standardizes fields into title, text, "
            "subject, date, label, label_name, and source_file."
        )


def show_methodology() -> None:
    page_header("Methodology", "A transparent traditional machine learning pipeline.")
    steps = pd.DataFrame(
        [
            {
                "Step": "Text cleaning",
                "Purpose": "Remove URLs, HTML tags, non-letter characters, casing differences, and extra spaces.",
            },
            {
                "Step": "Tokenization",
                "Purpose": "Handled by TF-IDF vectorizer after text normalization.",
            },
            {
                "Step": "TF-IDF vectorization",
                "Purpose": "Convert article text into weighted word and phrase features.",
            },
            {
                "Step": "Traditional ML models",
                "Purpose": "Compare Naive Bayes, Logistic Regression, Linear SVM, and optional Stacking.",
            },
            {
                "Step": "Cross-validation",
                "Purpose": "Estimate model performance on training folds before final test evaluation.",
            },
            {
                "Step": "Bootstrap intervals",
                "Purpose": "Estimate uncertainty around final accuracy and Macro F1.",
            },
            {
                "Step": "Error analysis",
                "Purpose": "Review wrong predictions and discuss dataset bias/generalization limits.",
            },
        ]
    )
    st.dataframe(steps, use_container_width=True, hide_index=True)

    st.info(
        "TF-IDF is kept inside the sklearn Pipeline. This is important because each "
        "cross-validation fold fits TF-IDF only on its training portion, reducing data leakage."
    )

    with st.expander("Why no deep learning?"):
        st.write(
            "The project requirement is traditional machine learning only. This version does "
            "not use BERT, Transformers, LSTM, CNN, TensorFlow, or PyTorch."
        )


def show_training() -> None:
    page_header("Training & Model Artifacts", "Generate the saved pipeline used by the website.")
    model = load_model()
    model_status_box(model)

    st.subheader("Train the Final Pipeline")
    st.code("python train_model.py", language="bash")
    st.write(
        "The command loads `data/Fake.csv` and `data/True.csv`, cleans text, performs "
        "a stratified split, compares models with cross-validation, saves evaluation "
        "outputs, and writes `models/final_model.pkl`."
    )

    st.subheader("Optional Stacking Run")
    st.code("python train_model.py --include-stacking", language="bash")
    st.write(
        "Stacking is slower, but it is still a traditional machine learning ensemble."
    )

    artifacts = pd.DataFrame(
        [
            {"File": "models/final_model.pkl", "Status": "Found" if MODEL_PATH.exists() else "Missing"},
            {
                "File": "outputs/model_comparison.csv",
                "Status": "Found" if (OUTPUTS_DIR / "model_comparison.csv").exists() else "Missing",
            },
            {
                "File": "outputs/classification_report.txt",
                "Status": "Found" if (OUTPUTS_DIR / "classification_report.txt").exists() else "Missing",
            },
            {
                "File": "outputs/confusion_matrix.csv",
                "Status": "Found" if (OUTPUTS_DIR / "confusion_matrix.csv").exists() else "Missing",
            },
        ]
    )
    st.dataframe(artifacts, use_container_width=True, hide_index=True)


def show_results() -> None:
    page_header("Evaluation Dashboard", "Model comparison and final evaluation outputs.")
    comparison = read_csv_if_exists(OUTPUTS_DIR / "model_comparison.csv")
    if comparison is None:
        st.warning("No saved evaluation table found yet. Run `python train_model.py` first.")
        st.write("After training, this page will display model comparison results and final metrics.")
    else:
        st.subheader("Model Comparison")
        st.dataframe(comparison.round(4), use_container_width=True, hide_index=True)
        best = comparison.sort_values("CV_Macro_F1_Mean", ascending=False).iloc[0]
        col1, col2, col3 = st.columns(3)
        col1.metric("Best Model", str(best["Model"]))
        col2.metric("CV Macro F1", f"{best['CV_Macro_F1_Mean']:.4f}")
        col3.metric("Test Macro F1", f"{best['Test_Macro_F1']:.4f}")

    matrix = read_csv_if_exists(OUTPUTS_DIR / "confusion_matrix.csv")
    if matrix is not None:
        st.subheader("Confusion Matrix")
        st.dataframe(matrix, use_container_width=True, hide_index=True)

    report_path = OUTPUTS_DIR / "classification_report.txt"
    if report_path.exists():
        st.subheader("Classification Report")
        st.code(report_path.read_text(encoding="utf-8"), language="text")

    bootstrap_path = OUTPUTS_DIR / "bootstrap_confidence_intervals.txt"
    if bootstrap_path.exists():
        st.subheader("Bootstrap Confidence Intervals")
        st.code(bootstrap_path.read_text(encoding="utf-8"), language="text")

    roc_path = OUTPUTS_DIR / "roc_curve.png"
    cm_path = OUTPUTS_DIR / "confusion_matrix.png"
    image_cols = st.columns(2)
    if roc_path.exists():
        image_cols[0].image(str(roc_path), caption="ROC Curve", use_container_width=True)
    if cm_path.exists():
        image_cols[1].image(str(cm_path), caption="Confusion Matrix", use_container_width=True)

    st.info(
        "High same-dataset F1 should be interpreted carefully. Strong test performance on "
        "one dataset does not automatically prove real-world generalization."
    )


def show_prediction() -> None:
    page_header(
        "Interactive Prediction",
        "Paste a headline or article and classify it with the saved traditional ML pipeline.",
    )
    model = load_model()
    model_status_box(model)
=======

@st.cache_resource(show_spinner=False)
def load_trained_model() -> tuple[Any | None, str | None]:
    if not MODEL_PATH.exists():
        return None, "missing"

    try:
        return joblib.load(MODEL_PATH), None
    except Exception as exc:
        return None, f"load_error: {exc}"


def clean_text(text: str) -> str:
    text = re.sub(r"https?://\S+|www\.\S+", " ", text)
    text = re.sub(r"<.*?>", " ", text)
    text = text.lower()
    text = re.sub(r"[^a-z\s]", " ", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text


def format_confusion_matrix() -> pd.DataFrame:
    return CONFUSION_MATRIX.apply(lambda column: column.map(lambda value: f"{int(value):,}"))


def format_classification_report() -> pd.DataFrame:
    report = CLASSIFICATION_REPORT.copy()
    for column in ["Precision", "Recall", "F1-score"]:
        report[column] = report[column].map(lambda value: "" if pd.isna(value) else f"{value:.4f}")
    report["Support"] = report["Support"].map(lambda value: f"{int(value):,}")
    return report


def format_bootstrap_intervals() -> pd.DataFrame:
    intervals = BOOTSTRAP_INTERVALS.copy()
    for column in ["Mean", "95% CI Lower", "95% CI Upper"]:
        intervals[column] = intervals[column].map(lambda value: f"{value:.4f}")
    return intervals


def label_to_text(label: Any) -> str:
    normalized = str(label).strip().lower()
    if normalized in {"0", "fake", "fake news"}:
        return "Fake News"
    if normalized in {"1", "true", "true news", "real", "real news"}:
        return "True News"
    return "True News" if bool(label) else "Fake News"


def prediction_confidence(model: Any, cleaned_text: str, predicted_label: Any) -> float | None:
    if not hasattr(model, "predict_proba"):
        return None

    try:
        probabilities = model.predict_proba([cleaned_text])[0]
    except Exception:
        return None

    classes = getattr(model, "classes_", None)
    if classes is not None:
        for index, class_label in enumerate(classes):
            if str(class_label) == str(predicted_label):
                return float(probabilities[index])

    try:
        label_index = int(predicted_label)
        if 0 <= label_index < len(probabilities):
            return float(probabilities[label_index])
    except (TypeError, ValueError):
        pass

    return float(np.max(probabilities))


def show_model_status(model: Any | None, model_error: str | None) -> None:
    if model is not None:
        st.success("final_model.pkl loaded successfully. The prediction page is ready.")
        return

    if model_error == "missing":
        st.warning(
            "final_model.pkl was not found. Export the trained model from the notebook and place it "
            "next to app.py before running predictions."
        )
        st.code(MODEL_EXPORT_SNIPPET, language="python")
        return

    st.error("final_model.pkl exists, but Streamlit could not load it.")
    st.caption(model_error.replace("load_error: ", "") if model_error else "Unknown model loading error.")


def render_header(title: str, caption: str) -> None:
    st.title(title)
    st.caption(caption)


def render_home(model: Any | None, model_error: str | None) -> None:
    render_header(
        "Fake vs Real News Detector",
        "Interactive Streamlit application for classifying news text with a trained machine learning model.",
    )

    metric_cols = st.columns(4)
    metric_cols[0].metric("Final Model", PERFORMANCE["Final Model"])
    metric_cols[1].metric("Accuracy", f"{PERFORMANCE['Accuracy']:.4f}")
    metric_cols[2].metric("Macro F1-score", f"{PERFORMANCE['Macro F1-score']:.4f}")
    metric_cols[3].metric("Wrong Predictions", PERFORMANCE["Wrong Predictions"])

    st.divider()

    left, right = st.columns([1.25, 1])
    with left:
        st.subheader("Application Overview")
        st.write(
            "Use the sidebar to review model performance, inspect evaluation tables, and run an "
            "interactive fake news prediction on a headline or full article."
        )
        with st.expander("Text preprocessing used before prediction", expanded=True):
            st.write(
                "The app removes URLs and HTML tags, lowercases text, removes non-letter characters, "
                "and normalizes extra whitespace before passing the cleaned text to the model."
            )
    with right:
        st.subheader("Model Status")
        show_model_status(model, model_error)


def render_prediction(model: Any | None, model_error: str | None) -> None:
    render_header(
        "Interactive Prediction",
        "Enter a headline or article, then classify it as Fake News or True News.",
    )

    show_model_status(model, model_error)
>>>>>>> 510ae17251100941bd544b6b6caf5502af649133

    user_text = st.text_area(
        "News headline or article",
        height=220,
<<<<<<< HEAD
        placeholder="Paste a news headline or article here...",
    )

    col1, col2 = st.columns([1, 3])
    predict_clicked = col1.button("Predict", type="primary", use_container_width=True)
    col2.caption("The app cleans the input text before passing it into the saved TF-IDF + classifier pipeline.")

    with st.expander("Preview the cleaning rules"):
        st.write("Remove URLs, remove HTML tags, lowercase, remove non-letter characters, remove extra spaces.")
        if user_text:
            st.code(clean_text(user_text), language="text")

    if predict_clicked:
        if model is None:
            st.error("Prediction is unavailable until `models/final_model.pkl` is created.")
            st.code("python train_model.py", language="bash")
            return
        if not user_text.strip():
            st.warning("Please enter a headline or article first.")
            return

        cleaned = clean_text(user_text)
        prediction = int(model.predict([cleaned])[0])
        score = model_scores(model, [cleaned])
        label = LABEL_NAMES.get(prediction, str(prediction))

        if prediction == 0:
            st.error(f"Predicted label: {label}")
        else:
            st.success(f"Predicted label: {label}")

        if score is not None:
            value = float(score[0])
            if hasattr(model, "predict_proba"):
                confidence = value if prediction == 1 else 1 - value
                st.metric("Confidence", f"{confidence:.2%}")
                st.caption(f"Real-news probability: {value:.4f}")
            else:
                st.metric("Decision score", f"{value:.4f}")

        st.info(
            "This prediction is based on learned text patterns, not direct factual verification. "
            "A real article can still be misclassified if its wording resembles patterns learned "
            "from fake-news examples, or if the dataset contains source/style bias."
        )


def show_limitations() -> None:
    page_header("Limitations & Future Work", "How to interpret this project responsibly.")
    st.subheader("Limitations")
    limitations = [
        "This is a text classification system, not a real fact-checking system.",
        "It cannot directly verify factual correctness against external evidence.",
        "It may learn source-specific, topic-specific, or writing-style patterns.",
        "It may struggle with partially true, mixed, satire, or very short news text.",
        "Performance on the same dataset may overestimate real-world generalization.",
    ]
    for item in limitations:
        st.write(f"- {item}")

    st.subheader("Future Work")
    future = [
        "Evaluate on external datasets not used during model development.",
        "Use source-based or time-based train/test splits.",
        "Add more diverse news sources and publication periods.",
        "Try non-deep-learning text representations such as Word2Vec features.",
        "Add metadata features such as source credibility, author, or date.",
        "Optionally integrate a fact-checking API as a separate evidence layer.",
    ]
    for item in future:
        st.write(f"- {item}")


def main() -> None:
    st.sidebar.title("News Classification")
    st.sidebar.caption("Traditional machine learning project website")
    pages = {
        "Home": show_home,
        "Dataset Explorer": show_dataset,
        "Methodology": show_methodology,
        "Training & Artifacts": show_training,
        "Evaluation Dashboard": show_results,
        "Interactive Prediction": show_prediction,
        "Limitations & Future Work": show_limitations,
    }
    selected = st.sidebar.radio("Pages", list(pages.keys()))

    st.sidebar.divider()
    if MODEL_PATH.exists():
        st.sidebar.success("Model file found")
    else:
        st.sidebar.warning("Model file missing")
    st.sidebar.caption("Label convention: Fake News = 0, Real News = 1")

    pages[selected]()
=======
        placeholder="Paste a news headline or article text here...",
    )

    predict_clicked = st.button("Predict", type="primary")

    if not predict_clicked:
        with st.expander("Preview the cleaning rules"):
            st.write("URLs, HTML tags, punctuation, digits, and extra spaces are removed before prediction.")
        return

    if model is None:
        st.warning("Prediction is unavailable until final_model.pkl is added and loaded successfully.")
        return

    cleaned = clean_text(user_text)
    if not cleaned:
        st.warning("Please enter text with at least a few alphabetic words before predicting.")
        return

    try:
        predicted_label = model.predict([cleaned])[0]
        result = label_to_text(predicted_label)
        confidence = prediction_confidence(model, cleaned, predicted_label)
    except Exception as exc:
        st.error("The model could not make a prediction for this input.")
        st.caption(str(exc))
        return

    result_cols = st.columns([1, 1])
    with result_cols[0]:
        if result == "True News":
            st.success(result)
        else:
            st.error(result)
    with result_cols[1]:
        if confidence is not None:
            st.metric("Confidence", f"{confidence:.2%}")
        else:
            st.info("This model does not expose predict_proba, so no confidence score is available.")

    with st.expander("Cleaned text sent to the model", expanded=False):
        st.write(cleaned)


def render_performance() -> None:
    render_header(
        "Model Performance",
        "Summary metrics for the final trained stacking model.",
    )

    cols = st.columns(4)
    cols[0].metric("Final Model", PERFORMANCE["Final Model"])
    cols[1].metric("Accuracy", f"{PERFORMANCE['Accuracy']:.4f}")
    cols[2].metric("Macro F1-score", f"{PERFORMANCE['Macro F1-score']:.4f}")
    cols[3].metric("Wrong Predictions", PERFORMANCE["Wrong Predictions"])

    performance_table = pd.DataFrame(
        [
            {"Metric": "Final Model", "Value": PERFORMANCE["Final Model"]},
            {"Metric": "Accuracy", "Value": f"{PERFORMANCE['Accuracy']:.4f}"},
            {"Metric": "Macro F1-score", "Value": f"{PERFORMANCE['Macro F1-score']:.4f}"},
            {"Metric": "Wrong Predictions", "Value": PERFORMANCE["Wrong Predictions"]},
        ]
    )
    st.subheader("Performance Table")
    st.dataframe(performance_table, hide_index=True, width="stretch")

    st.subheader("ROC Curve")
    if ROC_CURVE_PATH.exists():
        st.image(str(ROC_CURVE_PATH), caption="ROC Curve - Final Model", width="stretch")
    else:
        st.info("roc_curve_final_model.png was not found, so the ROC curve image is hidden.")


def render_confusion_matrix() -> None:
    render_header(
        "Confusion Matrix",
        "Prediction counts split by actual and predicted class.",
    )

    correct = int(CONFUSION_MATRIX.loc["Actual Fake", "Predicted Fake"] + CONFUSION_MATRIX.loc["Actual True", "Predicted True"])
    total = int(CONFUSION_MATRIX.to_numpy().sum())
    mistakes = total - correct

    cols = st.columns(3)
    cols[0].metric("Correct Predictions", f"{correct:,}")
    cols[1].metric("Wrong Predictions", f"{mistakes:,}")
    cols[2].metric("Total Samples", f"{total:,}")

    st.subheader("Matrix")
    st.dataframe(format_confusion_matrix(), width="stretch")

    if CONFUSION_MATRIX_IMAGE_PATH.exists():
        with st.expander("View confusion matrix image"):
            st.image(
                str(CONFUSION_MATRIX_IMAGE_PATH),
                caption="Confusion Matrix - Final Model",
                width="stretch",
            )

    with st.expander("Raw values"):
        st.write("Actual Fake predicted Fake: 4690")
        st.write("Actual Fake predicted True: 4")
        st.write("Actual True predicted Fake: 1")
        st.write("Actual True predicted True: 4240")


def render_classification_report() -> None:
    render_header(
        "Classification Report",
        "Precision, recall, F1-score, and support by class.",
    )

    st.dataframe(format_classification_report(), hide_index=True, width="stretch")

    with st.expander("Report notes"):
        st.write("Label convention used by the app: 0 = Fake News, 1 = True News.")
        st.write("Accuracy: 0.9994 on 8935 held-out examples.")


def render_bootstrap_intervals() -> None:
    render_header(
        "Bootstrap Confidence Intervals",
        "Estimated uncertainty for the final model metrics.",
    )

    cols = st.columns(2)
    cols[0].metric("Accuracy Mean", "0.9994", "95% CI 0.9989 to 0.9999")
    cols[1].metric("F1 Score Mean", "0.9994", "95% CI 0.9988 to 0.9999")

    st.subheader("Confidence Interval Table")
    st.dataframe(format_bootstrap_intervals(), hide_index=True, width="stretch")

    chart_data = BOOTSTRAP_INTERVALS.set_index("Metric")[["Mean", "95% CI Lower", "95% CI Upper"]]
    st.bar_chart(chart_data)


def render_submission_info(model: Any | None, model_error: str | None) -> None:
    render_header(
        "Submission Information",
        "How to run the app and prepare the final trained model artifact.",
    )

    st.subheader("Run Locally")
    st.code("streamlit run app.py", language="bash")

    st.subheader("Share on the Same Wi-Fi")
    st.write(
        "For a short demo on the same network, run Streamlit on all network interfaces, then share "
        "your computer's local IPv4 address with the port."
    )
    st.code("streamlit run app.py --server.address 0.0.0.0 --server.port 8501", language="bash")
    st.code("http://YOUR-IP-ADDRESS:8501", language="text")

    st.subheader("Deploy for Public Access")
    st.write(
        "For a link that works on other people's computers anywhere, deploy the project to Streamlit "
        "Community Cloud from GitHub and use app.py as the entrypoint."
    )
    st.code("https://share.streamlit.io", language="text")
    with st.expander("Public deployment checklist", expanded=True):
        st.write("Push app.py, requirements.txt, README.md, and .streamlit/config.toml to GitHub.")
        st.write("Add final_model.pkl to the repository if you want online predictions to work.")
        st.write("Create a new Streamlit Community Cloud app from the repository.")
        st.write("Set the main file path to app.py.")
        st.write("Share the generated streamlit.app URL.")

    st.subheader("Required Model File")
    show_model_status(model, model_error)

    with st.expander("Export final_model.pkl from the notebook", expanded=True):
        st.write("After training and selecting the best model, run this in the notebook:")
        st.code(MODEL_EXPORT_SNIPPET, language="python")

    with st.expander("Included app files", expanded=True):
        st.write("app.py")
        st.write("requirements.txt")
        st.write("README.md")
        st.write(".streamlit/config.toml")


def render_sidebar(model: Any | None) -> str:
    st.sidebar.title("News Detector")
    page = st.sidebar.radio("Pages", PAGES)
    st.sidebar.divider()
    st.sidebar.caption("Model file")
    if model is not None:
        st.sidebar.success("final_model.pkl loaded")
    else:
        st.sidebar.warning("final_model.pkl missing or unavailable")
    st.sidebar.caption("Label convention: 0 = Fake News, 1 = True News")
    return page


def main() -> None:
    apply_theme()
    model, model_error = load_trained_model()
    page = render_sidebar(model)

    if page == "Home":
        render_home(model, model_error)
    elif page == "Interactive Prediction":
        render_prediction(model, model_error)
    elif page == "Model Performance":
        render_performance()
    elif page == "Confusion Matrix":
        render_confusion_matrix()
    elif page == "Classification Report":
        render_classification_report()
    elif page == "Bootstrap Confidence Intervals":
        render_bootstrap_intervals()
    elif page == "Submission Information":
        render_submission_info(model, model_error)
>>>>>>> 510ae17251100941bd544b6b6caf5502af649133


if __name__ == "__main__":
    main()
