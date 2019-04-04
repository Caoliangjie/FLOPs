import json
import csv
fi = 'something-something-v2-validation.json'
fi1 = 'something-something-v2-validation.csv'
with open(fi,'r') as load_f:
    with open(fi1,'w',newline='') as write_f:
      load_dict = json.load(load_f)
      writer = csv.writer(write_f,delimiter=';')
      for k in load_dict:
          x = k['template'].replace('[','')
          y = x.replace(']','')   
          print(y)       
          l = [k['id'],y]
          writer.writerow(l)
          #writer.writerow([k])
