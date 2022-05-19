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
    return RandomList(A+B)


def OutPut(ListIn_, Route, Mode):  # 将ListIn中的数据输出到Route中，文件模式为Mode，一个数据一个换行
    f = open(Route, mode=Mode, encoding='utf-8')
    ListIn = ListIn_.copy()
    while len(ListIn):
        loc = random.randint(0, len(ListIn) - 1)
        f.write(ListIn[loc] + '\n')
        ListIn.pop(loc)