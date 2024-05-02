#将修好的图放在sysgrp_bmp文件夹中(必须以bmp格式），运行此代码，即可将处理好的文件输出到sysgrp_out文件夹中，将其中的文件复制到游戏目录中即可替换图片。

import os
from 译文合并 import listdir

bmp_list=listdir('sysgrp_bmp','bmp')

for i in bmp_list:
    os.system('SysgrpConverter.exe sysgrp_bmp\\'+i)

out_list=listdir('sysgrp_bmp','out')
os.system('del /Q sysgrp_out\\*.*')
for i in out_list:
    os.system('move sysgrp_bmp\\'+i+' sysgrp_out\\')
    os.system('ren sysgrp_out\\'+i+' '+i.replace('.bmp.out',''))