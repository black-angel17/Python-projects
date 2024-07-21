import pandas as pd
import time
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix, accuracy_score, recall_score, precision_score, f1_score
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.impute import SimpleImputer

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
nominal_cols = ["Layer","ack_no", "Time_interval", "src_ip", "tcp_length", "stream", "Time(seconds)", "socket_count",
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

# Scale the data
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X_imputed)

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

# Initialize Logistic Regression classifier with increased max_iter
logreg_classifier = LogisticRegression(max_iter=1000, random_state=42)

# Train the classifier and measure training time
start_time = time.time()
logreg_classifier.fit(X_train, y_train)
training_time = time.time() - start_time

# Predict using the trained classifier and measure prediction time
start_time = time.time()
y_pred = logreg_classifier.predict(X_test)
prediction_time = time.time() - start_time

# Compute confusion matrix
conf_matrix = confusion_matrix(y_test, y_pred)
print("Confusion Matrix:")
print(conf_matrix)

# Calculate evaluation metrics
accuracy = accuracy_score(y_test, y_pred)
recall = recall_score(y_test, y_pred)
precision = precision_score(y_test, y_pred)
f1 = f1_score(y_test, y_pred)

# Calculate True Positive Rate (TPR), False Positive Rate (FPR), and additional metrics
tn, fp, fn, tp = conf_matrix.ravel()
tpr = tp / (tp + fn)
fpr = fp / (fp + tn)

# Print evaluation metrics and timing information
print(f'Accuracy: {accuracy:.4f}')
print(f'Recall: {recall:.4f}')
print(f'Precision: {precision:.4f}')
print(f'F1 Score: {f1:.4f}')
print(f'TPR: {tpr:.4f}')
print(f'FPR: {fpr:.4f}')
print(f'Training Time: {training_time:.4f} seconds')
print(f'Prediction Time: {prediction_time:.4f} seconds')
