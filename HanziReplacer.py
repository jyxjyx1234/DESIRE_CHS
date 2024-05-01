#将sjis中不支持的汉字临时替换为支持的汉字，后续通过[UniversalInjectorFramework]换回
#此方法替换的汉字没有对于字型相似的要求
#还包含了去掉特殊符号（用于匹配）、替换不支持的符号等功能。

'''
使用方法示例（replacement_dict为原文、译文的对应）
for i in replacement_dict:#生成hanzidic
    tempdict,replacelist=GetInvalidChars(replacement_dict[i],tempdict,replacelist)
hanzidic,target_chars,source_chars=Createhanzidic(tempdict,replacelist)
'''

'''
导入到ufi_config:

with open('.\\Marguerite_chs\\uif_config.json','r',encoding='utf8',errors='ignore') as f:
    f=json.load(f)
    f["text_processor"]["rules"][0]["source_chars"]=source_chars
    f["text_processor"]["rules"][0]["target_chars"]=target_chars

with open('.\\Marguerite_chs\\uif_config.json','w',encoding='utf8') as fout:
    json.dump(f,fout,ensure_ascii=False,indent=4)

'''

import re
import json

tempdict={}
charlist='這説為凜們時過対麼瑤還現髪種樣見経頭書実開両動話問間論長進義給関別門覚復難東応風張認伝題処馬詩讓愛師語変爾許結邊歴記読識戰徳術遠総観遙槇連強則該堯場軽親統龜帯業産臉雖軍極類満転歩剣黒離電毎飛済藝衆殺報車終紅視誰絶確達驚羅楽資運華傷評響剛談領権晩興齧顕圖銭楊態霊訳鄰歓錯聯計紀請創陽選緊単詞調編異員僅勢講齡漢証較撃厳竜約蘭質鉤幇陸鉄節細筆値陳熱蘇齣懐媽際級悪須維挙専導備務簡費脳雑亜顧歳構隊魯続劇聞爺敵規陣習線樹階訴設謂囲議謝録層標揺帰劉斉戯隠鉋尋査試飯漸護組勝喬釈討験買貴継団適農嘆衛麗塊宮環齒換倫敗圧聖責絲骭頁険頓孫鳳薬婦韋養裃園紙労鐘揚誤齊劃揮畢負寧鼡銀諸陰呉趙閃納罷遺順輯郷臨堅頂練緩増職鼕館偉獲勁槍滅皷罵輩憶優預擇補貝鮮織積暁売倣載鼈盧諾偸夥純課鼇営黨啓紛擺弾財賞盤牆點豐頗賛圓紹縦賈執慮煩黐嚇鬧魚縁閑黌騎鏡庁誠焼傾韓戸叢緑慣搶項蕭鎮島栄鎬躍顔審軟擁貼礎謀飄訓閉塵窮湯憂蕩麭藍淨辯訪蒼憤撲薩県豈奮奪慶澤輪針監寛鋒緒遅側粛鶏潔儀穏烏躱鄭徹銷滾鳥廃瘋聡測渉姉襲獄毀飲閲検麪麩縮嘗濃麥麕麌賽貨掲協賊厭輸騙喪麁奨橋瑪勧邏鳴鹽減掃損悶詳爛庫朶鹹繞馮呂絵頼鷽碼顫競貧帥閣鷭貫渾鷏暫艦鷆夾飾倆獸壇賢賓鎖蓮牽諍轟匯騰額鑑輝纏喚訊霧遷悩並舗訂闊臘齢帳皺錚紐賦駕購塗鶺顆拡艶痩喩禍艱鶸鷁鷄凱遜鋼臓廟逓鋭鶲撫鴻鶤鵺趨暈嬌擠鑚鈕鍵倶銅縄懸絡貢鵬鵯鶫諷茲違呑煉鶇駆災譜頌擾偽篭輌猟餓膚績虧噴楓汚賭鵙鵐誕暢闡贏攬潤鵤錦懶斬簽鵞歯罰撥鵈擬誘瓊馳臥憲郵桜縫饒賀訝綜欄溝謹厖療邁窪摂渇鈴飽湊糾櫃燭顛嬰嘯犠袙覧貪綿鵆闖鴾鷹謙焔隣窩脇諒幣腸頑騒紋綱鵁斎嗚鴒刪溌擲頻驃滬鵄鶯亀贈侖頚鴪聳襯墜綉鴃駛鳫詢釘蘊賜諧鴈鳰鍋鶴詭詐駐賎駁寵厠唖瑩億畳駭漁頬攤鳧縛簾欽軌籌竄鈞鱶潰鱧遼貶軒鱚瞞鴉僂鰾鈎錫鱆嚢飢誼謬賺鱇窺鰰塩鰡竪獅脹貞輔滄誦繊銘償驕譚瀟墳嘩紗粧荊羨擱兪鰤詫鏈壷貿濫賠鰛釵倉債鰮滲渋凍燦淪採鰄謡謎聶鰊瑣穎鰒鰈膩鑰姪甎漲鰆懲闘餅絋諱訣斃灘販鰌鰉崗鰔揀廂尭鋳譏傘驟鰕轎昿鯰嶺鯱縷殻禿儲娯鯲腫鰺侶蝋棟綻鯔朧鯣偵鯒妬鮑瀾鉱鯑懇鯏煥繆鯆濺鮹鮴黴駱鮨鮠鮗爍膠摯鮖慚綺嵐栲鴛驢駝鮓頽箋剤輿鬪吶隴廬閨閻診擣籃艙頃銜鴨鬨覓駿傭漿貸鬥鬚鬘綢鵝鬆岡髷鈔鞏鴦嘔髱髴悵撹髮髣髢驀鵲巣鴬碩鑿髞蝕體驫驗竇驛釀驅鳩盞騷駲紳錘駮囂馼塁陜饑虜勲蘿軸壟鍛狽誣矯歛繃濱綽讚誅饐禎饂蟻糞洶蔭誇詔絨龍詛餽蕪頤辮餬閥餠餤濁餝餘薫餔篤穢硯釣飃掻撈襪颱颪緞顳顯顋醤幀幟竅顏僑譴簫鵑鈑蝿憫鉛贖憊綴繹頸韲絞韈詮韆鞴鞐羈錐梱鞦誡頒諦翹鞨澆獰熾漣聾絆瀉袞訶鞜鞆懴靺鞁靹瀘靱憚暉驤撓諭靤櫓鰐靜閔轍瓏諌靉蝦靈蹌靆霤逕霙兌輓雜訟襍隸靭鬢隱闕賄嶄軾險陦陝鱗陞鈍滸嘖陏阯韃鰲阨闢關闍馴濶閧頷躊閠婁鈬鉉閙鴿閖閊渦懾閇钁駅薐籬蛍輾墾鑽謨顱鑵釟儼檸桟絹謗竃鈩詣倹鑪柵饅轄棗鑢嫋鑛鑄贅鑒鑁鐡輳闌鐵癆緬鐶鹸輒馭韜喞鐇鐓畝鐔鐚繚絳僥誨檻褻饋塢鏝紂噸鏥鎹涜諜鋸鎔鄒訛鐸薔瀏鐙攅紡鎭鍖雋惻紜鍮鍼鍠鍜緯錻楡瘡讒鑼緝躡錵錺釁綏矚錣駒錢鍄蠱鋺錏鋩銛獎締癲瀝鉐儂鴎鋤銕鉈鉅參襖詰釿貽靂燼釶葦嗇繭頡簒釼錮蛻釛釡釖餌鉗釐闔詁綾鯨釋醯醫醂謁嫻酳酘軼騁酖愴髏澗邉遲腎隨氈巓璽鉢轅絢飆遶賍漬遯遞諺誹騾蟄縹遖遉逎逹癩藹逧藾窯迴邇鐺磽殱瀕迯迚辷駢辭轣雛轢佇謔緲滌轜銹轗轉轌鯊諳輹諄磯靄颯謫渙輛輙軣軈嶼賂軅躾曖軆鸞軋緋躰貳鏗躙躔綸躄鸚閘蹠濾蹤搾蹐踴魘踰慟唄踐梟貯跿踈纓跼赱贔贓贐贊匱膾賻輟篩錠賣歟賤貮撻訥貭飼戝膿釧豼貎貍霑詼纜霽餃殯塋閂鶚錨繽鏘豬隕豎谺讙閹痺讌讀譽譯緘譟鹵餉葷譖輻證燉譌謚譁謠鵡諡鎧謌鐐諠紺諫諚誂巒觸謐靫觧觝觀蹣覽蝟簍覺覩覊覈襾襷躪襴鷲慫襭懣囁觴哢褝牘襌褞鯉褌褄裲裝裄礫攣謳袿軻袰袮袗鎌諂詆袵衵衞欒衒餒驥衂驍衄蠻餡蠧齪餞蠶蠑蠎齷蟷蠍蠏潁蟲蟇蟐螢蠅囈蝪蝨嶇蜑閭蛯蛬蠣靦蚰號乕虍蘰蘆鷺蘋蘓藥諛薹顰痙蕷藪鏤薑薀臍蝸蕋蘂蕣褸蕀蔔謾龕慂溏蔕蔟騫鴣蔘襤蓆嫗蓚噛蒻欖濘蓙蒟煬皚葢輦葹驪鷓葯飩萬轆葮蒭蒄曁蕚綰銓鉞儷曇駄贍萪菻儻駟躋蔆萠萢菷崢菎枠菫萓菴贄荵荳鵠讖莵嚀嬪莊莇鐫茣莖莟莚閏脛誥茘譎荅茖苙茆嚶苺襠苳艸鯤艷漑舮薈殤擯艪艨瞼覦艢芻艟艚犢艝綬鄲艀舩舖鴇歿舊與鸛檳臺臟覬飭塹臈臙臑膽膸膵慍櫚膰膓賁羶鳶腟膣膤膕膃諢腦脣脩肬冐肭肅聽聹聰捫聲聨聢鍍顎聟耡鷦靨飜翆譱羮覲羣羇羃銖羂罸輕罧罌薊罠罎鮟纎轡纖纔纐纒鶻續繿緕纃鑞繻繼繩鈿繪繙繖繧鯀縺繦縱縒縡縣縅誚緻緤颶綟緜殞綯總綫綵綛絽襃徠經絣饗絏絎縉絖紵紮絅詬糺鳬橢糴縊糒糘鶩糂鍬糀粨粡粫粢粭粐浹粃籵曄訐籖籤籟籘軫奩籐籏籔簷篶鴕簗簓簀蘚殫籠儕愾簔簑縟篏箙幃箏箒箚箟鑾箘筬獪筰筴筥筅饌筍筺騅笶笵笘笂甌竢竡竝竚竓竏謄訖誑竍竊窰儔竈穽龝穩椏穉穃稾稱稟稙稘鑠顴秡潯槞秬禮禪齋繝贋繕禝瘧縵祿祕礙篋礑賃讎礒礇磚奐儺磑藺簣嬋碯碪賑緇碵碆硴礪砠礦矼矇飴瞹瞶眛眥眞眤盻餾蘯盪莢盡皹皰皃囀鴆絛皀鰍發訌癶媼癧癪癨癢癡鱸癜癈穡瘻瘉犖痳痲痃疳疂櫛螻疉疊疇鑷當畭畫畧縞畩槧畆畉畊畍畄檣紕齟尢甼瀬甦甞甕甅轂甃瓸齬訃瓱瓰瓲瓩瓧瓔幗珸瑯璢僉珎獻獵獨魎梔猯狹狢狆犲蓴鶉犧獺犇犂鴟牴牋綣牀爼爲爭爐燿燵薺燬燒隲燗熕燻紆稈黷櫺煖熈煕鍔烋烱詒灣鷙饉竰鰻灑煢騏瀰瀁瀋濛諤濔駻濕濟躑齎謖澪濆廩澣摶堊澑濳鏃潛澀澁滷滯滉溂磧滿渟湶渮淕淺駑淒渕濤鰥諞浤洳洟覯泙沺泝沒汳篳沚沍汢氣毬毟毆殼殲殪廡殕殘殀歸歡歐齦飮盜錙欟鬱欅蘢鬮櫻櫟櫑櫞蘗閼飫檢檍鷂樢樸橸樶橲慳樌樓櫁樒覡槫樔蕎槭誄樞槹權樛樂槨榠榑樮槝榾槓榿榮榲楪蕘檪榁楙楴椹銃楾楜輊棆椡椣椚蕁椪闃椨縋棯椥椄齲椶棧棔椌癬棡椦椢椈橈棊桾憮梍梺鮫梠梹檮梛條桿瘍桙栫桍驂痾懍栞檜柧柆柎枹貲柮柤枴枅銑枡輜臚礬枦枌枩杤杣杙朷朸杁朿朮朞朖滝鮎朏曵曠曚暸暼曉暘暎暃晢晧晝晉晄昜旡旙旛斷變斂喰數鬩敘敍攷攴攜擽擴軛擶擡舉擧據攪摎臠瀲傴搨搗攝鯢鰭搆搖掵癇魴掟閾掫掎櫪挾鐃拵挧挌萇癰珱擔拑抃抂扨扠扞苧戲戞戉戀懼懽懺憺懆懃懷應憑憇憖憙慓慱慥慯慴慙慘慄愽戔愼惱闥愡愃惷悽忰惓躓惡悋悧悗悁恆恊恟恷鷸怺怱緡怐恠悳從徑彿輅徃彡彙彑彎彌彈彁羆弸弖彜弉廸廴廰廳廱廢廚廝廣廏廐廈廁幵鰓幤幎黽帶帋巵巛巖巉嶐嶽嶮嶬嶝嵶嵳嵎嵒鋏崘鮭崙崚崑崟嵜崕崋嶌峺峽峩萵峇岾頏峅岼岶岻妛癘潟屶蒔乢屮屬屓嘸屆覘賚尨尠尓冪對鎰鮒專將尅轤寳譫鵜齏寶寫寢蹕實寉寃斈學孅竕駘孃嬾鱈嬶嫐糶嫺娵婬娚姙侫妝奬奧竒夲夬艫夛譛夐壽壼壻懌壺壯壜壥壘壗壓墮墸墻壞墺墫墹堽塰塲堝埣埖埓鏨埆垰垪垤垳垉坿垈鉚埀坩圸圷圦鱒團壙圍國圀琺囮囓囑囎愨囃嚴嚮嚥嚔嚠嚊營剴噐嗹咼喨單啝唸啗啅啌啣啀唹哘鰹咾咥鏑咢呰呟吽叺雙厰剄卻夘卩覿凖卍丗卆區紲匸匳勹鷯勸勵纉勳勠勦勣勞勗勍劵劼辧劑剱劒劔劍剳筧剋剏刧刔刋鮃刄凾凵琿凩處凅冱冫冩冦冖冓冑冏囘冂兩竸兒儚鮪儖儁樅儉價僣僞傳僊傚偖偐會伜倅俥俤俛俔儘來侘仭黶仂亰亠亞弍亊亅亂乂丿丼丶鉦丱弌椀亙艤錬憐暦隷涙齠瑠糧稜瞭涼葎裡裏慾葉遊縲猶湧癒鑓匁籾戻杢黙網麺無夢粍脈麿侭桝柾槙釦僕鉾豊砲峯穂諏鋪辺箆塀併雰鈷仏蕕払淵複鋲氷俵柊毘樋釆鯡範汎氾塙噺抜醗発畠畑筈硲萩楳盃拝覇覗廼禰韮駸匂弐貰畷楢薙齶瀞椴栃峠働燈梼嶋兎澱紬嬬辻槻栂塚鎚捗勅銚聴徴彫弔瀦酎註築恥歎蛸皸凧託択瀧辿鯛騨楕詑揃蔵鎗荘窓蟶捜惣遡疎曽岨糎薦栴蹟跡塒隻製棲摺椙髄酔粋醸譲穣壌剰窶乗鍾衝纈昇廠藷準楯従醜週讐蒐繍収呪捨舎偲鏐篠蔀雫宍鴫児諮誌糸屍讃錆鯖皐冊糲笹碕埼榊堺冴砕瑳込狛穀麹閤砿紘広紿効倖檎後個絃捲圏決傑罫繋渓恵係繰粂駈粁脅況兇禦拠喫気機棄蟯幾願翫巌舘陥櫨潅幹姦巻乾苅栢蚫鞄樺椛梶橿樫掛穫浬蓋廻壊蔦菓箇価仮贇沖於薗煙詠榎頴洩叡嶢雲噂欝韻鰯稲壱闇扱蜆鯵穐齔姶鱠'#一共3048个在汉化文本中不常用的汉字，用于被临时替换，通常来说是够用了。

