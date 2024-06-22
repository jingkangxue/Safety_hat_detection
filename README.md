# Safety_hat_detection
目标检测任务，能够识别所给出图像或视频中的人是否正确佩戴安全帽。

## Installation
### 1) Code
在所创建的项目文件夹中打开运行终端，运行以下代码下载文件。
```bash
git clone https://github.com/jingkangxue/Safety_hat_detection
```
### 2) Data
数据集下载https://aistudio.baidu.com/datasetdetail/91022
将HelmetDetection.zip解压缩到.dataset目录下面，并将其整理成标准的VOC格式。
```bash
python data_clean.py
```
### 3) Library
下载所需要的python库，在requirements.txt所在的文件夹中打开终端，运行以下代码。
```bash
pip install -r requirements.txt
```
## 项目代码结构
```bash
helmet_detection
├── dataset  #数据集
│   ├── images			#图片
│   │   ├── train			#训练集
│   │   │   ├── xxx1.jpg	
│   │   │   │    ···
│   │   ├── val			#验证集
│   │   │   ├── xxx1.jpg
│   │   │   │    ···
│   ├── labels				#坐标标识
│   │   ├── train			#训练集
│   │   │   ├── xxx1.txt	
│   │   │   │    ···
│   │   ├── val			#验证集
│   │   │   ├── xxx1.txt
│   │   │   │    ···
│   │   ├── train.cache	#训练集图像转为txt
│   │   ├── val.cache		#验证集图像转为txt
│   ├── label_list.txt		#类别
│   ├── test_name.txt	#测试集图像名称
│   ├── train.txt			#训练数据集文件列表
│   └── valid.txt			#测试数据集文件列表
├── models  #所用模型合集
│   ├── yolov8.py  #YOLOv8程序
│   ├── yolov8.yaml		#YOLOv8模型
│   └── utils.py  #其他插件
├── data_clean.py  #数据清理
├── train.py  #训练模型
├── test.py  #测试模型
├── inference.py  #推理模型
├── requirements.txt  #所需库
└── README.md  #实现步骤说明
```
## Training

## Evaluation
