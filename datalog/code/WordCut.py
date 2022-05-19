from hanlp_restful import HanLPClient
import time
import tqdm
HanLP = HanLPClient('https://www.hanlp.com/api', auth=None, language='zh')  # auth不填则匿名，zh中文，mul多语种


def WordCut(TextIn: str):
    try:
        k = HanLP.parse(TextIn)["tok/fine"]
        print(k)
        return k
    except Exception as e:
        print("等待更新权限15s...")
        for T in tqdm.tqdm(range(0, 20, 1)):
            time.sleep(1)
        k = HanLP.parse(TextIn)["tok/fine"]
        print(k)
        return k


if __name__ == '__main__':
    x = WordCut("2021年HanLPv2.1为生产环境带来次世代最先进的多语种NLP技术。阿婆主来到北京立方庭参观自然语义科技公司。")
    print(x)