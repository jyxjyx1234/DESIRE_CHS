# DESIRE remaster A ver.  Sakura AI机翻汉化补丁

本补丁是[DESIRE remaster A ver.](https://el-dia.net/desire/desire-a/desire-a.html)的AI机翻汉化补丁，使用[Sakura](https://github.com/SakuraLLM/Sakura-13B-Galgame) v0.10进行翻译。

未进行校对。

本补丁仅供交流学习AI翻译使用，请在购买[游戏本体](https://el-dia.net/desire/desire-a/desire-a.html)的基础上使用本补丁。

本补丁发布于[https://github.com/jyxjyx1234/DESIRE_CHS](https://github.com/jyxjyx1234/DESIRE_CHS)

查看本人制作的其他机翻补丁：[https://github.com/jyxjyx1234?tab=repositories](https://github.com/jyxjyx1234?tab=repositories)

### **使用说明**

将补丁文件夹中的所有文件复制到游戏目录即可。（本人技术不行，所以有一大堆小文件）

本游戏需要使用[Locale-Emulator](https://github.com/xupefei/Locale-Emulator)转区运行！！！

点击修改此程序的配置：

![1714551362791](image/README/1714551362791.png)

按照下图进行修改：（勾选上管理员权限、伪造语言相关注册表键值、伪造系统UI语言）

![1714551416307](image/README/1714551416307.png)

### 重新打包

如需自行修改译文，请下载本仓库中的内容，在 `译文.json`中的 `"post_zh_preview"`中修改译文。运行译文合并.py即可重新打包，在DESIRE_CHS中可以找到新的文件，替换原本的汉化补丁文件即可。

### 游戏信息

摘自[Getchu](https://www.getchu.com/soft.phtml?id=970517)

|  ブランド： | [Eｌ Dia](http://eve.el-dia.net/ "このブランドの公式サイトを開く")[（このブランドの作品一覧）](https://www.getchu.com/php/search.phtml?search_brand_id=81516) |
| ----------: | ---------------------------------------------------------------------------------------------------------------------------------------------------- |
|      定価： | ￥7,800 (税込￥8,580)                                                                                                                                |
|    発売日： | [2017/12/22](https://www.getchu.com/php/search.phtml?start_date=2017/12/22&end_date=2017/12/22&genre=pc_soft "同じ発売日の同ジャンル商品を開く")           |
|  メディア： | DVD-ROM                                                                                                                                              |
|  ジャンル： | ADV                                                                                                                                                  |
| JANコード： | 4580264785081                                                                                                                                        |

游戏信息\本体购买：[https://www.getchu.com/soft.phtml?id=970517](https://www.getchu.com/soft.phtml?id=970517)

### 致谢

本补丁使用了以下开源项目：

* [BGIKit](https://github.com/xupefei/BGIKit)  : 对BGI引擎的脚本进行编、解码
* [Sakura-13B-Galgame](https://github.com/SakuraLLM/Sakura-13B-Galgame) : 适配轻小说/Galgame的日中翻译大模型
* [UniversalInjectorFramework](https://github.com/AtomCrafty/UniversalInjectorFramework)：对汉化后的文本进行修正以正常显示
* [GalTransl](https://github.com/xd2333/GalTransl) ：自动化翻译工具
