import numpy as np
import pandas as pd
import torch
import sklearn
from sklearn.model_selection import cross_val_score
import config
import joblib
import m2cgen as m2c

#选择模型
if(config.data["ml_method"]=="NB"):
    from models.NB import Model
if(config.data["ml_method"]=="SVM"):
    from models.SVM import Model
if(config.data["ml_method"]=="DT"):
    from models.DT import Model
if(config.data["ml_method"]=="KNN"):
    from models.KNN import Model
if(config.data["ml_method"]=="LR"):
    from models.LR import Model
if(config.data["ml_method"]=="RF"):
    from models.RF import Model
if(config.data["ml_method"]=="XB"):
    from models.XB import Model

#读取数据
df=pd.read_csv( config.data["fpath"] )
features=df.columns.tolist()
features.remove( config.data["target_name"] )
y=df[ config.data["target_name"] ]
X=df[features].values
"""
#及时查看，避免数据错误
print(df.head(5))
print(features)
print('Y:\n',y[0])
print("X:\n",X[2])
input()
"""
#如果要[[],[]]这样的y 就df[["Survived"]]
#如果要[1,2,3]这样的y 就df["Survived"]

#特征选择
pass

##模型训练与性能评价
clf = Model()

print("ml_method:\t\t", config.data["ml_method"])
print("GridSearchCV:\t", config.data["GridSearchCV"],"\n")

if(config.data["GridSearchCV"]):
    clf.fit(X, y)
    #其实可以直接clf.best_score_获得模型的平均分，但是不五个都显示就怕方差太大
    scores = cross_val_score(clf.best_estimator_, X, y, cv=5, scoring=config.evaluate["scoring"])
    print("best_paras:\n", clf.best_params_,"\n")
    print("5-fold:\n", scores,"\n")
    print("mean-score:\n",sum(scores)/len(scores),"\n")
else:
    scores = cross_val_score(clf, X, y, cv=5, scoring=config.evaluate["scoring"])
    print("paras:\n",clf.get_params(),"\n")
    print("5-fold:\n",scores,"\n")
    print("mean-score:\n",sum(scores)/len(scores),"\n")

clf=clf.fit(X, y)#不然模型加载时候会报错
mean_score=round(sum(scores)/len(scores),5)

#输出模型
joblib.dump(clf,
            "./output/" + config.data["ml_method"] + "-"+str(mean_score) + ".pkl"
            )

#转换成C
if(config.data["GridSearchCV"]):
    final_clf=clf.best_estimator_.fit(X,y)
    code=m2c.export_to_c(final_clf)
else:
    final_clf=clf.fit(X,y)
    code=m2c.export_to_c(final_clf)
f = open("./output/"+ config.data["ml_method"] + "-"+str(mean_score) + ".C", "w")
f.write(code)
f.close()
