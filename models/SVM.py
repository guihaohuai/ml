from sklearn import svm
import config
from sklearn.model_selection import GridSearchCV

def Model():
    if(config.data["GridSearchCV"]):
        clf=GridSearchCV(
            svm.SVC(),
            config.SVM_,
            refit = True,
            cv = 5,
            scoring=config.evaluate["scoring"],
            n_jobs=-1
        )
    else:
        clf = svm.SVC(
            kernel=config.SVM["kernel"],
            C=config.SVM["C"]
        )
    return clf
