from sklearn.ensemble import RandomForestClassifier
import config
from sklearn.model_selection import GridSearchCV

def Model():
    if (config.data["GridSearchCV"]):
        clf = GridSearchCV(
            RandomForestClassifier(),
            config.RF_,
            refit=True,
            cv=5,
            scoring=config.evaluate["scoring"],
            n_jobs=-1
        )
    else:
        #https://blog.csdn.net/qq_38923076/article/details/82931340
        clf=RandomForestClassifier(
            n_estimators = config.RF["n_estimators"],
            criterion=config.RF["criterion"],
            max_depth = config.RF["max_depth"],
            min_samples_split = config.RF["min_samples_split"],
            min_samples_leaf = config.RF["min_samples_leaf"],
            min_weight_fraction_leaf = config.RF["min_weight_fraction_leaf"],
            max_features =config.RF["max_features"],
            max_leaf_nodes = config.RF["max_leaf_nodes"],
            min_impurity_decrease = config.RF["min_impurity_decrease"]
        )
    return clf