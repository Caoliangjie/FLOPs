import csv
filename = 'train_lack.csv'
file2 = 'wrong_train1.txt'
with open(filename,'r') as f:
   with open(file2,'w') as f2:
        reader = csv.reader(f)
        for row in reader:
            f2.write(row[0]+'\n')

