# Initialize lists to store metric values
tpr_values = []
fpr_values = []
precision_values = []
recall_values = []
f1_score_values = []

for k in k_values:
    knn_classifier = KNeighborsClassifier(n_neighbors=k)
    knn_classifier.fit(X_train, y_train)
    y_pred = knn_classifier.predict(X_test)

    # Compute confusion matrix
    conf_matrix = confusion_matrix(y_test, y_pred)
    TN, FP, FN, TP = conf_matrix.ravel()

    # Calculate True Positive Rate (TPR)
    tpr = TP / (TP + FN)
    tpr_values.append(tpr)

    # Calculate False Positive Rate (FPR)
    fpr = FP / (FP + TN)
    fpr_values.append(fpr)

    # Calculate Precision
    precision = TP / (TP + FP)
    precision_values.append(precision)

    # Calculate Recall
    recall = TP / (TP + FN)
    recall_values.append(recall)

    # Calculate F1 Score (F-measure)
    f1_score = 2 * (precision * recall) / (precision + recall)
    f1_score_values.append(f1_score)

    # Print the metrics for each k
    print(f'k = {k}: TPR = {tpr:.4f}, FPR = {fpr:.4f}, Precision = {precision:.4f}, Recall = {recall:.4f}, F1 Score = {f1_score:.4f}')

# Calculate average of each metric
avg_tpr = sum(tpr_values) / len(tpr_values)
avg_fpr = sum(fpr_values) / len(fpr_values)
avg_precision = sum(precision_values) / len(precision_values)
avg_recall = sum(recall_values) / len(recall_values)
avg_f1_score = sum(f1_score_values) / len(f1_score_values)

# Print the averages
print(f'Average TPR: {avg_tpr:.4f}')
print(f'Average FPR: {avg_fpr:.4f}')
print(f'Average Precision: {avg_precision:.4f}')
print(f'Average Recall: {avg_recall:.4f}')
print(f'Average F1 Score: {avg_f1_score:.4f}')
