import joblib
import numpy as np

#读入数据
str_data=input("input:").split()
list_data=[float(str_data[i]) for i in range(len(str_data))]
np_data=np.array([list_data])
#print(np_data)

#加载模型
clf = joblib.load("./output/"+"DT-0.81458.pkl")

#预测输出
predict_out=clf.predict(np_data)
print("Predict:\t",predict_out)

#0.395022041	0	1	1	0	0	1	0	0	1	0	0	0	1	0
#输出[1]