#先遍历一遍文本，通过GetInvalidChars找出所有不受支持的字符，映射到数字；再从replacelist中排除本来就被使用了的汉字。
#生成hanzidic

def GetInvalidChars(text,tempdict,charlist):#返回输入文本中不受支持的单字
    InvalidChars=[]
    for char in text:
        try:
            char.encode(encoding='sjis')
        except UnicodeEncodeError:
            if char not in tempdict:
                tempdict[char]=len(tempdict)
        if char in charlist:
            charlist.replace(char,'')
    return tempdict,charlist
    
def Createhanzidict(tempdict,replacelist):#输出hanzidic,target_chars,source_chars
    hanzidic={}
    for char in tempdict:
        try:
            hanzidic[char]=replacelist[tempdict[char]]
        except IndexError:
            print('用于替换的字符不够了，请再补充一些，或者检查你的代码，因为这通常不会发生。')
            raise RuntimeError
    target_chars=''
    source_chars=''
    for char in hanzidic:
        target_chars=target_chars+char
        source_chars=source_chars+hanzidic[char]
    return hanzidic,target_chars,source_chars

def teshuzifutihuan(text):#匹配时去除特殊字符 
    text=re.sub('\[([^|\]]+)\|','',text)#删除脚本中的注音标识
    text = text.replace("♪", "").replace("〜", "").replace("～", "").replace("?", "").replace(" ", "").replace('\u3000','').replace('\t','').replace(']','').replace('[・|','').replace('『','').replace('』','').replace('[・・|','').replace("・", "").replace('。','').replace('\n','')
    return text

def fuhaotihuan(text):#替换掉译文中一些不支持的常见特殊符号形式，以正常显示
    return text.replace('—','ー').replace('～','〜').replace('“','「').replace('”','」').replace('·','・')

def hanzitihuan(text,hanzidict):#主函数，实行对汉字的替换
    replaced_string=''
    for char in text:
        replaced_string += hanzidict.get(char, char)
    return replaced_string

def ChangeUFIConfig(UFIConfigpath,source_chars,target_chars):
    with open(UFIConfigpath,'r',encoding='utf8',errors='ignore') as f:
        f=json.load(f)
        f["character_substitution"]["source_chars"]=source_chars
        f["character_substitution"]["target_chars"]=target_chars

    with open(UFIConfigpath,'w',encoding='utf8') as fout:
        json.dump(f,fout,ensure_ascii=False,indent=4)
    