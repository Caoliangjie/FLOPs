import sys
f1, f2=None,None
try:
    f1=open("train.txt", "r")
    m=f1.readlines()
except IOError:
    sys.exit(2)
finally:
    if f1:
        f1.close()
# reead lines from mids2.txt
try:
    f2=open("butong.txt", "r")
    n=f2.readlines()
except IOError:
    sys.exit(2)
finally:
    if f2:
        f2.close()
#filter
for a in m:
    for b in n:
        if a==b:
            n.remove(b)     
for i in range(len(n)):
 with open("diff.txt","a") as fe:
    n[i]=n[i].strip()
    fe.write(n[i]+"\n")
    print('n[i]=',n[i])
#print ('n =', n)
#print " ".join(n)
#for aar in n:
#	with open("lack.txt","a") as fe:
#		fe.write(aar+"\n")
#		print(aar)

