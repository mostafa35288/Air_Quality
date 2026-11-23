# Air Quality Prediction

## Project Description
End-to-end machine learning project that predicts the air quality class from environmental features. It covers data analysis, preprocessing, model training with and without scikit-learn pipelines, and a Streamlit app for real-time predictions.

## Project Structure
- `Air_Quality.ipynb`: EDA, preprocessing, and the full model comparison without pipelines.
- `Air_Quality-with pipeline.ipynb`: the same workflow rebuilt with scikit-learn pipelines.
- `stAirPredict.py`: Streamlit app for real-time air quality predictions.

## Dataset
Kaggle: **Air Quality and Pollution Assessment** (`mujtabamatin/air-quality-and-pollution-assessment`), file `updated_pollution_dataset.csv`. The target is `Air Quality` with 4 classes (Good, Moderate, Poor, Hazardous). Models are evaluated on a held-out test split of 1,000 rows.

## Features
- Temperature
- Humidity
- PM2.5
- PM10
- NO2
- SO2
- CO
- Proximity to Industrial Areas
- Population Density

## Models

**Linear Model**
- Logistic Regression

**Distance-Based Models**
- K-Nearest Neighbors (KNN)
- Support Vector Machine (SVC)

**Tree-Based Models**
- Decision Tree

**Probabilistic Models**
- Gaussian Naive Bayes

**Bagging Ensembles**
- Random Forest
- Extra Trees

**Boosting Ensembles**
- AdaBoost
- Gradient Boosting
- HistGradientBoosting
- XGBoost
- LightGBM
- CatBoost

**Advanced Ensembles**
- Voting Classifier (soft voting: Logistic Regression + Random Forest + Naive Bayes + XGBoost)
- Stacking Classifier (Logistic Regression + Random Forest + Naive Bayes + LightGBM, with XGBoost as the meta-model, using probability outputs)

## Evaluation
Train/test split with accuracy, precision, recall, F1-score, confusion matrix, and multiclass ROC-AUC.

## Results
The strongest models (boosting and stacking ensembles) reach about **0.996 ROC-AUC** and around **96% test accuracy** on the held-out test split.

## Run the Streamlit app
```bash
streamlit run stAirPredict.py
```
