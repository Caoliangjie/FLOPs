import sys
f1, f2=None,None
try:
    f1=open("train.txt", "r")##之前的视频数量，少的一部分
    m=f1.readlines()
except IOError:
    sys.exit(2)
finally:
    if f1:
        f1.close()
# reead lines from mids2.txt
try:
    f2=open("butong_train.txt", "r")##总共的视频数量，多的一部分。
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
 with open("diff_train.txt","a") as fe:
    n[i]=n[i].strip()
    fe.write(n[i]+"\n")
    print('n[i]=',n[i])

