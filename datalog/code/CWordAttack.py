import WordCut
import pandas as pd
import awakeNeuralNetwork as NW
import basicFunction
import opencc
import random
import warnings
import time
from xpinyin import Pinyin

cc = opencc.OpenCC('s2t')
warnings.filterwarnings('ignore')
testRoute = '/Users/andrewlee/Desktop/Projects/LW/text-classification-cnn-rnn/data/cnews/cnews.test.txt'
# 测试集的地址,用于存放
TrainTXT_Made_Route = '/Users/andrewlee/Desktop/Projects/LW/datalog/dataMadeFromCNN/4000text.txt'
# 造出来的训练集的地址
trainRoute = '/Users/andrewlee/Desktop/Projects/LW/text-classification-cnn-rnn/data/cnews/cnews.train.txt'
valRoute = '/Users/andrewlee/Desktop/Projects/LW/text-classification-cnn-rnn/data/cnews/cnews.val.txt'
normalRoute = '/Users/andrewlee/Desktop/Projects/LW/datalog/data_finished/OPT3/Normal.txt'
# 训练集和验证集


def get_time(fmt: str = '%Y-%m-%d %H-%M-%S') -> str:  # 获得当前时间
    ts = time.time()
    ta = time.localtime(ts)
    t = time.strftime(fmt, ta)
    return t


def CWordAttack_OnWord(WordIn: str):  # 修改单个词语，四种mode都有，可改
    if len(WordIn) <= 0:
        return '0'
    x_ = random.randint(0, 4) % 3
    if x_ == 0:  # 转繁体
        return cc.convert(WordIn)
    elif x_ == 1:  # 扰动（直接翻转)
        l = list(WordIn)
        l.reverse()
        result = "".join(l)
        return result
    elif x_ == 2:  # 拆解
        LEN = len(WordIn)
        pos = random.randint(0, LEN - 1)
        return WordIn[0:pos] + '#-#' + WordIn[pos:LEN]
    else:  # 转拼音
        p = Pinyin()
        result1 = p.get_pinyin(WordIn)
        return result1


def FusionText(ListIn):  # 将二维列表里面的词语汇总，从而便于放到测试集中去测试
    res = ''
    for sen in ListIn:
        for Word in sen:
            res += str(Word)
    return res


def FusionText1(ListIn):  # 将一维列表里面的词语汇总，从而便于放到测试集中去测试
    res = ''
    for Word in ListIn:
        res += str(Word)
    return res


def readText(Route, splitchar: str):  # 读入txt文本，将文本中的数据汇总成列表，返回列表
    # 其中，文本的格式是：一条数据后跟两个回车，下面的代码就是使用两个连续的回车来分割数据的
    f = open(Route, 'r', encoding='utf-8')
    s = f.read()
    f.close()
    TrainList = s.split(splitchar)
    for i in range(0, len(TrainList), 1):
        TrainList[i] = str(TrainList[i]).replace('。', '，')
    return TrainList


def readOpenSource():  # 从开源数据集中读入所有正常文本，用于后续训练
    df = pd.read_excel("../openSource.xls")
    f = open(normalRoute, 'w', encoding='utf-8')
    for i in df[df['label'] == 'normal']['content']:
        f.write(i + '\n\n')
    f.close()


def outputTrain(normal__, train__, validate__):
    # 读取正常文本集
    normal_ = []
    train_ = []
    validate_ = []
    for i in normal__:
        normal_.append("normal\t{}".format(i))
    for i in train__:
        train_.append("fraud\t{}".format(i))
    for i in validate__:
        validate_.append("fraud\t{}".format(i))
    train = basicFunction.Fusion(normal_, train_, int(len(normal_) * 0.8), len(train_))
    f = open(trainRoute, 'w', encoding='utf-8')
    for i in train:
        x = str(i).replace('\n', '')
        f.write(str(x) + '\n')
    f.close()
    # 输出训练集
    validate = basicFunction.Fusion(normal_, validate_, int(len(normal_) * 0.2), len(validate_))
    f1 = open(valRoute, 'w', encoding='utf-8')
    for i in validate:
        x = str(i).replace('\n', '')
        f1.write(str(x) + '\n')
    f1.close()
    # 输出验证集


