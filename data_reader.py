import pandas as pd
import config
import re
import jieba

def parse(path):
    data = pd.read_csv(path, encoding='utf-8')
    columns = data.columns.tolist()
    src = [seg(remove(str(item))) for column in ['Question', 'Dialogue'] for item in data[column]]
    if 'Report' in columns:
        tgt = [seg(remove(str(item))) for item in data['Report']]
    else:
        tgt = []
    return src, tgt

def remove(string):
    pat = r'[^0-9a-zA-Z\u4e00-\u9fa5]'
    return re.sub(pat, '', string)

def seg(string):
    return '|'.join(jieba.cut(string, cut_all=False))

def save_data(train_path, test_path, train_seg_x_path, train_seg_y_path, test_seg_path):
    train_x, train_y = parse(train_path)
    test_x, _ = parse(test_path)
    with open(train_seg_x_path, mode='w', encoding='utf-8') as f1:
        for each in train_x[:-1]:
            f1.write(each+'\n')
        f1.write(train_x[-1])
    with open(train_seg_y_path, mode='w', encoding='utf-8') as f2:
        for each in train_y[:-1]:
            f2.write(each+'\n')
        f2.write(train_y[-1])
    with open(test_seg_path, mode='w', encoding='utf-8') as f3:
        for each in test_x[:-1]:
            f3.write(each+'\n')
        f3.write(test_x[-1])

if __name__=='__main__':
    train_path = config.train_path
    test_path = config.test_path
    train_seg_x_path = config.train_seg_x_path
    train_seg_y_path = config.train_seg_y_path
    test_seg_path = config.test_seg_path
    save_data(train_path, test_path, train_seg_x_path, train_seg_y_path, test_seg_path)
