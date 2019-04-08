import csv
with open('least_train1.csv','w') as f1:
  with open('least_train.txt','r') as f2:
     writer = csv.writer(f1)
     for i in f2:
         writer.writerow([i[:-2]])##这里因为是writerrow写的是list类型，所以说直接用[]把起括起来作为list即可。
