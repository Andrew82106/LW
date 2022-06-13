import pandas as pd
import random


def extract_by_Count(ListInput, Count: int):  # 将ListInput随机分为Count和1-Count的两部分，返回Count和1-Count的部分
    ListIn = ListInput
    list_chosen = []
    while len(list_chosen) < Count and len(ListIn):
        loc = random.randint(0, len(ListIn) - 1)
        list_chosen.append(ListIn[loc])
        ListIn.pop(loc)
    return [list_chosen, ListIn]


def extract_by_Rate(ListInput, Rate: float):  # 将ListInput随机分为Rate和1-Rate的两部分，返回Rate和1-Rate的部分
    ListIn = ListInput
    length = len(ListIn)
    list_chosen = []
    while len(list_chosen) < int(Rate * length) and len(ListIn):
        loc = random.randint(0, len(ListIn) - 1)
        list_chosen.append(ListIn[loc])
        ListIn.pop(loc)
    return [list_chosen, ListIn]


def RandomList(ListInput):  # 将ListInput随机打乱
    ListIn = ListInput
    list_chosen = []
    while len(ListIn):
        loc = random.randint(0, len(ListIn) - 1)
        list_chosen.append(ListIn[loc])
        ListIn.pop(loc)
    return list_chosen


def Fusion(List1, List2, lengthA, lengthB):  # 将两个List合并,长度为lengthA，lengthB
    xii = List1
    yii = List2
    A = extract_by_Count(xii, lengthA)[0]
    B = extract_by_Count(yii, lengthB)[0]
    return RandomList(A + B)


def OutPut(ListIn_, Route, Mode):  # 将ListIn中的数据输出到Route中，文件模式为Mode，一个数据一个换行
    f = open(Route, mode=Mode, encoding='utf-8')
    ListIn = ListIn_.copy()
    while len(ListIn):
        loc = random.randint(0, len(ListIn) - 1)
        f.write(ListIn[loc] + '\n')
        ListIn.pop(loc)


class OptI:

    @staticmethod
    def getTest_and_train():  # 从开源数据集中取出训练集，全是诈骗的测试集，全是正常的测试集
        df = pd.read_excel("openSource.xls")
        normal_list = []
        fraud_list = []
        for i in df[df['label'] != 'normal']['content']:
            fraud_list.append('fraud' + '\t' + i)
        for i in df[df['label'] == 'normal']['content']:
            normal_list.append('normal' + '\t' + i)
        # 从文本中将数据读入数组中
        test_list_normal, normal_list = extract_by_Rate(normal_list, 0.2)
        test_list_fraud, fraud_list = extract_by_Rate(fraud_list, 0.2)
        # 存储抽取出来的测试集（全normal和全fraud)
        return [normal_list + fraud_list, test_list_fraud, test_list_normal]

    @staticmethod
    def deal_fraud_text():
        df = pd.read_excel("fromOnline.xls")
        datalog = []
        for i in df['content']:
            datalog.append('fraud\t' + i)
        return datalog

    def Main(self):
        route = "data_finished/"
        train, test_fraud, test_normal = self.getTest_and_train()
        test_mini = OptI.deal_fraud_text()
        # 得到训练集和三个测试集
        train_train, train_validate = extract_by_Rate(train, 0.8)
        OutPut(train_train, route + 'OPT1/train.txt', 'w')
        OutPut(train_validate, route + 'OPT1/validate.txt', 'w')
        # 输出训练集和验证集
        TestA = Fusion(test_mini, test_normal, len(test_mini), len(test_mini))
        TestB = Fusion(test_fraud, test_normal, min(len(test_fraud), len(test_normal)),
                       min(len(test_fraud), len(test_normal)))
        OutPut(TestA, route + 'OPT1/TestA.txt', 'w')
        OutPut(TestB, route + 'OPT1/TestB.txt', 'w')
        # 输出混合后的测试集
        print("end")


