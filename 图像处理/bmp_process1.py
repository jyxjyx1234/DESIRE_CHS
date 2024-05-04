import os
import json
import re
from PIL import Image

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

def touming(x1,y1,x2,y2,img : Image):
    for i in range(x1, x2):
        for j in range(y1, y2):
            img.putpixel((i,j), (0, 0, 0, 0))
    return img
    
def replace_rect(src_path, replacement_path, output_path,text):
    # 打开源文件和替换文件
    src_img = Image.open(src_path)
    replacement_img = Image.open(replacement_path)
    # 读取矩形部分的内容
    rect = src_img.crop((71, 0, 326, 64))
    
    # 将矩形部分替换为替换文件的内容
    if text!='':
        src_img.paste(replacement_img.crop((71, 0, 326, 64)), (71, 0, 326, 64))

    # 加入文字
        from PIL import ImageDraw, ImageFont
        draw = ImageDraw.Draw(src_img)
        font = ImageFont.truetype("C:\Windows\Fonts\msyhbd.ttc", 30)  # 使用合适的字体文件路径
        draw.text((77, 8), text , font=font, fill=(254,254,254))
    src_img=src_img.convert('RGBA')
    src_img=touming(321,0,352,64,src_img)
    src_img=touming(0,0,704,3,src_img)
    src_img=touming(0,61,704,64,src_img)
    src_img=touming(691,0,704,64,src_img)
    src_img=touming(77,58,326,64,src_img)
    src_img=touming(445,58,704,64,src_img)
    src_img=touming(444,59,446,64,src_img)
    src_img=touming(443,58,446,64,src_img)
    src_img=src_img.transpose(Image.Transpose.FLIP_TOP_BOTTOM)
    src_img.save(output_path,format='bmp')

# 调用函数
with open('图像处理\\transtext.json','r',encoding='utf8') as t:
    transtext=json.load(t)

filenames=listdir('sysgrp_bmp1','bmp')
for file in filenames:
    if file.replace('.bmp','') not in transtext:
        continue
    text=transtext[file.replace('.bmp','')]
    replace_rect("sysgrp_bmp1\\"+file, "sysgrp_bmp_origin\\background_1.bmp", "sysgrp_bmpout\\"+file, text)
