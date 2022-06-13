# 快速开始

运行``datalog/OPT3/allocate.py``即可

# 主要代码

``datalog/code``中：

 - awakeNeuralNetwork.py:调用神经网络（可选择调用cnn或者rnn，至于是调用rnn中的lstm还是gru就需要在``text-classification-cnn-rnn/rnn_model.py``中进行设置）
 - basicFunction.py:列表的一些基本操作，用于混合训练集
 - CWordAttack.py:CWordAttack算法主体部分
 - WordCut.py:提供分词功能

``datalog/OPT3``中：

 - allocate.py：用于配置模型训练文件和调度训练任务
 - allocate.txt：用于配置运行规则： 
   - 是否重新生成训练数据（0，1） 
   - 规定训练集（0：正常+开源诈骗数据集，1：正常+生成诈骗数据集，2：正常+混合数据集） 
   - 规定验证集（0：诈骗数据小样本，1：开源诈骗数据集）
   - 规定训练模型（lstm gru cnn）
   - 规定生成诈骗集和诈骗集之比
   - 规定生成诈骗集和诈骗集所得集合和正常集之比
   - 规定训练集和验证集的比例

``datalog``中：

 - datadealing.py：用于生成实验1，2，3的相关数据



# 主要数据

``datalog/data_finished``中：

 - OPT1是第一个实验的文件夹，里面的TestA.txt是诈骗数据的小样本，TextB.txt是开源诈骗数据集
 - OPT3文件夹是第三个实验的文件夹
 - OPT3文件夹中的runLog.txt存放CWordAttack算法运行记录
 - OPT3文件夹中的Normal.txt是从开源数据集中提取出来的正常文本

``text-classification-cnn-rnn/data/cnews``中：

 - cnews.train.txt:是训练集入口
 - cnews.test.txt:是测试集入口
 - cnews.val.txt:是验证集入口