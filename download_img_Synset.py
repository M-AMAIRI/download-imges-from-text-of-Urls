
#!/usr/bin/env python 

import os
import shutil
import requests

True_Url=0;

fh = open('imagenet.synset.geturls.txt')

x = input("Enter a number ( Number of images to be downloaded ) : ")
path = input("path : ")

for i in range(int(x)) :
    line = fh.readline()
    print(line)
    print("download file "+str(i))


    f = open(path+'/image_'+str(i)+'_.jpg','wb')
    try :
     f.write(requests.get(line).content)
     f.close()
     True_Url=True_Url+1
    except:
     print("sorry url not found ...")
     os.remove('Im_path/image_'+str(i)+'_.jpg')

    if not line:
        break

if(True_Url==0):
 print("download failed ! ")
else :
 print(str(True_Url)+" images downloaded successfully")
 print(str(int(x)-True_Url)+" of urls page not found")


fh.close()
