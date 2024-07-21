import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, confusion_matrix, precision_score, recall_score, f1_score

# Load data from n.csv and a.csv
data_normal = pd.read_csv("n.csv")
data_attack = pd.read_csv("a.csv")

# Combine normal and attack data
combined_data = pd.concat([data_normal, data_attack], ignore_index=True)

# Replace missing values with 0
combined_data.fillna(0, inplace=True)

# Separate features and labels
X = combined_data.drop(columns=["Label"])  # Exclude the 'Label' column
y = combined_data["Label"]

# One-hot encode categorical features
X_encoded = pd.get_dummies(X)

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X_encoded, y, test_size=0.2, random_state=42)

# Initialize SVM classifier
svm_classifier = SVC(kernel='linear')  # You can choose different kernels based on your data and requirements

# Fit SVM classifier to the training data
svm_classifier.fit(X_train, y_train)

# Predict labels for the test data
y_pred = svm_classifier.predict(X_test)

# Compute confusion matrix
conf_matrix = confusion_matrix(y_test, y_pred)
TN, FP, FN, TP = conf_matrix.ravel()

# Calculate overall accuracy
overall_accuracy = accuracy_score(y_test, y_pred)

# Calculate True Positive Rate (TPR)
tpr = TP / (TP + FN)

# Calculate False Positive Rate (FPR)
fpr = FP / (FP + TN)

# Calculate Precision
precision = precision_score(y_test, y_pred, pos_label='A')  # Set pos_label based on your dataset

# Calculate Recall
recall = recall_score(y_test, y_pred, pos_label='A')  # Set pos_label based on your dataset

# Calculate F1 Score (F-measure)
f1_score_value = f1_score(y_test, y_pred, pos_label='A')  # Set pos_label based on your dataset

# Print the metrics
print(f'Overall Accuracy: {overall_accuracy * 100:.2f}%')
print(f'TPR = {tpr:.4f}, FPR = {fpr:.4f}, Precision = {precision:.4f}, Recall = {recall:.4f}, F1 Score = {f1_score_value:.4f}')
