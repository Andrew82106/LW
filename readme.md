# 主要代码

``datalog/code``中：

 - awakeNeuralNetwork.py:调用神经网络（由于调用rnn时间成本太大，因此选择调用cnn）
 - basicFunction.py:列表的一些基本操作，用于混合训练集
 - CWordAttack.py:CWordAttack算法主体部分，运行这份代码就可以开始CWordAttack算法
 - WordCut.py:提供分词功能

# 主要数据

``datalog/data_finished``中：

 - OPT3文件夹是第三个实验的文件夹
 - OPT3文件夹中的runLog.txt存放CWordAttack算法运行记录
 - OPT3文件夹中的Normal.txt是从开源数据集中提取出来的正常文本

``text-classification-cnn-rnn/data/cnews``中：

 - cnews.train.txt:是训练集入口
 - cnews.test.txt:是测试集入口
 - cnews.val.txt:是验证集入口