"""def modifyTrain():
    F = open("../data_finished/OPT3/runLog.txt", "a", encoding='utf-8')
    F.write('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>Train:'+str(get_time())+'\n')
    TrainList = readText(TrainTXT_Made_Route, '\n\n')
    train, validate = basicFunction.extract_by_Rate(TrainList, 0.8)
    # 读取训练数据，拆分成训练集和验证集
    normal = readText(normalRoute, '\n\n')
    outputTrain(normal, train, validate)
    NW.awakeLSTMtoTrain()
    ori_acc = NW.awakeLSTMtoTest()  # 记录原准确度
    print("原准确度：{}".format(ori_acc))
    F.write("原准确度：{}".format(ori_acc)+'\n')
    F.close()
    maxDelta = -1  # 比一下最大变化量
    maxPos = []  # 记录一下最大变化度的词语位置
    for sentence_id in range(0, len(train), 1):
        print("当前句：{}".format(train[sentence_id]))
        F = open("../data_finished/OPT3/runLog.txt", "a", encoding='utf-8')
        F.write("当前句：{}".format(train[sentence_id]) + '\n')
        F.close()
        cut = WordCut.WordCut(train[sentence_id])
        cut = cut[0]
        # 利用分词接口将训练集中的当前句进行分词
        for word_id in range(0, len(cut), 1):
            F = open("../data_finished/OPT3/runLog.txt", "a", encoding='utf-8')
            ori_word = cut[word_id]
            print("原词汇：{}".format(ori_word))
            newWord = CWordAttack_OnWord(cut[word_id])
            print("新词汇：{}".format(newWord))
            if ori_word == newWord:
                continue
            F.write("原词汇：{}-->".format(ori_word))
            F.write("新词汇：{}".format(newWord) + '\n')
            cut[word_id] = newWord
            train[sentence_id] = FusionText1(cut)
            # 对词语进行修改
            outputTrain(normal, train, validate)
            NW.awakeLSTMtoTrain()
            new_acc = NW.awakeLSTMtoTest()
            print("新准确度:{}".format(new_acc))
            F.write("新准确度:{}".format(new_acc) + ' ')
            if abs(new_acc - ori_acc) > maxDelta:
                maxDelta = abs(new_acc - ori_acc)
                maxPos = [sentence_id, word_id]
            F.write("delta:{}".format(abs(new_acc - ori_acc)) + ' ' + '\n')
            # 训练得到新准确度
            cut[word_id] = ori_word
            train[sentence_id] = FusionText1(cut)
            F.close()
            # 恢复当前词语，准备对下一个词语进行修改
    return maxPos"""


def modifyTXT_Made():
    TrainList = readText(TrainTXT_Made_Route, '\n\n')
    for sentence_id in range(0, len(TrainList), 1):
        if len(TrainList[sentence_id]) == 0:
            continue
        print("当前句：{}".format(TrainList[sentence_id]))
        try:
            cut = WordCut.WordCut(TrainList[sentence_id])
            cnt_ = 0
            while cnt_ < 100:
                cnt_ += 1
                pos = random.randint(0, len(cut)-1)
                if len(cut[pos]) == 1:
                    continue
                newWord = CWordAttack_OnWord(cut[pos])
                if newWord != cut[pos]:
                    cut[pos] = newWord
                    break
            TrainList[sentence_id] = FusionText1(cut)
            print("改后句：{}".format(TrainList[sentence_id]))
        except Exception as e:
            print(e)
            raise ImportError
    route = "/Users/andrewlee/Desktop/Projects/LW/datalog/data_finished/OPT3/Modified_Make.txt"
    F = open(route, 'w', encoding='utf-8')
    for i in TrainList:
        x = i.replace("\n", '')
        F.write(x+"\n\n")


if __name__ == '__main__':
    # NW.awakeLSTMtoTrain()
    modifyTXT_Made()