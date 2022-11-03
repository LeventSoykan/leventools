from sklearn.metrics import accuracy_score, f1_score
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
import pandas


def classification_score(y_test, y_pred):
    f1 = f1_score(y_test, y_pred)
    accuracy = accuracy_score(y_test, y_pred)
    print(f'Accuracy Score = {accuracy}\nF1 Score:{f1}\n')
    print(classification_report(y_test, y_pred))
    print(pandas.DataFrame(confusion_matrix(y_test, y_pred)[::-1, ::-1],
                           columns=['Pred_True', 'Pred_False'],
                           index=['Act_True', 'Act_False']))
    