import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
import seaborn as sns
import matplotlib.pyplot as plt
import Main as m
import datacleaning.Cleaned_DataFrame_Description as dc

model = LogisticRegression() 
model.fit(dc.X_train, dc.y_train)
   
y_pred = model.predict(dc.X_test)
accuracy = accuracy_score(dc.y_test, y_pred)
conf_matrix = confusion_matrix(dc.y_test, y_pred)
class_report = classification_report(dc.y_test, y_pred)

    

def display_results(accuracy, conf_matrix, class_report):
    print(f'Accuracy: {accuracy}')
    print('Confusion Matrix:\n', conf_matrix)
    print('Classification Report:\n', class_report)
    sns.heatmap(conf_matrix, annot=True, fmt='d', cmap='Blues')
    plt.xlabel('Predicted')
    plt.ylabel('Actual')
    plt.title('Confusion Matrix')
    plt.show()





