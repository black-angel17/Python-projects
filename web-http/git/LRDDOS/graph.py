import os
import matplotlib.pyplot as plt

# Create the directory if it doesn't exist
save_dir = './graph'
os.makedirs(save_dir, exist_ok=True)

# Metrics for KNN
knn_metrics = [0.9996, 0.9995, 1.0000, 0.9998, 0.9995, 0.0000, 0.1931, 41.1288]

# Metrics for Random Forest
rf_metrics = [0.9996, 0.9995, 1.0000, 0.9998, 0.9995, 0.0000, 89.4745, 0.5789]

# Metrics for Logistic Regression
lr_metrics = [0.9682, 0.9847, 0.9758, 0.9802, 0.9847, 0.0979, 14.7288, 0.0595]

# Labels for metrics
metrics_labels = ['Accuracy', 'Recall', 'Precision', 'F1 Score', 'TPR', 'FPR', 'Training Time', 'Prediction Time']

# Common colors for algorithms
colors = ['lightblue', 'lightgreen', 'lightcoral']

# Create separate bar graphs for each metric and save them
for i in range(len(metrics_labels)):
    plt.figure(figsize=(8, 6))
    plt.bar(['KNN', 'Random Forest', 'Logistic Regression'], [knn_metrics[i], rf_metrics[i], lr_metrics[i]], color=colors)
    plt.title(metrics_labels[i])
    plt.ylabel(metrics_labels[i])
    plt.savefig(os.path.join(save_dir, f'{metrics_labels[i]}.png'))  # Save each graph in the specified directory
    plt.close()
