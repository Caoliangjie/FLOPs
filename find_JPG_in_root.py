import os
import argparse
import subprocess
import shutil
parser = argparse.ArgumentParser(description='find jpg files')
parser.add_argument('data', metavar='DIR',
                    help='path to root')
args = parser.parse_args()
x = os.walk(args.data)
if not os.path.exists('jiafang'):
    os.mkdir('jiafang')
for root,dirs,filename in x:
   for i in filename:
       if '.txt' in i:
           name = i.split('.')[0]       
       if not os.path.exists('jiafang/zhongzhuan/'+name):
             os.mkdir('jiafang/zhongzhuan/'+name)
       if 'JPG' in i:
         path = 'jiafang/zhongzhuan/'+name
         shutil.copy(root+'/'+i,path)
