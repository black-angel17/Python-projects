import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix
from sklearn.preprocessing import LabelEncoder
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
nominal_cols = ["Layer", "Time_interval", "src_ip", "tcp_length", "stream", "Time(seconds)", "socket_count",
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

# Initialize KNN classifier
k_values = range(1, 11)
accuracy_using_metrics = []

for k in k_values:
    knn_classifier = KNeighborsClassifier(n_neighbors=k)
    knn_classifier.fit(X_train, y_train)
    y_pred = knn_classifier.predict(X_test)

    # Compute confusion matrix
    conf_matrix = confusion_matrix(y_test, y_pred)
    TN, FP, FN, TP = conf_matrix.ravel()

    # Calculate accuracy using TP, TN, FP, FN
    accuracy = (TP + TN) / (TP + TN + FP + FN)
    accuracy_using_metrics.append(accuracy)

    # Print the accuracy and additional metrics for each k
    print(f'k = {k}: Accuracy = {accuracy:.4f}, TP = {TP}, TN = {TN}, FP = {FP}, FN = {FN}')

    # Calculate True Positive Rate (TPR)
    tpr = TP / (TP + FN)

    # Calculate False Positive Rate (FPR)
    fpr = FP / (FP + TN)

    # Calculate Precision
    precision = TP / (TP + FP)

    # Calculate Recall
    recall = TP / (TP + FN)

    # Calculate F1 Score (F-measure)
    f1_score = 2 * (precision * recall) / (precision + recall)

    # Print the additional metrics for each k
    print(
        f'evaluation for {k} : TPR = {tpr:.4f}, FPR = {fpr:.4f}, Precision = {precision:.4f}, Recall = {recall:.4f}, F1 Score = {f1_score:.4f}')

# Calculate overall accuracy
overall_accuracy = sum(accuracy_using_metrics) / len(accuracy_using_metrics)

# Print the overall accuracy
print(f'Overall Accuracy: {overall_accuracy * 100:.2f}%')

# Plot the accuracy
plt.plot(k_values, accuracy_using_metrics, marker='o', label='Accuracy using metrics')
plt.title('Accuracy vs. Number of Neighbors')
plt.xlabel('Number of Neighbors (k)')
plt.ylabel('Accuracy')
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()
