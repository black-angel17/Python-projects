import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix

# Step 1: Load the data from CSV files
# Assuming your CSV files are named 'normal_data.csv', 'attack_data.csv', and 'shuffled_data.csv'
normal_data = pd.read_csv('n.csv')
attack_data = pd.read_csv('a.csv')
shuffled_data = pd.read_csv('t.csv')

# Step 2: Separate features (X) and labels (y) for normal and attack datasets
X_normal = normal_data.drop(columns=['label'])  # assuming the label column is named 'label'
y_normal = normal_data['label']

X_attack = attack_data.drop(columns=['label'])  # assuming the label column is named 'label'
y_attack = attack_data['label']

# Step 3: Splitting the labeled data into training and testing sets
X_normal_train, X_normal_test, y_normal_train, y_normal_test = train_test_split(X_normal, y_normal, test_size=0.2, random_state=42)
X_attack_train, X_attack_test, y_attack_train, y_attack_test = train_test_split(X_attack, y_attack, test_size=0.2, random_state=42)

# Step 4: Training k-NN model
# Combine the labeled datasets for training
X_train = pd.concat([X_normal_train, X_attack_train], axis=0)
y_train = pd.concat([y_normal_train, y_attack_train], axis=0)

# Initialize k-NN classifier
knn_classifier = KNeighborsClassifier(n_neighbors=5)  # you can adjust the value of k

# Train the classifier
knn_classifier.fit(X_train, y_train)

# Step 5: Evaluate the model
# Combine the labeled test sets for evaluation
X_test = pd.concat([X_normal_test, X_attack_test], axis=0)
y_test = pd.concat([y_normal_test, y_attack_test], axis=0)

# Predict on the combined test set
y_pred = knn_classifier.predict(X_test)

# Calculate accuracy
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)

# Calculate precision, recall, and F1-score
precision = precision_score(y_test, y_pred)
recall = recall_score(y_test, y_pred)
f1 = f1_score(y_test, y_pred)

print("Precision:", precision)
print("Recall:", recall)
print("F1-score:", f1)

# Calculate confusion matrix
conf_matrix = confusion_matrix(y_test, y_pred)
print("Confusion Matrix:")
print(conf_matrix)

# Step 6: Predicting on the shuffled dataset
# Assuming shuffled_data contains only features and no labels
predicted_labels = knn_classifier.predict(shuffled_data)
print("Predicted labels for the shuffled dataset:", predicted_labels)
