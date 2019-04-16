import os
import csv
f = 'lack_train_400'
#fi = 'lack_val_400'
x = os.walk(f)
#x2 = os.walk(fi)
i = 0
with open('train_400.txt','w',newline='') as f1: 
 #with open('val_400_1.txt','w',newline='') as f2:
  #writer = csv.writer(f1)
  #writer1 = csv.writer(f2)
  for root,path,filename in x:
    for s in filename:
         f1.write(s[:11]+'\n') 
         #writer.writerow([s[:11]])    
  #for root,path,filename in x2:
   # for s in filename:
    #     f2.write(s[:10]+'\n')
         #writer.writerow([s[:10]]) 
