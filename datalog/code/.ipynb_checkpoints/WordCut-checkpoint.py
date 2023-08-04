import jieba
import time
import tqdm


def WordCut(TextIn: str):
    return jieba.lcut(TextIn, cut_all=False)


if __name__ == '__main__':
    x = WordCut("2021年HanLPv2.1为生产环境带来次世代最先进的多语种NLP技术。阿婆主来到北京立方庭参观自然语义科技公司。")
    print(x)