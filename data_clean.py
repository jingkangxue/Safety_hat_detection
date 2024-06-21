
import os

# 定义VOC文件存放的路径
xml_dir = 'HelmetDetection\\HelmetDetection\helmet\\train\\annotations'
img_dir = 'HelmetDetection\\HelmetDetection\helmet\\train\\images'
train_txt_path = 'HelmetDetection\\HelmetDetection\helmet\\train\\train.txt'
valid_txt_path = 'HelmetDetection\\HelmetDetection\helmet\\train\\valid.txt'
label_list_txt_path = 'HelmetDetection\\HelmetDetection\helmet\\train\\label_list.txt'
# 读取标注文件
xml_files = os.listdir(xml_dir)
print('数据集含有 ' + str(len(xml_files)) + '张图片')
# 训练集和测试集占比
radio = 0.8
trainset = xml_files[:int(radio*len(xml_files))]
validset = xml_files[int(radio*len(xml_files)):]

with open(train_txt_path, 'w') as f:
    for i in trainset:
        img_path = './images/'+ i[:-4] + '.png'
        xml_path = './annotations/'+ i 
        text = img_path + ' ' + xml_path + '\n'
        f.write(text)
f.close()
print('生成train.txt完毕...')

with open(valid_txt_path, 'w') as f:
    for i in validset:
        img_path = './images/'+ i[:-4] + '.png'
        xml_path = './annotations/'+ i 
        text = img_path + ' ' + xml_path + '\n'
        f.write(text)
f.close()
print('生成valid.txt完毕...')


labels = ['helmet', 'head']
with open(label_list_txt_path, 'w') as f:
    for label in labels:
        f.write(label+'\n')
f.close()
print('生成label_list.txt完毕...')