class OptII:

    @staticmethod
    def deal_4000_data():  # 获得生成的4000条数据
        f = open("dataMadeFromCNN/4000text.txt")
        # w = open("dataMadeFromCNN/trainDataMakeFromCnn.txt", 'w', encoding='utf-8')
        x = f.read()
        y = x.split('\n')
        cnt = 0
        ListOut = []
        for i in y:
            if len(i) < 45:
                continue
            if cnt > 4000:
                break
            cnt += 1
            i = i.replace("\n", ' ')
            ListOut.append("fraud\t" + i)
        return ListOut

    @staticmethod
    def makeTrain():
        df = pd.read_excel("openSource.xls")
        normal_list = []
        fraud_list = []
        for i in df[df['label'] != 'normal']['content']:
            fraud_list.append('fraud' + '\t' + i)
        for i in df[df['label'] == 'normal']['content']:
            normal_list.append('normal' + '\t' + i)
        # 读取开源数据中的正常文本和诈骗文本
        produced_list = OptII.deal_4000_data()
        # 读取生成的数据文本
        xi = len(normal_list)
        yi = len(fraud_list)
        zi = len(produced_list)
        Size = min(xi, yi, zi) * 2 - 10
        # 规定数据集大小
        a = Fusion(fraud_list.copy(), normal_list.copy(), int(Size * 0.5), int(Size * 0.5))
        b = Fusion(produced_list.copy(), normal_list.copy(), int(Size * 0.5), int(Size * 0.5))
        c0 = Fusion(produced_list.copy(), fraud_list.copy(), int(min(zi, yi) * 0.68), int(min(zi, yi) * 0.32))
        c = Fusion(c0.copy(), normal_list.copy(), int(Size * 0.5), int(Size * 0.5))
        if len(a) != len(b) or len(b) != len(c):
            print("ERROR")
        else:
            print("len(a)={} len(b)={} len(c)={}".format(len(a), len(b), len(c)))
        # 混合数据集
        a0, a1 = extract_by_Rate(a, 0.8)
        OutPut(a0, 'data_finished/OPT2/Train_fraud_list_normal_list.txt', 'w')
        OutPut(a1, 'data_finished/OPT2/Validate_fraud_list_normal_list.txt', 'w')
        b0, b1 = extract_by_Rate(b, 0.8)
        OutPut(b0, 'data_finished/OPT2/Train_produced_list_normal_list.txt', 'w')
        OutPut(b1, 'data_finished/OPT2/Validate_produced_list_normal_list.txt', 'w')
        c0, c1 = extract_by_Rate(c, 0.8)
        OutPut(c0, 'data_finished/OPT2/Train_fraud_list_produced_list_normal_list.txt', 'w')
        OutPut(c1, 'data_finished/OPT2/Validate_fraud_list_produced_list_normal_list.txt', 'w')
        # 输出训练集

    @staticmethod
    def Main():
        OptII.makeTrain()
        # 从输出混合后的训练集至文件


