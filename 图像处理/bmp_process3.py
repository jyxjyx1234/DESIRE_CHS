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

def replace_rect(src_path, replacement_path, output_path,text):
    # 打开源文件和替换文件
    src_img = Image.open(src_path)
    replacement_img = Image.open(replacement_path)
    # 读取矩形部分的内容
    rect = src_img.crop((34, 17, 319, 50))
    replacement_img = replacement_img.crop((34, 17, 319, 50))

    # 将矩形部分替换为替换文件的内容
    src_img.paste(replacement_img, (34, 17, 319, 50))

    # 加入文字
    from PIL import ImageDraw, ImageFont
    draw = ImageDraw.Draw(src_img)
    try:
        size=28
        font = ImageFont.truetype("C:\Windows\Fonts\msyh.ttc", size)  # 使用合适的字体文件路径
        w=font.getlength(text)
        if w>300:
            raise RuntimeError
    except RuntimeError:
        size-=1

    draw.text((int(173-0.5*w), 12), text , font=font, fill="white")
    src_img=src_img.transpose(Image.Transpose.FLIP_TOP_BOTTOM)

    # 保存输出文件
    src_img.save(output_path)

# 调用函数
with open('图像处理\\transtext.json','r',encoding='utf8') as t:
    transtext=json.load(t)

filenames=listdir('sysgrp_bmp3','bmp')
for file in filenames:
    if file.replace('.bmp','') not in transtext:
        continue
    if transtext[file.replace('.bmp','')]=='':
        continue
    text=transtext[file.replace('.bmp','')]
    replace_rect("sysgrp_bmp3\\"+file, "sysgrp_bmp_origin\\background_3.bmp", "sysgrp_bmpout\\"+file, text)
