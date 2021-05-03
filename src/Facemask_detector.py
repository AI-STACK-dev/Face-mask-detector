# USAGE
# python detect_mask_video.py
#Created by S. Jahnavi Prasad
#(https://github.com/jahnavi-prasad)
# import the necessary packages
import numpy as np 
import pandas as pd
from bs4 import BeautifulSoup
import torchvision
from torchvision import transforms, datasets, models
import torch
from PIL import Image
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from torchvision.models.detection.faster_rcnn import FastRCNNPredictor
import os
from imutils.video import VideoStream
import argparse
import imutils
import time
import cv2

def get_model_instance_segmentation(num_classes):
    # load an instance segmentation model pre-trained pre-trained on COCO
    model = torchvision.models.detection.fasterrcnn_resnet50_fpn(pretrained=True)
    # get number of input features for the classifier
    in_features = model.roi_heads.box_predictor.cls_score.in_features
    # replace the pre-trained head with a new one
    model.roi_heads.box_predictor = FastRCNNPredictor(in_features, num_classes+1)
    return model

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-m", "--model", type=str,
    default= "C:/Users/dorim/Downloads/",
    help="path to trained face mask detector model")
ap.add_argument("-c", "--confidence", type=float, default=0.5,
    help="minimum probability to filter weak detections")
args = vars(ap.parse_args())

tensor_transform = transforms.Compose([
    transforms.ToTensor()
])
# load our serialized face detector model from disk
print("[INFO] loading face detector model...")
model = get_model_instance_segmentation(3)
resume = os.path.sep.join([args["model"], "fastrcnn_res50_epoch25_lr002.pth"])
checkpoint = torch.load(resume)
model.load_state_dict(checkpoint['state_dict'])
device = torch.device('cuda') if torch.cuda.is_available() else torch.device('cpu')
model = model.to(device)


# load the face mask detector model from disk


# initialize the video stream and allow the camera sensor to warm up
print("[INFO] starting video stream...")
vs = VideoStream(src=0).start()
time.sleep(2.0)

# loop over the frames from the video stream
while True:
    frame = vs.read()
    frame = imutils.resize(frame, width=600)
    model.eval()
    img = tensor_transform(frame)
    img = img.to(device)

    preds = model(list(img[None, :, :]))

    if len(preds[0]["boxes"])==0:
        pass
    else:
        mask = preds[0]["scores"] > 0.5

        for (box, labels) in zip(preds[0]["boxes"][mask], preds[0]["labels"][mask]):
            xmin, ymin, xmax, ymax = box
            xmin = int(xmin)
            ymin = int(ymin)
            xmax = int(xmax)
            ymax = int(ymax)

            if labels == 1:
                label = 'with_mask'
                color = (0, 255, 0)
            elif labels == 2:
                label = 'without_mask'
                color = (0, 0, 255)
            elif labels == 3:
                label = "mask_weared_incorrect"
                color = (0, 255, 255)
        
            
            cv2.putText(frame, label, (xmin, ymin - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.45, color, 2)
            cv2.rectangle(frame, (xmin, ymin), (xmax, ymax), color, 2)

   
    cv2.imshow("Frame", frame)
   # torch.cuda.empty()
    key = cv2.waitKey(1) & 0xFF

   # if the `q` key was pressed, break from the loop
    if key == ord("q"):
        break

# do a bit of cleanup
cv2.destroyAllWindows()
vs.stop()