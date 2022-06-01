import os


def awakeLSTMtoTest():
    os.system('cd ..&&cd ..&&cd ..&&cd text-classification-cnn-rnn&&python run_rnn.py test')
    # 转到地址并运行
    f = open("/Users/andrewlee/Desktop/Projects/LW/text-classification-cnn-rnn/acc.txt", 'r', encoding='utf-8')
    acc = float(f.read())
    # 读取训练得到的准确度
    return acc


def awakeLSTMtoTrain():
    if os.path.exists("/Users/andrewlee/Desktop/Projects/LW/text-classification-cnn-rnn/tensorboard"):
        print("TrainFileExist.")
        os.system("rm -r /Users/andrewlee/Desktop/Projects/LW/text-classification-cnn-rnn/tensorboard")
    os.system('cd ..&&cd ..&&cd ..&&cd text-classification-cnn-rnn&& python run_rnn.py train')
    # 转到地址并运行


def awakeCNNtoTest():
    os.system('cd ..&&cd ..&&cd ..&&cd text-classification-cnn-rnn&&python run_cnn.py test')
    # 转到地址并运行
    f = open("/Users/andrewlee/Desktop/Projects/LW/text-classification-cnn-rnn/acc.txt", 'r', encoding='utf-8')
    acc = float(f.read())
    # 读取训练得到的准确度
    return acc


def awakeCNNtoTrain():
    if os.path.exists("/Users/andrewlee/Desktop/Projects/LW/text-classification-cnn-rnn/tensorboard"):
        print("TrainFileExist.")
        os.system("rm -r /Users/andrewlee/Desktop/Projects/LW/text-classification-cnn-rnn/tensorboard")
    os.system('cd ..&&cd ..&&cd ..&&cd text-classification-cnn-rnn&& python run_cnn.py train')
    # 转到地址并运行


if __name__ == '__main__':
    TrainRoute = [
        "/Users/andrewlee/Desktop/Projects/LW/datalog/data_finished/OPT3/Train_fraud_list_normal_list.txt",
        "/Users/andrewlee/Desktop/Projects/LW/datalog/data_finished/OPT3/Train_produced_list_normal_list.txt",
        "/Users/andrewlee/Desktop/Projects/LW/datalog/data_finished/OPT3/Train_fraud_list_produced_list_normal_list.txt"
    ]
    # 训练集地址：正常+开源诈骗数据集，正常+生成诈骗数据集的对抗样本，正常+混合数据集
    ValRoute = [
        "/Users/andrewlee/Desktop/Projects/LW/datalog/data_finished/OPT3/Validate_fraud_list_normal_list.txt",
        "/Users/andrewlee/Desktop/Projects/LW/datalog/data_finished/OPT3/Validate_produced_list_normal_list.txt",
        "/Users/andrewlee/Desktop/Projects/LW/datalog/data_finished/OPT3/Validate_fraud_list_produced_list_normal_list.txt"
    ]
    # 验证集地址：正常+开源诈骗数据集，正常+生成诈骗数据集的对抗样本，正常+混合数据集
    FraudMiniRoute = "/Users/andrewlee/Desktop/Projects/LW/datalog/data_finished/OPT1/TestA.txt"
    FraudOpenSource = "/Users/andrewlee/Desktop/Projects/LW/datalog/data_finished/OPT1/TestB.txt"
    # 测试集地址：诈骗数据小样本，开源诈骗数据集
    ModelTrainRoute = "/Users/andrewlee/Desktop/Projects/LW/text-classification-cnn-rnn/data/cnews/cnews.train.txt"
    ModelValRoute = "/Users/andrewlee/Desktop/Projects/LW/text-classification-cnn-rnn/data/cnews/cnews.val.txt"
    ModelTestRoute = "/Users/andrewlee/Desktop/Projects/LW/text-classification-cnn-rnn/data/cnews/cnews.test.txt"
    # 模型训练数据接口地址：训练地址接口，验证地址接口，测试地址接口
    cnt = 1
    f = open(TrainRoute[cnt], 'r', encoding='utf-8')
    f1 = open(ModelTrainRoute, 'w', encoding='utf-8')
    f2 = open(ValRoute[cnt], 'r', encoding='utf-8')
    f3 = open(ModelValRoute, 'w', encoding='utf-8')
    # 规定训练集和验证集
    f4 = open(FraudOpenSource, 'r', encoding='utf-8')
    f5 = open(ModelTestRoute, 'w', encoding='utf=8')
    # 规定测试集
    f1.write(f.read())
    f3.write(f2.read())
    f5.write(f4.read())
    awakeLSTMtoTrain()
    awakeLSTMtoTest()
    f4.close()
    f5.close()
    # >>>>>>>>>>训练开源测试集
    f4 = open(FraudMiniRoute, 'r', encoding='utf-8')
    f5 = open(ModelTestRoute, 'w', encoding='utf=8')
    # 规定测试集
    f5.write(f4.read())
    awakeLSTMtoTest()
    # >>>>>>>>>>训练小样本测试集
    # awakeCNNtoTrain()
    # awakeCNNtoTest()
