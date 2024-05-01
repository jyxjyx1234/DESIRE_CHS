#简单粗暴，出现次数多的就很可能是人名
import os
import json
import re

folderpath='文本\\'
filenames=os.listdir(folderpath)
namelist=[]

def filter(text):
    if len(text)<2:
        return False
    if re.match('[a-zA-Z0-9 ]',text[0]):
        return False
    return True

out=[]
dir={}
outjsonfile=open('namelist.json','w',encoding='utf8')
for filename in filenames:
    file=open(folderpath+filename,'r',encoding='utf8')

    for line in file:
        line=re.sub('<.*>','',line)
        line=line.replace('\n','')

        if filter(line):
            if len(line)>10:
                continue
            if "‥" in line:
                continue
            if re.search('[？。、！「屋室舎前]',line):
                continue
            
            if line not in dir:
                dir[line]=1
            else:
                dir[line]=dir[line]+1

for line in dir:
    out.append((dir[line],line))
out.sort(reverse=True)
outt=[]
for i in out:
    outt.append(i[1])
json.dump(outt,outjsonfile,ensure_ascii=False,indent=4)