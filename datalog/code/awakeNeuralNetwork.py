import os


def awakeLSTMtoTest():
    os.system('cd ..&&cd ..&&cd text-classification-cnn-rnn&&python run_cnn.py test')
    # 转到地址并运行
    f = open("/Users/andrewlee/Desktop/Projects/LW/text-classification-cnn-rnn/acc.txt", 'r', encoding='utf-8')
    acc = float(f.read())
    # 读取训练得到的准确度
    return acc


def awakeLSTMtoTrain():
    if os.path.exists("/Users/andrewlee/Desktop/Projects/LW/text-classification-cnn-rnn/tensorboard"):
        print("TrainFileExist.")
        os.system("rm -r /Users/andrewlee/Desktop/Projects/LW/text-classification-cnn-rnn/tensorboard")
    os.system('cd ..&&cd ..&&cd text-classification-cnn-rnn&& python run_cnn.py train')
    # 转到地址并运行


if __name__ == '__main__':
    awakeLSTMtoTrain()
    print(awakeLSTMtoTest())
