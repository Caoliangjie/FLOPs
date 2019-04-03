fi = 'val.txt'
with open(fi,'r') as f:
     f.readline()
     for row in f:
         if row[len(row)-2]!='4':
            print(row)
