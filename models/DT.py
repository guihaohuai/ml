from sklearn import tree
import config
from sklearn.model_selection import GridSearchCV

def Model():
    if(config.data["GridSearchCV"]):
        clf=GridSearchCV(
            tree.DecisionTreeClassifier(),
            config.DT_,
            refit = True,
            cv = 5,
            scoring=config.evaluate["scoring"],
            n_jobs=-1
        )
    else:
        #https://blog.csdn.net/qq_38923076/article/details/82931340
        clf = tree.DecisionTreeClassifier(
            criterion=config.DT["criterion"],
            max_depth=config.DT["max_depth"],
            min_samples_split=config.DT["min_samples_split"],
            min_samples_leaf=config.DT["min_samples_leaf"],
            min_impurity_decrease=config.DT["min_impurity_decrease"]
        )

    return clf




