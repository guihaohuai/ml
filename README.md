# 传统机器学习算法使用


## 1. 项目简介   
&emsp;&emsp;当我们想要使用传统机器学习算法处理某任务时，往往需要多次调参并将不同算法进行对比。本项目将多个传统算法如DT、SVM、LR、NB等统一在一个工程项目中，通过对配置文件的设置进行对多个算法的快速测试。并将模型转化为C语言，方便使用。
## 2. 目录结构
└─ml  
&emsp;├─data  
&emsp;├─models  
&emsp;│&emsp;├─NB  
&emsp;│&emsp;├─SVM  
&emsp;│&emsp;├─DT  
&emsp;│&emsp;├─KNN  
&emsp;│&emsp;├─LR  
&emsp;│&emsp;├─RF  
&emsp;│&emsp;└─XB  
&emsp;├─output  
&emsp;├─utils  
&emsp;│&emsp;└─data_tools  
&emsp;├─config.py  
&emsp;├─predict.c  
&emsp;├─predict.py  
&emsp;├─README.md  
&emsp;└─train.py


上图展现了本项目的目录结构：
### 2.1 data
&emsp;&emsp;data中保留处理好，待输入到模型中进行训练的数据。可以保留少量数据方便训练，不建议存储大量样本数据。

### 2.2 models
&emsp;&emsp;models存有基于sklearn库的机器学习算法的模型实现，返回一个estimator。可以通过config中的参数，选择是否进行自动调参。

### 2.3 output
&emsp;&emsp;output中存有最终输出的.pkl和.C的模型文件。

### 2.4 utils
&emsp;&emsp;utils下保存了数据预处理时使用到的notebooks。

### 2.5 根目录下文件
#### 2.5.1 config.py
&emsp;&emsp;该配置文件存储了各种训练需要的参数，包括读取数据路径、是否选择网格调参、各个模型手动参数配置、自动调参参数配置等。
#### 2.5.2 predict.py
&emsp;&emsp;使用output目录下的.pkl文件进行预测。
#### 2.5.3 predict.c
&emsp;&emsp;使用output目录下的.C文件进行预测。
#### 2.5.4 README
&emsp;&emsp;你正在读哦。
#### 2.5.5 train.py
&emsp;&emsp;模型训练文件，该项目入口。

## 3. 项目使用
### 3.1 设置参数
&emsp;&emsp;首先在config中设置参数，参数主要分为data、evaluate和其他各中模型。在data中选择要测试的模型和数据读取路径，以及是否选择自动调参。evaluate中可以选择模型评价方式。其他参数如DT标注着选择手动调参时设置的参数，DT_则可以设置自动调参时的参数范围。

### 3.2 模型训练
&emsp;&emsp;设置好参数后在train.py中运行，会输出模型5折交叉验证的评分，平均分，和模型参数（如果是自动调参即为最佳参数）。并在output中输出模型的.pkl和.c文件。文件名用“算法-评分”命名。此外可以在这里查看输入数据的形式，避免后续的错误。

### 3.3 测试模型
&emsp;&emsp;模型预测部分没有做更好的抽象，在这里只是简单的用单样本进行测试。.py文件加载.pkl模型就可以使用。.c文件是可调用的函数。

## 4. 其他
### 4.1 思考
+ 4.1.1 特征工程和模型部署的位置

&emsp;&emsp;该项目主要是进行模型的训练，获得表现良好的模型。其上游任务是进行特征工程，获得足够好的训练数据。下游任务是进行模型部署包括模型模块在具体环境的调用和即时输入的数据的改写（变成合适模型的输入）。这两部分都不适合进行更加具体的抽象，因而不适合放入到该项目这一模块当中。此外，考虑特征工程对数据多次改动和其本身对内存的占据，我想目前都不太适合放入该模块中。不过在utils中准备了用于特征工程的一些notebook，可以慢慢进行完善。

+ 4.1.2 模型量级和解释性

&emsp;&emsp;模型准确度固然重要，但现实任务往往需要考量其他问题，如即时性，部署内存，可解释性等。该项目中可以看到这种差异。作者在使用Titanic进行简单测试的时候，在精度相近的情况下，使用DT转换成C语言代码，文本量不算多。而使用50的RF就会有上万行的代码，10的RF也有2000余行（m2cgen转换）。前者1kb，后者集成需要2000kb和100kb左右，显然在工程上的模型部署中是值得考虑的问题。

+ 4.1.3 predict没有抽象
  
&emsp;&emsp;predict无论是c还是py都应由两个模块组成。第一是把输入变成合适模型的输入（数据处理），第二是调用模型把输入变成输出（model）。然后就可以结合成一个可调用的predict模块了。对于更多用于工程的c,就应该为其准备好特征改变的规则rule（正则化，离散化，分享等），然后在源码中相应实现。对于要求不高如竞赛等情景，py面对的数据至少有三种情况：未处理单样本数据，处理后单样本数据，表格，并且潜在存在更多可能。目前觉得没有必要做这方面抽象，因为仍然是有rule就可以写出来，所以这里只写最简单的单样本处理。

+ 4.1.4 评价方式没有抽象

&emsp;&emsp;模型评价方式的抽象还是蛮有必要的，不过目前还没有加入。但不会太麻烦，前面的工作使将来这一部分的改造会变得简单，在train和config中方便更改。

### 4.2 参考
+ 项目结构：
[link1](https://blog.csdn.net/qq_41074047/article/details/89498946)
[link2](https://www.cnblogs.com/geo-will/p/11311418.html)
+ 配置文件
[link](https://blog.csdn.net/qq_33229351/article/details/106265743?spm=1001.2101.3001.6650.1&utm_medium=distribute.pc_relevant.none-task-blog-2%7Edefault%7ECTRLIST%7ERate-1-106265743-blog-109955474.pc_relevant_paycolumn_v3&depth_1-utm_source=distribute.pc_relevant.none-task-blog-2%7Edefault%7ECTRLIST%7ERate-1-106265743-blog-109955474.pc_relevant_paycolumn_v3&utm_relevant_index=2)
+ 模型评价方式
[link](https://scikit-learn.org/stable/modules/model_evaluation.html#scoring-parameter)








