import pandas as pd
import opencc
import random
import warnings
import time
from xpinyin import Pinyin
import jieba
import time
import tqdm


cc = opencc.OpenCC('s2t')
warnings.filterwarnings('ignore')


def WordCut(TextIn: str):
    return jieba.lcut(TextIn, cut_all=False)


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


def readText(Route, splitchar: str):  # 读入txt文本，将文本中的数据汇总成列表，返回列表
    # 其中，文本的格式是：一条数据后跟两个回车，下面的代码就是使用两个连续的回车来分割数据的
    f = open(Route, 'r', encoding='utf-8')
    s = f.read()
    f.close()
    TrainList = s.split(splitchar)
    for i in range(0, len(TrainList), 1):
        TrainList[i] = str(TrainList[i]).replace('。', '，')
    return TrainList


def modifyTXT_Made(InputRoute, SaveRoute):
    dicc = {"original": [], "content": []}
    TrainList = readText(InputRoute, '\n')
    for sentence_id in tqdm.tqdm(range(0, len(TrainList), 1)):
        if len(TrainList[sentence_id]) == 0:
            continue
        # print("当前句：{}".format(TrainList[sentence_id]))
        dicc['original'].append(TrainList[sentence_id])
        try:
            cut = WordCut(TrainList[sentence_id])
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
            TrainList[sentence_id] = ""
            for kk in cut:
                TrainList[sentence_id] += kk
            # print("改后句：{}".format(TrainList[sentence_id]))
            dicc['content'].append(TrainList[sentence_id])
        except Exception as e:
            print(e)
            raise ImportError
    pd.DataFrame(dicc).to_csv(SaveRoute if ".csv" in SaveRoute else SaveRoute + ".csv")


if __name__ == '__main__':
    # NW.awakeLSTMtoTrain()
    modifyTXT_Made("/ChatGLM2-6B/workspace/qingbao.txt", "/ChatGLM2-6B/workspace/qingbao(CWordAttack).csv")