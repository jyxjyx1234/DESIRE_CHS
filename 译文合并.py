import os
import re
import json
from HanziReplacer import *
from 文本提取 import filter

def listdir(path,type):
    files=os.listdir(path)
    ret=[]
    for file in files:
        if '.' not in file:
            if type=='':
                ret.append(file)
            continue

        filetype=file.split('.')
        filetype=filetype[-1]
        if filetype==type:
            ret.append(file)
    return ret

ori_filenames=listdir('文本\\','txt')

yiwen=open('译文.json','r',encoding='utf8')
yiwen=json.load(yiwen)
namelist=open('namelist.json','r',encoding='utf8')
namelist=json.load(namelist)

replacement_dict={}
for dic in yiwen:
    replacement_dict[dic["pre_jp"]]=dic["post_zh_preview"]
for i in namelist:
    replacement_dict[i]=namelist[i]
    

for i in replacement_dict:#生成hanzidic
    tempdict,charlist=GetInvalidChars(replacement_dict[i],tempdict,charlist)
hanzidict,target_chars,source_chars=Createhanzidict(tempdict,charlist)

for filename in ori_filenames:
    file=open('文本\\'+filename,'r',encoding='utf8')
    outfile=open('译文合并\\'+filename,'w',encoding='utf8')
    for line in file:
        content=re.sub('<.*>','',line)
        if filter(content):
            content=content.replace('\n','')
            if content in replacement_dict:
                line=line.replace(content,hanzitihuan(replacement_dict[content],hanzidict))
        outfile.write(line)
    outfile.close()

ChangeUFIConfig(".\\DESIRE_CHS\\uif_config.json",source_chars,target_chars)

trans_filenames=listdir('译文合并\\','txt')
for filename in trans_filenames:
    os.system('ScriptEncoder.exe 译文合并\\'+filename)
    os.system('move 译文合并\\'+filename+'.new '+'DESIRE_CHS\\')
    os.system('ren DESIRE_CHS\\'+filename+'.new '+filename.replace('.txt',''))
