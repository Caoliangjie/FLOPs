import sys
f1, f2=None,None
try:
    f1=open("train_400.txt", "r")##之前的视频数量，少的一部分
    m=f1.readlines()
except IOError:
    sys.exit(2)
finally:
    if f1:
        f1.close()
# reead lines from mids2.txt
try:
    f2=open("train_lack.txt", "r")##总共的视频数量，多的一部分。
    n=f2.readlines()
except IOError:
    sys.exit(2)
finally:
    if f2:
        f2.close()
for a in m:
    for b in n:
        if a==b:
            n.remove(b)     
for i in range(len(n)):
 with open("least_train.txt","a") as fe:
    n[i]=n[i].strip()
    fe.write(n[i]+"\n")
    print('n[i]=',n[i])
##train.txt是我们之前少的那部分，butong_train是我们刚生成的包含总共的数据集的txt文件

##还是的用txt查出错，然后在转为csv文件。
