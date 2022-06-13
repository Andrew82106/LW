import os
import time

dataDealing_Route = "/Users/andrewlee/Desktop/Projects/LW/datalog/datadealing.py"
import datalog.datadealing as DD


def awakeLSTMtoTest(Model: str):
    os.system('cd ..&&cd ..&&cd ..&&cd text-classification-cnn-rnn&&python run_rnn.py test {}'.format(Model))
    # 转到地址并运行
    f = open("/Users/andrewlee/Desktop/Projects/LW/text-classification-cnn-rnn/acc.txt", 'r', encoding='utf-8')
    acc = float(f.read())
    # 读取训练得到的准确度
    return acc


def awakeLSTMtoTrain(Model: str):
    if os.path.exists("/Users/andrewlee/Desktop/Projects/LW/text-classification-cnn-rnn/tensorboard"):
        print("INFO：TrainFileExist.")
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
        print("INFO：TrainFileExist.")
        os.system("rm -r /Users/andrewlee/Desktop/Projects/LW/text-classification-cnn-rnn/tensorboard")
    os.system('cd ..&&cd ..&&cd ..&&cd text-classification-cnn-rnn&& python run_cnn.py train')
    # 转到地址并运行


def RunManual():
    opt0 = int(input("是否需要重新生成训练数据？0-->不需要,非0-->需要:"))
    if opt0:
        DD.OptMain.Main()
    opt = int(input("规定训练集：0：正常+开源诈骗数据集，1：正常+生成诈骗数据集，2：正常+混合数据集:"))
    opt2 = int(input("规定验证集：0：诈骗数据小样本，1：开源诈骗数据集:"))
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
    opt5 = input("规定训练模型：lstm gru cnn:")
    if opt5 == 'cnn':
        awakeCNNtoTrain()
        awakeCNNtoTest()
    elif opt5 == 'lstm':
        awakeLSTMtoTrain(opt5)
        awakeLSTMtoTest(opt5)
    elif opt5 == 'gru':
        awakeLSTMtoTrain(opt5)
        awakeLSTMtoTest(opt5)
    else:
        print("ERROR，默认为cnn运行")
        awakeCNNtoTrain()
        awakeCNNtoTest()
    f4.close()
    f5.close()


def RunAuto(opt, opt2, opt5):
    # opt0 = int(input("是否需要重新生成训练数据？0-->不需要,非0-->需要:"))
    # opt = int(input("规定训练集：0：正常+开源诈骗数据集，1：正常+生成诈骗数据集，2：正常+混合数据集:"))
    # opt2 = int(input("规定验证集：0：诈骗数据小样本，1：开源诈骗数据集:"))
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
    # opt5 = input("规定训练模型：lstm gru cnn:")
    if opt5 == 'cnn':
        awakeCNNtoTrain()
        awakeCNNtoTest()
    elif opt5 == 'lstm':
        awakeLSTMtoTrain(opt5)
        awakeLSTMtoTest(opt5)
    elif opt5 == 'gru':
        awakeLSTMtoTrain(opt5)
        awakeLSTMtoTest(opt5)
    else:
        print("INFO：ERROR，默认为cnn运行")
        awakeCNNtoTrain()
        awakeCNNtoTest()
    f4.close()
    f5.close()


def runFileMode():
    f = open("allocate.txt", 'r', encoding='utf-8')
    command_line = str(f.read()).split('\n')
    cnt = 1
    for i in command_line:
        if cnt % 6 == 0:
            print("INFO：模型睡眠60秒，CPU降温中")
            time.sleep(5 * 60)
        x = str(i).split()
        if len(x) != 7:
            print("INFO：命令{}无效".format(i))
            continue
        if x[0] == '0':
            RunAuto(int(x[1]), int(x[2]), x[3])
            dicName = {'0': "正常+开源诈骗数据集", '1': "正常+生成诈骗数据集", '2': "正常+混合数据集"}
            dicName2 = {'0': "诈骗数据小样本", '1': "开源诈骗数据集"}
            f0 = open("/Users/andrewlee/Desktop/Projects/LW/text-classification-cnn-rnn/acc.txt", 'r', encoding='utf-8')
            acc0 = float(f0.read())
            f0.close()
            print("未重新生成数据")
            print("训练集:{}\n验证集:{}\n训练模型:{}\n生成诈骗集和诈骗集之比:{}\n生成诈骗集和诈骗集所得集合和正常集之比:{}\n训练集和验证集的比例:{}\n准确度:{}".format(
                dicName[x[1]],
                dicName2[x[2]],
                x[3],
                x[4],
                x[5],
                x[6],
                acc0))
            f0 = open("/Users/andrewlee/Desktop/Projects/LW/datalog/data_finished/OPT3/outputdata.txt", "a",
                      encoding='utf-8')
            f0.write(
                ">>>>>>>>>>>>>>>>>>>\n未重新生成数据\n训练集:{}\n验证集:{}\n训练模型:{}\n生成诈骗集和诈骗集之比:{}\n生成诈骗集和诈骗集所得集合和正常集之比:{}\n训练集和验证集的比例:{}\n准确度:{}\n".format(
                    dicName[x[1]],
                    dicName2[x[2]],
                    x[3],
                    x[4],
                    x[5],
                    x[6],
                    acc0))
            f0.close()
        else:
            DD.OptMain.OutputFusion(float(x[4]), float(x[5]), float(x[6]))
            RunAuto(int(x[1]), int(x[2]), x[3])
            dicName = {'0': "正常+开源诈骗数据集", '1': "正常+生成诈骗数据集", '2': "正常+混合数据集"}
            dicName2 = {'0': "诈骗数据小样本", '1': "开源诈骗数据集"}
            f0 = open("/Users/andrewlee/Desktop/Projects/LW/text-classification-cnn-rnn/acc.txt", 'r', encoding='utf-8')
            acc0 = float(f0.read())
            f0.close()
            print("已经重新生成数据")
            print("训练集:{}\n验证集:{}\n训练模型:{}\n生成诈骗集和诈骗集之比:{}\n生成诈骗集和诈骗集所得集合和正常集之比:{}\n训练集和验证集的比例:{}\n准确度:{}".format(
                dicName[x[1]],
                dicName2[x[2]],
                x[3],
                x[4],
                x[5],
                x[6],
                acc0))
            f0 = open("/Users/andrewlee/Desktop/Projects/LW/datalog/data_finished/OPT3/outputdata.txt", "a",
                      encoding='utf-8')
            f0.write(
                ">>>>>>>>>>>>>>>>>>>\n已经重新生成数据\n训练集:{}\n验证集:{}\n训练模型:{}\n生成诈骗集和诈骗集之比:{}\n生成诈骗集和诈骗集所得集合和正常集之比:{}\n训练集和验证集的比例:{}\n准确度:{}\n".format(
                    dicName[x[1]],
                    dicName2[x[2]],
                    x[3],
                    x[4],
                    x[5],
                    x[6],
                    acc0))
            f0.close()
        cnt += 1
    f.close()


if __name__ == '__main__':
    runFileMode()
