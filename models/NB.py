from sklearn.naive_bayes import GaussianNB
from sklearn.naive_bayes import MultinomialNB
from sklearn.naive_bayes import BernoulliNB
import config
from sklearn.model_selection import GridSearchCV

def Model():
    if(config.data["GridSearchCV"]):
        if(config.NB["method"]=="Gaussian"):
            #为了保持一致，高斯贝叶斯也用了集成的方法写
            clf = GridSearchCV(
                GaussianNB(),
                {},
                refit=True,
                cv=5,
                scoring=config.evaluate["scoring"],
                n_jobs=-1
            )
        if (config.NB["method"] =="Multinomial"):
            #https://scikit-learn.org.cn/view/690.html
            clf = GridSearchCV(
                MultinomialNB(),
                config.NB_M_,
                refit=True,
                cv=5,
                scoring=config.evaluate["scoring"],
                n_jobs=-1
            )
        if (config.NB["method"] =="Bernoulli"):
            clf = GridSearchCV(
                BernoulliNB(),
                config.NB_B_,
                refit=True,
                cv=5,
                scoring=config.evaluate["scoring"],
                n_jobs=-1
            )
    else:
        if(config.NB["method"]=="Gaussian"):
            clf = GaussianNB()#没有参数
        if (config.NB["method"] =="Multinomial"):
            #https://scikit-learn.org.cn/view/690.html
            clf = MultinomialNB(
                alpha=config.NB["M_alpha"],
                fit_prior=config.NB["M_fit_prior"]
            )
        if (config.NB["method"] =="Bernoulli"):
            clf = BernoulliNB(
                alpha=config.NB["B_alpha"],
                fit_prior=config.NB["B_fit_prior"]
            )
    return clf