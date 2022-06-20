from sklearn.neighbors import KNeighborsClassifier
import config
from sklearn.model_selection import GridSearchCV

def Model():
    if (config.data["GridSearchCV"]):
        clf = GridSearchCV(
            KNeighborsClassifier(),
            config.KNN_,
            refit=True,
            cv=5,
            scoring=config.evaluate["scoring"],
            n_jobs=-1
        )
    else:
        clf = KNeighborsClassifier(
            n_neighbors=config.KNN["n_neighbors"]
        )
    return clf