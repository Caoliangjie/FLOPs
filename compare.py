import cv2
import numpy as np
import os
import matplotlib.pyplot as plt
#fps = 25 #视频帧率
#fourcc = cv2.VideoWriter_fourcc(*'XVID')
#videoWriter = cv2.VideoWriter('compose.avi', fourcc, fps, (224,224))
alpha = 0.5##0.5这个alpha通道得到的效果是最好的。
beta = 1-alpha
gamma = 0
path='resize'
x=os.walk(path)
image = []
count=0
for root,dirs,filename in x:
    #image=plt.imread(filename)##用matplotlib读取的时候就是RGB的
    print(filename)
for s in filename:
    image.append(plt.imread(path+'/'+s))
#image=cv2.cvtColor(image,cv2.COLOR_BGR2RGB)##这说明opencv读取的时候是把通道读成了BGR格式
# image = cv2.resize(image,(224,224))
image2 = plt.imread("mb.jpg")
image2 = cv2.resize(image2,(224,224))
#image2 = cv2.cvtColor(image2,cv2.COLOR_BGR2GRAY)
#image2 = cv2.merge((image2,image2,image2))
#plt.imshow(image2)
#plt.show()
#image2 = cv2.flip(image2,1,dst=None)##发现something的都会翻转，翻转回原始位置,ucf101则不会(已证实是错误的）
for s in image:
    s = cv2.resize(s,(224,224))
    img = cv2.addWeighted(s, alpha, image2, beta, gamma)
    count+=1
    img2 = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)##添加新功能，可以直接打印出组合的视频出来
    #videoWriter.write(img2)
    plt.imsave('compose/5_compose_{}_mbma.jpg'.format(count),img)
