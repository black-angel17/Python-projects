import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix, accuracy_score
from sklearn.preprocessing import LabelEncoder
from sklearn.impute import SimpleImputer
import numpy as np
import time

# Load data
data_normal = pd.read_csv("n.csv")
data_attack = pd.read_csv("a.csv")

# Combine normal and attack data
data = pd.concat([data_normal, data_attack], ignore_index=True)

# Handle label encoding for binary variables
binary_cols = ["Label"]
label_encoder = LabelEncoder()
for col in binary_cols:
    data[col] = label_encoder.fit_transform(data[col])

# Handle one-hot encoding for nominal variables
nominal_cols = ["Layer","ack_no", "Time_interval", "src_ip", "tcp_length", "stream", "Time(seconds)", "socket_count", "sql"]
data = pd.get_dummies(data, columns=nominal_cols)

# Remove "Unnamed: 2" column if present
if "Unnamed: 2" in data.columns:
    data = data.drop(columns=["Unnamed: 2"])

# Separate features and labels
X = data.drop(columns=["Label"])
y = data["Label"]

# Impute missing values
imputer = SimpleImputer(strategy='constant', fill_value=0)
X_imputed = imputer.fit_transform(X)

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X_imputed, y, test_size=0.2, random_state=42)

# Initialize KNN classifier for k=1
k = 1
accuracy_using_metrics = []
training_times = []
prediction_times = []  # Corrected typo

start_time = time.time()

knn_classifier = KNeighborsClassifier(n_neighbors=k)
knn_classifier.fit(X_train, y_train)

end_time = time.time()
training_time = end_time - start_time
training_times.append(training_time)

start_time = time.time()

y_pred = knn_classifier.predict(X_test)

end_time = time.time()
prediction_time = end_time - start_time
prediction_times.append(prediction_time)  # Added this line to store prediction time

# Calculate accuracy using accuracy_score
accuracy = accuracy_score(y_test, y_pred)
accuracy_using_metrics.append(accuracy)

# Print the accuracy and training time
print(f'k = {k}: Accuracy = {accuracy:.4f}, Training Time = {training_time:.4f} seconds')

# Compute confusion matrix
conf_matrix = confusion_matrix(y_test, y_pred)
TN, FP, FN, TP = conf_matrix.ravel()

# Calculate True Positive Rate (TPR)
tpr = TP / (TP + FN)

# Calculate False Positive Rate (FPR)
fpr = FP / (FP + TN)

# Calculate Precision
precision = TP / (TP + FP)

# Calculate Recall
recall = TP / (TP + FN)

# Calculate F1 Score (F-measure)
f1_score_value = 2 * (precision * recall) / (precision + recall)

# Print the additional metrics for k=1
print(f'Evaluation for {k}:')
print(f'TPR = {tpr:.4f}')
print(f'FPR = {fpr:.4f}')
print(f'Precision = {precision:.4f}')
print(f'Recall = {recall:.4f}')
print(f'F1 Score = {f1_score_value:.4f}')

# Print exact prediction time
print(f'Prediction Time: {prediction_time:.4f} seconds')
