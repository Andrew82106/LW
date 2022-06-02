import os
dataDealing_Route = "/Users/andrewlee/Desktop/Projects/LW/datalog/datadealing.py"
import datalog.datadealing as DD


def awakeLSTMtoTest():
    os.system('cd ..&&cd ..&&cd ..&&cd text-classification-cnn-rnn&&python run_rnn.py test')
    # 转到地址并运行
    f = open("/Users/andrewlee/Desktop/Projects/LW/text-classification-cnn-rnn/acc.txt", 'r', encoding='utf-8')
    acc = float(f.read())
    # 读取训练得到的准确度
    return acc


def awakeLSTMtoTrain(Model: str):
    if os.path.exists("/Users/andrewlee/Desktop/Projects/LW/text-classification-cnn-rnn/tensorboard"):
        print("TrainFileExist.")
        os.system("rm -r /Users/andrewlee/Desktop/Projects/LW/text-classification-cnn-rnn/tensorboard")
    os.system('cd ..&&cd ..&&cd ..&&cd text-classification-cnn-rnn&& python run_rnn.py train {}'.format(Model))
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


def Run():
    opt0 = int(input("是否需要重新生成训练数据？0-->不需要,非0-->需要"))
    if opt0:
        DD.OptMain.Main()
    opt = int(input("规定训练集：0：正常+开源诈骗数据集，1：正常+生成诈骗数据集的对抗样本，2：正常+混合数据集"))
    opt2 = int(input("规定验证集：0：诈骗数据小样本，1：开源诈骗数据集"))
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
    TestRoute = [
        "/Users/andrewlee/Desktop/Projects/LW/datalog/data_finished/OPT1/TestA.txt",
        "/Users/andrewlee/Desktop/Projects/LW/datalog/data_finished/OPT1/TestB.txt"
    ]
    # 测试集地址：诈骗数据小样本，开源诈骗数据集
    ModelTrainRoute = "/Users/andrewlee/Desktop/Projects/LW/text-classification-cnn-rnn/data/cnews/cnews.train.txt"
    ModelValRoute = "/Users/andrewlee/Desktop/Projects/LW/text-classification-cnn-rnn/data/cnews/cnews.val.txt"
    ModelTestRoute = "/Users/andrewlee/Desktop/Projects/LW/text-classification-cnn-rnn/data/cnews/cnews.test.txt"
    # 模型训练数据接口地址：训练地址接口，验证地址接口，测试地址接口
    f = open(TrainRoute[opt], 'r', encoding='utf-8')
    f1 = open(ModelTrainRoute, 'w', encoding='utf-8')
    f2 = open(ValRoute[opt], 'r', encoding='utf-8')
    f3 = open(ModelValRoute, 'w', encoding='utf-8')
    # 规定训练集和验证集
    f4 = open(TestRoute[opt2], 'r', encoding='utf-8')
    f5 = open(ModelTestRoute, 'w', encoding='utf=8')
    # 规定测试集
    f1.write(f.read())
    f3.write(f2.read())
    f5.write(f4.read())
    # 输入测试集，验证集和训练集
    opt5 = input("规定训练模型：lstm gru cnn")
    if opt5 == 'cnn':
        awakeCNNtoTrain()
        awakeCNNtoTest()
    elif opt5 == 'lstm':
        awakeLSTMtoTrain(opt5)
        awakeLSTMtoTest()
    elif opt5 == 'gru':
        awakeLSTMtoTrain(opt5)
        awakeLSTMtoTest()
    else:
        print("ERROR，默认为cnn运行")
        awakeCNNtoTrain()
        awakeCNNtoTest()
    f4.close()
    f5.close()


if __name__ == '__main__':
    Run()