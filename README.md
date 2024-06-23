 * @Author: lichenghui 837115887@qq.com
 * @Date: 2024-06-23 14:19:40
 * @LastEditors: lichenghui 837115887@qq.com
 * @LastEditTime: 2024-06-23 15:13:27
 * @FilePath: /chli/helmat_detectioin/Safety_hat_detection/README.md
 * @Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
-->
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
运行xml2txt.py将数据集整理成yolo格式
```bash
python xml2txt.py
```
运行split_data.py对数据集进行划分
```bash
python split_data.py
```
### 3) Library
下载所需要的python库，在requirements.txt所在的文件夹中打开终端，运行以下代码。
```bash
pip install -r requirements.txt
```
## 项目代码结构
```bash
helmet_detection
├──dataset					#数据集
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
├── models			#所用模型合集
│   ├── yolov8n.py		#YOLOv8模型
├── utils	 #数据清理和转换
│   ├── data_clean.txt			#数据清理
│   └── split_data.py         #划分数据集为训练集、测试集和验证集
│   └── xml2txt.py	           #把xml格式转换为txt格式
├── run			#训练结构分析
├── test				#测试环境可行性和分析结果
│   ├── test_cuda.py					#测试cuda可行
│   └── analytics.py                 #结果可视化
├── main.py			#开始
├── requirements.txt		#所需库
└── README.md		#实现步骤说明
```
## Training
```bash
python main.py
```
## Evaluation
see run/detect for mere detail