class OptIII:

    @staticmethod
    def deal_4000_data():  # 获得生成的4000条数据
        f = open("/Users/andrewlee/Desktop/Projects/LW/datalog/data_finished/OPT3/Modified_Make.txt")
        # w = open("dataMadeFromCNN/trainDataMakeFromCnn.txt", 'w', encoding='utf-8')
        x = f.read()
        y = x.split('\n')
        cnt = 0
        ListOut = []
        for i in y:
            if len(i) < 45:
                continue
            if cnt > 4000:
                break
            cnt += 1
            i = i.replace("\n", ' ')
            ListOut.append("fraud\t" + i)
        return ListOut

    @staticmethod
    def makeTrain():
        df = pd.read_excel("openSource.xls")
        normal_list = []
        fraud_list = []
        for i in df[df['label'] != 'normal']['content']:
            fraud_list.append('fraud' + '\t' + i)
        for i in df[df['label'] == 'normal']['content']:
            normal_list.append('normal' + '\t' + i)
        # 读取开源数据中的正常文本和诈骗文本
        produced_list = OptIII.deal_4000_data()
        # 读取生成的数据文本
        xi = len(normal_list)
        yi = len(fraud_list)
        zi = len(produced_list)
        Size = min(xi, yi, zi) * 2 - 10
        # 规定数据集大小
        a = Fusion(fraud_list.copy(), normal_list.copy(), int(Size * 0.5), int(Size * 0.5))
        b = Fusion(produced_list.copy(), normal_list.copy(), int(Size * 0.5), int(Size * 0.5))
        c0 = Fusion(produced_list.copy(), fraud_list.copy(), int(min(zi, yi) * 0.5), int(min(zi, yi) * 0.5))
        c = Fusion(c0.copy(), normal_list.copy(), int(Size * 0.5), int(Size * 0.5))
        if len(a) != len(b) or len(b) != len(c):
            print("ERROR")
        else:
            print("len(a)={} len(b)={} len(c)={}".format(len(a), len(b), len(c)))
        # 混合数据集
        a0, a1 = extract_by_Rate(a, 0.8)
        OutPut(a0, 'data_finished/OPT3/Train_fraud_list_normal_list.txt', 'w')
        OutPut(a1, 'data_finished/OPT3/Validate_fraud_list_normal_list.txt', 'w')
        b0, b1 = extract_by_Rate(b, 0.8)
        OutPut(b0, 'data_finished/OPT3/Train_produced_list_normal_list.txt', 'w')
        OutPut(b1, 'data_finished/OPT3/Validate_produced_list_normal_list.txt', 'w')
        c0, c1 = extract_by_Rate(c, 0.8)
        OutPut(c0, 'data_finished/OPT3/Train_fraud_list_produced_list_normal_list.txt', 'w')
        OutPut(c1, 'data_finished/OPT3/Validate_fraud_list_produced_list_normal_list.txt', 'w')
        # 输出训练集

    @staticmethod
    def Main():
        OptIII.makeTrain()
        # 从输出混合后的训练集至文件


