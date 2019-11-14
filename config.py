import os

#data path
data_path = os.path.abspath('./data')

train_path = os.path.join(data_path, 'AutoMaster_TrainSet.csv')
test_path = os.path.join(data_path, 'AutoMaster_TestSet.csv')

train_seg_x_path = os.path.join(data_path, 'train_seg_x.txt')
train_seg_y_path = os.path.join(data_path, 'train_seg_y.txt')

test_seg_path = os.path.join(data_path, 'test_seg.txt')