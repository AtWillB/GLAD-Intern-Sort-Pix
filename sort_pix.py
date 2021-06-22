# -*- coding: utf-8 -*-
"""internship_code.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1lVEl9T88wmnhx4XgYRzxtFV4MUqmqUds
"""

import os
import shutil
import collections

path = "C:/Users/wbyrne/Desktop/rawdata - local/"


# ONlY EDIT THINGS IN BETWEEN THESE LINES ------------------------------------
#Example: x383    
pic_path = "x383"

#BEFORE RUNNIGN THIS SCRIPT, CHECK FOR A SENTINAL PREFIX IN THE CHOSE FOLDER
#Example: IS_NKJ_        Must have _ at the end
sent_prefix = "IS_NKJ_"

#ONLY EDIT THINGS IN BETWEEN THESE LINES ------------------------------------

path += pic_path +"/"
names = os.listdir(path)
newNames = list()
#print(names)


#print(path)




#names.remove(".config")
#names.remove("sample_data")
#names.remove(".ipynb_checkpoints")
for name in names:
  if name.find("IP") != -1:
    newName = name.replace("IP_", "")
    index = names.index(name)
    newNames.insert(index,newName)
  if name.find("IS") != -1:
    newName = name.replace(sent_prefix, "")
    index = names.index(name)
    newNames.insert(index,newName)

newNames = sorted(newNames)
#print(newNames)
for origi_name in names:
  for new_name in newNames:
    if origi_name.find(new_name) != -1 and origi_name.find("IP_") != -1:
      prefix_new_name = "IP_"+new_name
      newNames.insert(newNames.index(new_name), prefix_new_name)
      newNames.remove(new_name)
    if origi_name.find(new_name) != -1 and origi_name.find(sent_prefix) != -1:
      prefix_new_name = sent_prefix+new_name
      newNames.insert(newNames.index(new_name), prefix_new_name)
      newNames.remove(new_name)

if not os.path.exists(path+"sorted/"):
  os.makedirs(path+"sorted/")

#print(newNames)

counter = 1

file_dict = collections.defaultdict()

for file_name in newNames:
  if newNames.index(file_name) == 0:
    file_dict["group"+str(counter)] = []
    file_dict["group"+str(counter)].append(file_name)
  elif file_name.find("IS") != -1 and newNames[newNames.index(file_name)-1].find("IS") != -1:
    file_dict["group"+str(counter)].append(file_name)
  elif file_name.find("IP") != -1 and newNames[newNames.index(file_name)-1].find("IP") != -1:
    file_dict["group"+str(counter)].append(file_name)
  
  elif file_name[:2] != newNames[newNames.index(file_name)-1][:2]:
    counter += 1
    file_dict["group"+str(counter)] = []
    file_dict["group"+str(counter)].append(file_name)

#print(file_dict)


for key in file_dict.keys():
  os.makedirs(path+"sorted/"+key)
  for file in file_dict[key]:
    shutil.copy(path+file, path+"sorted/"+key+"/"+file)