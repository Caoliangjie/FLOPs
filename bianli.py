import os
f = '20bn-something-something-v2'
x = os.walk(f)
i = 0
for root,path,filename in x:
    for s in filename:
        if '.webm' in s:
            i +=1
            print(s)
print(i)
