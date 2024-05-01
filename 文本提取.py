import os
import json
import re

folderpath='文本\\'
filenames=os.listdir(folderpath)
namelist=['アル', 'アナウンス', '女性の声', '窓際の女性', 'カズミ', 'レイコ', 'カイル', 'エレナ', 'アル・レイコ', 'マコト', 'ティーナ', 'ゲーツ', 'グスタフ', 'マルチナ', '男の声', '女の声', 'ツナギの女', 'シルビア', '放送の声', '女の子', '女の人', 'クリス', 'シェリル', '男の人', 'オバサン', 'ティーナの声', '少女', '編集長',"通りがかりの男",'見知らぬ女性']

def filter(text):
    if len(text)<2:
        return False
    if re.match('[a-zA-Z0-9 ]',text[0]):
        return False
    return True

outjsonfile=open('文本.json','w',encoding='utf8')
out=[]
id=1
for filename in filenames:
    #out=[]
    file=open(folderpath+filename,'r',encoding='utf8')
    #outjsonfile=open(folderpath.replace('文本','文本json')+filename.replace('txt','json'),'w',encoding='utf8')
    
    dic={}
    dic['id']=id

    for line in file:
        line=re.sub('<.*>','',line)
        line=line.replace('\n','')

        if filter(line):
            if line in namelist:
                dic['name']=line
                continue
            dic['message']=line

            if re.match('^[。、？‥]*$', line):
                dic={}
                dic['id']=id
                continue

            out.append(dic)
            id+=1
            dic={}
            dic['id']=id
    
json.dump(out,outjsonfile,ensure_ascii=False,indent=4)
