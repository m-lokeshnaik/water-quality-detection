# -*- coding: utf-8 -*-
"""waterpotability-with_different_anomly_model.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/10AZVsmObhXEnrTjOyG-MNJqIHGI_wavM
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df=pd.read_csv(r"/content/water_potability.csv")

# Get summary statistics
df.describe()

# Check for missing values
missing_values = df.isnull().sum()
print("Missing values in the dataset:")
print(missing_values)

plt.figure(figsize=(10, 6))
sns.boxplot(data=df.drop(columns='Potability'))
plt.title('Boxplot of Water Quality Parameters')
plt.show()

# Handle missing values by imputing with mean or median
df.fillna(df.mean(), inplace=True)

# Check for missing values
missing_values = df.isnull().sum()
print("Missing values in the dataset:")
print(missing_values)

# Exploratory Data Analysis (EDA)
# Summary statistics
summary_stats = df.describe()
print("\nSummary Statistics:")
print(summary_stats)

# Data Visualization
df.hist(figsize=(12, 10))
plt.suptitle('Histograms of Water Quality Parameters', x=0.5, y=1.02)
plt.show()

# Correlation matrix
correlation_matrix = df.corr()
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f")
plt.title('Correlation Matrix of Water Quality Parameters')
plt.show()

X = df.drop('Potability',axis=1) # other variables - to send to model
y = df.iloc[:,9:].values  # potability
print(X.shape, y.shape)

# Splitting the dataset into the training set and data set
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)

def calculate_accuracy(y_test, y_pred):
  metrics = {}

  # False Negatives (True label is False, predicted as True)
  if list(y_pred).count(False) > list(y_test).count(False):
    metrics["Accuracy True False (False Negative)"] = (list(y_test).count(False) / list(y_pred).count(False)) * 100
    FP = list(y_test).count(False) / list(y_pred).count(False)
  else:
    metrics["Accuracy True False (False Negative)"] = (list(y_pred).count(False) / list(y_test).count(False)) * 100
    FP = list(y_pred).count(False) / list(y_test).count(False)

  # True Positives (True label is True, predicted as True)
  if list(y_pred).count(True) > list(y_test).count(True):
    metrics["Accuracy True True (True Positive)"] = (list(y_test).count(True) / list(y_pred).count(True)) * 100
    TP = list(y_test).count(True) / list(y_pred).count(True)
  else:
    metrics["Accuracy True True (True Positive)"] = (list(y_pred).count(True) / list(y_test).count(True)) * 100
    TP = list(y_pred).count(True) / list(y_test).count(True)

  # Overall Accuracy
  topVeriSayisi = list(y_test).count(True) + list(y_test).count(False)
  positive = list(y_pred).count(True) * TP + list(y_pred).count(False) * FP
  metrics["Accuracy"] = positive / topVeriSayisi * 100

  return metrics

# from sklearn.preprocessing import StandardScaler
# sc_X = StandardScaler()
# X_train = sc_X.fit_transform(X_train)
# X_test = sc_X.transform(X_test)

from sklearn.ensemble import IsolationForest
from sklearn.metrics import confusion_matrix, accuracy_score
# Train Isolation Forest model
model_1 = IsolationForest(contamination=0.1, random_state=42)
model_1.fit(X_train)

# Predicting the result with Isolation Forest Method
y_pred_1 = model_1.predict(X_test)
anomaly_score  = model_1.decision_function(X_test)

accuracy_metrics_1 = calculate_accuracy(y_test, y_pred_1)
print(accuracy_metrics_1)

from sklearn.ensemble import RandomForestClassifier
model_2 = RandomForestClassifier(n_estimators = 200, criterion = 'entropy' ,   random_state = 0)
model_2.fit(X_train, y_train)

y_pred_2 = model_2.predict(X_test)

accuracy_metrics_2 = calculate_accuracy(y_test, y_pred_2)
print(accuracy_metrics_2)

from sklearn.neighbors import LocalOutlierFactor
model_3 = LocalOutlierFactor(n_neighbors = 20, novelty = True, contamination = 'auto')
model_3.fit(X_train)

y_pred_3 = model_3.predict(X_test)
anomaly_score  = model_3.decision_function(X_test)

accuracy_metrics_3 = calculate_accuracy(y_test, y_pred_3)
print(accuracy_metrics_3)

from sklearn.linear_model import LogisticRegression
model_4 = LogisticRegression(random_state=0)
model_4.fit(X_train,y_train)

y_pred_4 = model_4.predict(X_test)
anomaly_score  = model_4.decision_function(X_test)

accuracy_metrics_4 = calculate_accuracy(y_test, y_pred_4)
print("isolaton forest",accuracy_metrics_1)
print("random forest classifer",accuracy_metrics_2)
print("Loacl Outlier factor",accuracy_metrics_3)
print("LogisticRegressioni",accuracy_metrics_4)