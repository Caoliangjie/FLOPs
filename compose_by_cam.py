def show_cam_on_image(img, mask,name):
	#heatmap = cv2.applyColorMap(np.uint8(255*mask), cv2.COLORMAP_JET)
	heatmap = np.float32(mask) / 255
	cam = heatmap+np.float32(img)
	cam = cam / np.max(cam)
	cv2.imwrite("cam/cam_{}".format(name), np.uint8(255 *cam))
import cv2
import numpy as np
import os
import torch
import matplotlib.pyplot as plt
#fps = 25 #视频帧率
#fourcc = cv2.VideoWriter_fourcc(*'XVID')
#videoWriter = cv2.VideoWriter('compose.avi', fourcc, fps, (224,224))
alpha = 0.5##0.5这个alpha通道得到的效果是最好的。
beta = 1-alpha
gamma = 0
path='resize'
x=os.walk(path)
image = {}
count=0
for root,dirs,filename in x:
    print(filename)
for s in filename:
    image.update({s:cv2.imread(path+'/'+s)})
image2 = cv2.imread("mb.jpg")
image2 = cv2.resize(image2,(224,224))
for k,v in image.items():
    img = np.float32(cv2.resize(v, (224, 224))) / 255
    show_cam_on_image(img,image2,k)
    #img = cv2.addWeighted(s, alpha, image2, beta, gamma)
##添加新功能，可以直接打印出组合的视频出
    #plt.imsave('compose/5_compose_{}_mbma.jpg'.format(count),img)
