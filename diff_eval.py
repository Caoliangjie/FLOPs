import csv
file1 = 'lack.txt'
file2 = 'train.txt'
file3 = 'chongfu.txt'
with open(file1,'r') as f1:
 with open(file2,'r') as f2:
  with open(file3,'w') as f3:
   m=f1.readlines()
   n=f2.readlines()
   for l1 in m:
    if l1 in n:
      print('重复')
    else:
      f3.write(l1)
