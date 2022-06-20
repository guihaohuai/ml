from sklearn import linear_model
import config
from sklearn.model_selection import GridSearchCV

def Model():
    if (config.data["GridSearchCV"]):
        clf = GridSearchCV(
            linear_model.LogisticRegression(),
            config.LR_,
            refit=True,
            cv=5,
            scoring=config.evaluate["scoring"],
            n_jobs=-1
        )
    else:
        #https://blog.csdn.net/qq_38923076/article/details/82931340
        clf = linear_model.LogisticRegression(
            penalty=config.LR["penalty"],
            dual=config.LR["dual"],
            tol=config.LR["tol"],
            C=config.LR["C"],
            fit_intercept=config.LR["fit_intercept"],
            intercept_scaling=config.LR["intercept_scaling"],
            class_weight=config.LR["class_weight"],
            random_state=config.LR["random_state"],
            solver=config.LR["solver"],
            max_iter=config.LR["max_iter"],
            multi_class=config.LR["multi_class"],
            verbose=config.LR["verbose"],
            warm_start=config.LR["warm_start"],
            n_jobs=config.LR["n_jobs"]
        )
    return clf
