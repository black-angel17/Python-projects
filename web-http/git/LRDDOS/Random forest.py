import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import confusion_matrix, accuracy_score, recall_score, precision_score, f1_score
from sklearn.preprocessing import LabelEncoder
from sklearn.impute import SimpleImputer
import time

# Load data
data_normal = pd.read_csv("n.csv")
data_attack = pd.read_csv("a.csv")

# Combine normal and attack data
data = pd.concat([data_normal, data_attack], ignore_index=True)

# Handle label encoding for binary variables
binary_cols = ["Label"]  # Assuming "Label" is a binary variable
label_encoder = LabelEncoder()
for col in binary_cols:
    data[col] = label_encoder.fit_transform(data[col])

# Handle one-hot encoding for nominal variables
nominal_cols = ["Layer", "Time_interval","ack_no", "src_ip", "tcp_length", "stream", "Time(seconds)", "socket_count",
                "sql"]  # List all nominal columns here
data = pd.get_dummies(data, columns=nominal_cols)

# Remove "Unnamed: 2" column if present
if "Unnamed: 2" in data.columns:
    data = data.drop(columns=["Unnamed: 2"])

# Separate features and labels
X = data.drop(columns=["Label"])
y = data["Label"]

# Impute missing values
imputer = SimpleImputer(strategy='constant', fill_value=0)  # Use constant strategy with fill value 0
X_imputed = imputer.fit_transform(X)

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X_imputed, y, test_size=0.2, random_state=42)

# Initialize Random Forest classifier
rf_classifier = RandomForestClassifier(n_estimators=100, random_state=42)

# Measure training time
start_time = time.time()
rf_classifier.fit(X_train, y_train)
end_time = time.time()
training_time = end_time - start_time

# Measure prediction time
start_time = time.time()
y_pred = rf_classifier.predict(X_test)
end_time = time.time()
prediction_time = end_time - start_time

# Compute confusion matrix
conf_matrix = confusion_matrix(y_test, y_pred)
print("Confusion Matrix:")
print(conf_matrix)

# Calculate evaluation metrics
accuracy = accuracy_score(y_test, y_pred)
recall = recall_score(y_test, y_pred)
precision = precision_score(y_test, y_pred)
f1 = f1_score(y_test, y_pred)

# Print evaluation metrics
print(f'Accuracy: {accuracy:.4f}')
print(f'Recall: {recall:.4f}')
print(f'Precision: {precision:.4f}')
print(f'F1 Score: {f1:.4f}')

# Calculate True Positive Rate (TPR), False Positive Rate (FPR), and additional metrics
tn, fp, fn, tp = conf_matrix.ravel()
tpr = tp / (tp + fn)
fpr = fp / (fp + tn)

# Print TPR, FPR, Training Time, and Prediction Time
print(f'TPR: {tpr:.4f}')
print(f'FPR: {fpr:.4f}')
print(f'Training Time: {training_time:.4f} seconds')
print(f'Prediction Time: {prediction_time:.4f} seconds')
