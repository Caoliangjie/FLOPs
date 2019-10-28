import os
from os.path import join, getsize
#with open 
def getdirsize(dir):
   size = 0L 
   count = 1
   for root, dirs, files in os.walk(dir):
      #print(root)
      size = ([getsize(join(root, name)) for name in files])
      for l in size:
        if l == 0:
         print(root)
         count+=1
         break
   print(count)
   return size
filesize = getdirsize('train/')
#print ('There are %.3f' % (filesize/1024), 'Mbytes in c:\\windows')
