from src.load_data import load_dataset
from src.clean_data import clean_data
from src.feature_engineering import feature_engineering
from src.model import train_model
from src.evaluate import evaluate_model
from src.predict import predict

from sklearn.model_selection import train_test_split

df = load_dataset("data/KDDTrain+.txt")
df = clean_data(df)
df = feature_engineering(df)

X = df.iloc[:, :-1]   
y = df.iloc[:, -1]    

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

model = train_model(X_train, y_train)

y_pred = predict(model, X_test)

accuracy, precision, recall, f1 = evaluate_model(y_test, y_pred)

print("Accuracy:", accuracy)
print("Precision:", precision)
print("Recall:", recall)
print("F1 Score:", f1)

from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay
import matplotlib.pyplot as plt

cm = confusion_matrix(y_test, y_pred)

disp = ConfusionMatrixDisplay(confusion_matrix=cm)
disp.plot()

plt.title("Confusion Matrix")
plt.show()