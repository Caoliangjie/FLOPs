import codecs
import matplotlib.pyplot as plt
import matplotlib
import numpy as np
from decimal import *
f = codecs.open('train.log', mode='r', encoding='utf-8') 
f1 = codecs.open('val.log', mode='r', encoding='utf-8') 
f2 = codecs.open('baseline-train.log', mode='r', encoding='utf-8') 
f3 = codecs.open('baseline-val.log', mode='r', encoding='utf-8')  # 打开文件，以‘utf-8’编码读取
epoch2=[]
i=1
for i in range(35):
    epoch2.append(i)
line = f.readline()   # 以行的形式进行读取文件
list1 = []
while line:
    a = line.split()
    print(a)
    b = str(a[2:3])   # 这是选取需要读取的位数
    b = b[2:-2]
    list1.append((1-float(b))*100)  # 将其添加在列表之中,并且转换为float类型
    line = f.readline()
f.close()
line2 = f1.readline() 
list2 = []
while line2:
    a = line2.split()
    b = str(a[2:3])  
    b = b[2:-2]
    list2.append((1-float(b))*100) 
    line2 = f1.readline()
f1.close()
line3 = f2.readline()  
list3 = []
while line3:
    a = line3.split()
    b = str(a[2:3]) 
    b = b[2:-2]
    list3.append((1-float(b))*100)  
    line3 = f2.readline()
f2.close()
line4 = f3.readline()   
list4 = []
while line4:
    a = line4.split()
    b = str(a[2:3])   
    b = b[2:-2]
    list4.append((1-float(b))*100)  
    line4 = f3.readline()
f2.close()
#print(list2)
#print(list3)
#print(list4)
matplotlib.rcParams['xtick.direction'] = 'in'
matplotlib.rcParams['ytick.direction'] = 'in'  
plt.xlim(1,35)
plt.ylim(0,15)
plt.plot(epoch2,list1,'r',linewidth=2)
plt.plot(epoch2,list2,'g',linewidth=2)
plt.plot(epoch2,list3,'b',linewidth=1)
plt.plot(epoch2,list4,'c',linewidth=1)
#plt.title('Error rate')#标题
plt.xlabel('epoch(n)')
plt.ylabel('err(%)')
plt.legend(('MBMA(train)','MBMA(val)','baseline(train)','baseline(val)'),loc='upper right')
plt.savefig('err.jpg',dpi=300)
plt.close()
