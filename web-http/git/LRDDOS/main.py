# main.py
import subprocess

def main():
    # Run KNN
    print("Running KNN...")
    knn_output = subprocess.check_output(["python", "knn.py"]).decode("utf-8")

    # Run Random Forest
    print("Running Random Forest...")
    rf_output = subprocess.check_output(["python", "random forest.py"]).decode("utf-8")

    # Run Logistic Regression
    print("Running Logistic Regression...")
    lr_output = subprocess.check_output(["python", "logistic regression.py"]).decode("utf-8")

    # Save outputs to a text file
    with open("report.txt", "w") as file:
        file.write("KNN Output:\n" + knn_output + "\n\n")
        file.write("Random Forest Output:\n" + rf_output + "\n\n")
        file.write("Logistic Regression Output:\n" + lr_output)

    print("Report saved as report.txt")

if __name__ == "__main__":
    main()
