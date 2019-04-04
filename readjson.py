import json
import csv
fi = 'something_v2_01.json'
fi1 = 'something-something-v2-train.csv'
fi2 = 'something-something-v2-validation.csv'
fi3 = 'something-something-v2-test.csv'
i=0
with open(fi,'r') as load_f:
 with open(fi1,'r') as load_f1:
  with open(fi2,'r') as load_f2:
   with open(fi3,'r') as load_f3:
    #with open(fi1,'w',newline='') as write_f:
      load_dict = json.load(load_f)
      #for k,v in load_dict.items():
      #print(load_dict['database'])
      reader = list(csv.reader(load_f1))
      reader1 = list(csv.reader(load_f2))
      reader2 = list(csv.reader(load_f3))
      for k,v in load_dict['database'].items():
          i +=1
          if v['subset'] == 'training':
             if k in str(reader):
               if v['annotations']['label'] in str(reader):
                print('train_pass')
          elif v['subset'] == 'validation':
             if k in str(reader1):
               if v['annotations']['label'] in str(reader1):
                print('validation_pass')                 
          elif v['subset'] == 'testing':
             if k in reader2:
               if v['annotations']['label'] in str(reader2):
                print('testing_pass')  
print(i)
     # writer = csv.writer(write_f,delimiter=';')
      #for k in load_dict:
          #x = k['template'].replace('[','')
          #y = x.replace(']','')   
          #print(y)       
       #   writer.writerow([k['id']])
          #writer.writerow([k])
