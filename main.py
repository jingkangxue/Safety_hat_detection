'''
Author: lichenghui 837115887@qq.com
Date: 2024-06-23 14:53:54
LastEditors: lichenghui 837115887@qq.com
LastEditTime: 2024-06-23 15:07:10
FilePath: /chli/helmat_detectioin/Safety_hat_detection/main.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
from ultralytics import YOLO

# Load a model
model = YOLO("yolov8n.yaml")  # build a new model from scratch
model = YOLO("yolov8n.pt")  # load a pretrained model (recommended for training)

# Use the model
model.train(data="/home/chli/yolov8-helmat_detectioin/ultralytics/dataset/helmet.yaml", epochs=150, batch=6, save_period=-1 ) # train the model
metrics = model.val()  # evaluate model performance on the validation set
# results = model("https://ultralytics.com/images/bus.jpg")  # predict on an image
path = model.export(format="onnx")  # export the model to ONNX format