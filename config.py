DEBUG = True

data = {
    #读入数据路径
    "fpath": "./data/train_v3_discrete.csv",
    #目标特征名
    "target_name": "Survived",
    #模型选择
    "ml_method":"RF",
    #自动网格调参
    "GridSearchCV": True
}

NB = {
    #NB类别
    "method": "Gaussian", #"Gaussian" "Multinomial"  "Bernoulli"  后面的方法应该对数据有特殊要求
    #Multinomial #不能使用负值
    "M_alpha": 1 ,
    "M_fit_prior": True ,
    #Bernoulli
    "B_alpha": 1 ,
    "B_fit_prior": True
}
NB_M_ = {
    "fit_prior": [True,False]
}
NB_B_ = {
    "fit_prior": [True,False]
}

SVM = {
    #核
    "kernel": 'linear',
    #惩罚系数
    "C": 1
}
SVM_ = {
    #核
    "kernel": ['linear', "poly"],
    #惩罚系数
    "C": [1,2]
}

LR = {
    "penalty":'l2',
    "dual":False,
    "tol":0.0001,
    "C":1.0,
    "fit_intercept":True,
    "intercept_scaling":1,
    "class_weight":None,
    "random_state":None,
    "solver":'liblinear',
    "max_iter":100,
    "multi_class":'ovr',
    "verbose":0,
    "warm_start":False,
    "n_jobs":1
}
LR_ = {
    "penalty":["l1",'l2'],
    "C":[1.0,2]
}

DT = {
    #划分方式
    "criterion": 'entropy',#gini
    #z最大深度
    "max_depth": 5 ,
    #可以分支的最少样本数
    "min_samples_split": 10 ,
    #叶节点最小样本数
    "min_samples_leaf": 10 ,
    #信息增益最小值
    "min_impurity_decrease": 0.001
}
DT_ = {
    #划分方式
    "criterion": ['entropy',"gini"],#gini
    #z最大深度
    "max_depth": [2,3,4,5] ,
    #可以分支的最少样本数
    "min_samples_split": [10,20] ,
    #叶节点最小样本数
    "min_samples_leaf": [10,20] ,
    #信息增益最小值
    "min_impurity_decrease": [0.001,0.01]
}

KNN = {
    "n_neighbors": 3
}
KNN_ = {
    "n_neighbors": [3,5,10]
}

RF = {
    "n_estimators" : 50,
    "criterion" : "gini",
    "max_depth" : None,
    "min_samples_split" : 2,
    "min_samples_leaf" : 1,
    "min_weight_fraction_leaf" : 0.0,
    "max_features" : "auto",
    "max_leaf_nodes" : None,
    "min_impurity_decrease" : 0.0
}
RF_ = {
    "n_estimators" : [10,20,50,80],
    "criterion" : ["entropy","gini"],
    "max_depth" : [4,8,12,None],
    "min_samples_split" : [2,5,10],
    "min_samples_leaf" : [1,10,20]
}

XB = {
    "learning_rate":0.01,
    "n_estimators":10,  # 树的个数-10棵树建立xgboost
    "max_depth":4,  # 树的深度
    "min_child_weight":1,  # 叶子节点最小权重
    "gamma":0.,  # 惩罚项中叶子结点个数前的参数
    "subsample":1,  # 所有样本建立决策树
    "colsample_btree":1,  # 所有特征建立决策树
    "scale_pos_weight":1,  # 解决样本个数不平衡的问题
    "random_state":27,  # 随机数
    "slient":0
}
XB_ = {
    "n_estimators":[10,30,60],  # 树的个数-10棵树建立xgboost
    "max_depth":[4,8,12],  # 树的深度
}

evaluate = {
    #模型评价方式：https://scikit-learn.org/stable/modules/model_evaluation.html#scoring-parameter
    "scoring":"accuracy"
}