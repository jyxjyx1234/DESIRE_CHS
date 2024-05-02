#将修好的图放在sysgrp_bmp文件夹中(必须以bmp格式），运行此代码，即可将处理好的文件输出到sysgrp_out文件夹中，将其中的文件复制到游戏目录中即可替换图片。

import os
from 译文合并 import listdir

bmp_path='sysgrp_bmpout\\'
out_path='sysgrp_out\\'

bmp_list=listdir(bmp_path,'bmp')

for i in bmp_list:
    os.system('SysgrpConverter.exe '+ bmp_path + i)

out_list=listdir(bmp_path,'out')
os.system('del /Q '+out_path+'\\*.*')
os.system('move '+bmp_path+'*.out'+' sysgrp_out\\')
for i in out_list:
    os.system('ren '+out_path+i+' '+i.replace('.bmp.out',''))