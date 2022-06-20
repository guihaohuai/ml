from xgboost import XGBClassifier
import config
from sklearn.model_selection import GridSearchCV

def Model():
    if(config.data["GridSearchCV"]):
        clf=GridSearchCV(
            XGBClassifier(),
            config.XB_,
            refit = True,
            cv = 5,
            scoring=config.evaluate["scoring"],
            n_jobs=-1
        )
    else:
        #https://blog.csdn.net/qq_38923076/article/details/82931340
        clf = XGBClassifier(
            learning_rate=config.XB["learning_rate"],
            n_estimators=config.XB["n_estimators"],  # 树的个数-10棵树建立xgboost
            max_depth=config.XB["max_depth"],  # 树的深度
            min_child_weight=config.XB["min_child_weight"],  # 叶子节点最小权重
            gamma=config.XB["gamma"],  # 惩罚项中叶子结点个数前的参数
            subsample=config.XB["subsample"],  # 所有样本建立决策树
            colsample_btree=config.XB["colsample_btree"],  # 所有特征建立决策树
            scale_pos_weight=config.XB["scale_pos_weight"],  # 解决样本个数不平衡的问题
            random_state=config.XB["random_state"],  # 随机数
            slient=config.XB["slient"]
        )
    return clf