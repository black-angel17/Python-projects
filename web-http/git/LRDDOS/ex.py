import pandas as pd
import os

# Create the directory if it doesn't exist
excel_dir = './excel'
os.makedirs(excel_dir, exist_ok=True)

# Metrics for KNN
knn_metrics = [0.9996, 0.9995, 1.0000, 0.9998, 0.9995, 0.0000, 0.1931, 41.1288]

# Metrics for Random Forest
rf_metrics = [0.9996, 0.9995, 1.0000, 0.9998, 0.9995, 0.0000, 89.4745, 0.5789]

# Metrics for Logistic Regression
lr_metrics = [0.9682, 0.9847, 0.9758, 0.9802, 0.9847, 0.0979, 14.7288, 0.0595]

# Labels for metrics
metrics_labels = ['Accuracy', 'Recall', 'Precision', 'F1 Score', 'TPR', 'FPR', 'Training Time', 'Prediction Time']

# Create a separate Excel file for each metric
for i, metric_label in enumerate(metrics_labels):
    df = pd.DataFrame({
        'Algorithm': ['KNN', 'Random Forest', 'Logistic Regression'],
        metric_label: [knn_metrics[i], rf_metrics[i], lr_metrics[i]]
    })
    excel_filename = os.path.join(excel_dir, f'{metric_label.replace(" ", "_").lower()}.xlsx')  # Use metric label as filename
    df.to_excel(excel_filename, index=False)
    print(f"Excel file saved as '{excel_filename}'")