class OptMain:

    @staticmethod
    def deal_4000_data():  # 获得生成的4000条数据
        f = open("/Users/andrewlee/Desktop/Projects/LW/datalog/data_finished/OPT3/Modified_Make.txt")
        # w = open("dataMadeFromCNN/trainDataMakeFromCnn.txt", 'w', encoding='utf-8')
        x = f.read()
        y = x.split('\n')
        cnt = 0
        ListOut = []
        for i in y:
            if len(i) < 45:
                continue
            if cnt > 4000:
                break
            cnt += 1
            i = i.replace("\n", ' ')
            ListOut.append("fraud\t" + i)
        return ListOut

    @staticmethod
    def makeTrain(rate0=0.5, rate1=0.5, rate2=0.5, rate3=0.5, rate_val=0.8):  # 输出训练数据
        df = pd.read_excel("/Users/andrewlee/Desktop/Projects/LW/datalog/openSource.xls")
        normal_list = []
        fraud_list = []
        for i in df[df['label'] != 'normal']['content']:
            fraud_list.append('fraud' + '\t' + i)
        for i in df[df['label'] == 'normal']['content']:
            normal_list.append('normal' + '\t' + i)
        print("读取开源数据中的正常文本和诈骗文本")
        # 读取开源数据中的正常文本和诈骗文本
        produced_list = OptMain.deal_4000_data()
        print("读取生成的数据文本")
        # 读取生成的数据文本
        xi = len(normal_list)
        yi = len(fraud_list)
        zi = len(produced_list)
        Size = min(xi, yi, zi) * 2 - 10
        # 规定数据集大小
        a = Fusion(fraud_list.copy(), normal_list.copy(), int(Size * rate0), int(Size * (1 - rate0)))
        b = Fusion(produced_list.copy(), normal_list.copy(), int(Size * rate1), int(Size * (1 - rate1)))
        c0 = Fusion(produced_list.copy(), fraud_list.copy(), int(Size * rate2), int(Size * (1 - rate2)))
        c = Fusion(c0.copy(), normal_list.copy(), int(Size * rate3), int(Size * (1 - rate3)))
        if len(a) != len(b) or len(b) != len(c):
            print("生成的三个数据集大小不同")
        else:
            print("len(a)={} len(b)={} len(c)={}".format(len(a), len(b), len(c)))
        print("混合数据集")
        # 混合数据集
        a0, a1 = extract_by_Rate(a, rate_val)
        OutPut(a0, '/Users/andrewlee/Desktop/Projects/LW/datalog/data_finished/OPT3/Train_fraud_list_normal_list.txt', 'w')
        OutPut(a1, '/Users/andrewlee/Desktop/Projects/LW/datalog/data_finished/OPT3/Validate_fraud_list_normal_list.txt', 'w')
        b0, b1 = extract_by_Rate(b, rate_val)
        OutPut(b0, '/Users/andrewlee/Desktop/Projects/LW/datalog/data_finished/OPT3/Train_produced_list_normal_list.txt', 'w')
        OutPut(b1, '/Users/andrewlee/Desktop/Projects/LW/datalog/data_finished/OPT3/Validate_produced_list_normal_list.txt', 'w')
        c0, c1 = extract_by_Rate(c, rate_val)
        OutPut(c0, '/Users/andrewlee/Desktop/Projects/LW/datalog/data_finished/OPT3/Train_fraud_list_produced_list_normal_list.txt', 'w')
        OutPut(c1, '/Users/andrewlee/Desktop/Projects/LW/datalog/data_finished/OPT3/Validate_fraud_list_produced_list_normal_list.txt', 'w')
        print("输出训练集")
        # 输出训练集

    @staticmethod
    def OutputFusion(rate: float, rate1: float, val_rate: float):  # 生成诈骗集和诈骗集之比,生成诈骗集和诈骗集所得集合和正常集之比,训练集和验证集的比例
        df = pd.read_excel("/Users/andrewlee/Desktop/Projects/LW/datalog/openSource.xls")
        normal_list = []
        fraud_list = []
        for i in df[df['label'] != 'normal']['content']:
            fraud_list.append('fraud' + '\t' + i)
        for i in df[df['label'] == 'normal']['content']:
            normal_list.append('normal' + '\t' + i)
        print("读取开源数据中的正常文本和诈骗文本")
        # 读取开源数据中的正常文本和诈骗文本
        produced_list = OptMain.deal_4000_data()
        print("读取生成的数据文本")
        # 读取生成的数据文本
        xi = len(normal_list)
        yi = len(fraud_list)
        zi = len(produced_list)
        Size = min(xi, yi, zi) * 2 - 10
        # 规定数据集大小
        c0 = Fusion(produced_list.copy(), fraud_list.copy(), int(Size * rate), int(Size * (1 - rate)))
        print("INFO:生成诈骗数据集和自然诈骗数据集之比：{}".format(rate))
        c = Fusion(c0.copy(), normal_list.copy(), int(Size * rate1), int(Size * (1 - rate1)))
        print("INFO:生成诈骗集和诈骗集所得集合和正常集之比：{}".format(rate1))
        print("INFO:混合数据集")
        # 混合数据集
        c0, c1 = extract_by_Rate(c, val_rate)
        print("INFO:训练集和验证集的比：{}".format(val_rate))
        OutPut(c0,
               '/Users/andrewlee/Desktop/Projects/LW/datalog/data_finished/OPT3/Train_fraud_list_produced_list_normal_list.txt',
               'w')
        OutPut(c1,
               '/Users/andrewlee/Desktop/Projects/LW/datalog/data_finished/OPT3/Validate_fraud_list_produced_list_normal_list.txt',
               'w')
        print("输出训练集")

    @staticmethod
    def Main():
        while 1:
            try:
                x = input("输入训练数据参数（空格分隔）\n"
                          "1:诈骗集和正常集之比\n"
                          "2:生成诈骗集和正常集之比\n"
                          "3:生成诈骗集和诈骗集之比\n"
                          "4:生成诈骗集和诈骗集所得集合和正常集之比:").split(' ')
                if len(x) != 4:
                    continue
                break
            except Exception as E:
                print(E)

        OptMain.makeTrain(float(x[0]), float(x[1]), float(x[2]), float(x[3]))
        # 从输出混合后的训练集至文件


if __name__ == '__main__':
    OptMain.Main()
