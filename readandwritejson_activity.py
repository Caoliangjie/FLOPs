import json
import csv
count = 0
fi = 'activity_net.v1-3.min.json'
fi2 = 'lack_activitynet_v1-3.json'
new_dict = {}
n2 = {}
with open(fi,'r') as load_f:
 with open('local.txt','r') as f:
  with open(fi2,'w') as f1:
   f = list(f)##把这个转成list来做比较快
   for i in range(len(f)):
      f[i] = f[i][:-1]
   d1 = json.load(load_f)
   #print(type(d1['database']))
   for k,v in d1.items():
      if k=='taxonomy':
        new_dict.setdefault(k,v)
      if k=='version':
        new_dict.setdefault(k,v)
      if k=='database':
        for k1,v1 in d1['database'].items():
          if k1 not in f:
            count +=1
            n2.setdefault(k1,v1)
        new_dict.setdefault(k,n2)
   json.dump(new_dict,f1)
print(count)
for k,v in new_dict.items():
   print(k)
##json文件读出不同的并且重新写到json文件中
