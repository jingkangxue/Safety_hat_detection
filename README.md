# Safety_hat_detection
目标检测任务，能够识别所给出图像或视频中的人是否正确佩戴安全帽。

## Installation
### 1) Code
```bash
git clone https://github.com/jingkangxue/Safety_hat_detection
```
### 2) Data
数据集下载https://aistudio.baidu.com/datasetdetail/91022
将HelmetDetection.zip解压缩到.\Dataset目录下面，并将其整理成标准的VOC格式。
```bash
python data_clean.py
```
## 项目代码结构
```bash
helmet_detection
├──Dataset  #数据集
│   ├── test  #测试集
│   │   ├── annotations  #标识文件夹
│   │   │   ├── xxx1.xml	
│   │   │   │    ···
│   │   ├── images  #图像文件夹
│   │   │   ├── xxx1.jpg
│   │   │   │    ···
│   ├── train  #训练集
│   │   ├── annotations  #标识文件夹
│   │   │   ├── xxx1.xml	
│   │   │   │    ···
│   │   ├── images  #图像文件夹
│   │   │   ├── xxx1.jpg
│   │   │   │    ···
├── label_list.txt  #类别
├── test_name.txt  #测试集图像名称
├── train.txt  #训练数据集文件列表
└── valid.txt  #测试数据集文件列表
├── models  #所用模型合集
│   ├── yolov8.py  #YOLOv8模型
│   └── utils.py  #其他插件
├── train.py  #训练模型
├── eval.py  #测试模型
├── inference.py  #推理模型
├── requirements.txt  #所需库
└── README.md  #实现步骤说明
```
## Training

## Evaluation
