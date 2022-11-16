##===============================01: Odd or Even===============================
num = int(input("輸入一個數字: "))
if (num % 2) == 0:
    print("{0} 是偶數".format(num))
else:
    print("{0} 是奇數".format(num))



##===============================02: Mad Libs===============================
#story = input ("請問需要建造幾次模板故事：")
num2 = input ("請輸入課程期數：")
classname = input ("請輸入課程名稱：")
name = input ("請輸入姓名：")
background = input ("請輸入您的背景(科系或職業)：")
expect = input ("請簡述對於本課程得期望(列出幾點修完課程想得到的技能/對自己未來的規劃)：")
print ("------------------------------------------")
print ("第", num2, "期 - ", classname)
print ("姓名：", name)
print ("學生背景：", background)
print ("==========================================")
print (name, "修習完課程[", classname, "]後，")
print ("結業成果獲得：", expect)
print ("Well Done.")



##===============================03: Guess the number===============================
import random
ans3 = random.randint(1,100)
#print (ans3)
min = 1
max = 100
count = 0
while True: 
    print ("請猜", min, "~", max, "之間的數字：", end='')
    try: 
        num3 = int(input ())
        count += 1
        if num3 == ans3:
            print ("恭喜答對！你猜了", count, "次！",)
            break
        elif num3 < ans3:
            min = num3
            print ("答錯！你猜了", count, "次！", end='')
            yn = input("是否要繼續猜?(Y/N)：").upper()
            if yn == "Y":
                continue
            else: 
                break
        elif num3 > ans3: 
            max = num3
            print ("答錯！你猜了", count, "次！", end='')
            yn = input("是否要繼續猜?(Y/N)：").upper()
            if yn == "Y":
                continue
            else: 
                break
    except: 
        print ("你輸入的並非1~100之間的整數，請重新輸入")


##===============================04: Word Count===============================
#### 使用者輸入一段文字或讀取一檔案，程式統計字數。
##輸入(Input):我要成為寫程式的專家
##輸出(Output):你用了 10 個文字述說內心的想法
#### 在特定的文章字串中搜尋輸入的特定字，請使用者輸入欲搜尋的文字，印出總共有幾個。
##輸入(Input):天
##輸出(Output): 9
    ##* 進階:計算文章中去除標點符號後的字數，找出文章中出現最多的字與次數

#04-1:
word = input ("請輸入想法： ")
print ("你用了%d個文字來形容你的想法"% (len(word)))

#04-2:
s = '''漢皇重色思傾國，御宇多年求不得。
楊家有女初長成，養在深閏人未識。
天生麗質難自棄，一朝選在君王側。
回眸一笑百媚生，六宮粉黛無顏色。
春寒賜浴華清池，溫泉水滑洗凝脂；
侍兒扶起嬌無力，始是新承恩澤時。
雲鬢花顏金步搖，芙蓉帳暖度春宵；
春宵苦短日高起，從此君王不早朝。
承歡侍宴無閑暇，春從春遊夜專夜。
後宮佳麗三千人，三千寵愛在一身。
金屋妝成嬌侍夜，玉樓宴罷醉和春。
姊妹弟兄皆列士，可憐光彩生門戶。
遂令天下父母心，不重生男重生女。
驪宮高處入青雲，仙樂風飄處處聞。
緩歌慢舞凝絲竹，盡日君王看不足。
漁陽鼙鼓動地來，驚破霓裳羽衣曲。
九重城闕煙塵生，千乘萬騎西南行。
翠華搖搖行復止，西出都門百餘里；
六軍不發無奈何？宛轉蛾眉馬前死。
花鈿委地無人收，翠翹金雀玉搔頭。
君王掩面救不得，回看血淚相和流。
黃埃散漫風蕭索，雲棧縈紆登劍閣。
峨嵋山下少人行，旌旗無光日色薄。
蜀江水碧蜀山青，聖主朝朝暮暮情。
行宮見月傷心色，夜雨聞鈴腸斷聲。
天旋地轉迴龍馭，到此躊躇不能去。
馬嵬坡下泥土中，不見玉顏空死處。
君臣相顧盡霑衣，東望都門信馬歸。
歸來池苑皆依舊，太液芙蓉未央柳；
芙蓉如面柳如眉，對此如何不淚垂？
春風桃李花開日，秋雨梧桐葉落時。
西宮南內多秋草，落葉滿階紅不掃。
梨園子弟白髮新，椒房阿監青娥老。
夕殿螢飛思悄然，孤燈挑盡未成眠。
遲遲鐘鼓初長夜，耿耿星河欲曙天。
鴛鴦瓦冷霜華重，翡翠衾寒誰與共？
悠悠生死別經年，魂魄不曾來入夢。
臨邛道士鴻都客，能以精誠致魂魄；
為感君王輾轉思，遂教方士殷勤覓。
排空馭氣奔如電，升天入地求之遍；
上窮碧落下黃泉，兩處茫茫皆不見。
忽聞海上有仙山，山在虛無縹緲間。
樓閣玲瓏五雲起，其中綽約多仙子。
中有一人字太真，雪膚花貌參差是。
金闕西廂叩玉扃，轉教小玉報雙成。
聞道漢家天子使，九華帳裡夢魂驚；
攬衣推枕起徘徊，珠箔銀屏迤邐開。
雲鬢半偏新睡覺，花冠不整下堂來。
風吹仙袂飄飄舉，猶似霓裳羽衣舞。
玉容寂寞淚闌干，梨花一枝春帶雨。
含情凝睇謝君王，一別音容兩渺茫。
昭陽殿裡恩愛絕，蓬萊宮中日月長。
回頭下望人寰處，不見長安見塵霧。
唯將舊物表深情，鈿合金釵寄將去。
釵留一股合一扇，釵擘黃金合分鈿。
但教心似金鈿堅，天上人間會相見。
臨別殷勤重寄詞，詞中有誓兩心知，
七月七日長生殿，夜半無人私語時：「
在天願作比翼鳥，在地願為連理枝。」
天長地久有時盡，此恨綿綿無絕期。
'''
word4 = input ("請輸入欲搜尋的文字來計算出現次數：")
count4=s.count(word4)
print (word4,"的出現次數為", count4)



##===============================05: Email slicer===============================
### 05 - Email 域名判斷器（Email slicer）
#### 請用戶輸入 Email 地址，然後判斷它是自定義域名還是熱門域名。
## > 題目：<br>
## 輸入(Input):shelly200318@hotmail.com.tw  <br>
## 輸出(Output):Your username is 'shelly200318' and your domain name is 'hotmail.com.tw' <br>
    ## * 進階：把常用的信箱存成字典，加入判斷是否為
    ## >輸入(Input):mary.jane@gmail.com  <br>
    ## 輸出(Output):這是註冊在 Google 之下的 Email 地址 <br>
    ## 輸入(Input):matt.pan@myfantasy.com  <br>
    ## 輸出(Output):這是在 myfantasy 之下自定義域

email = input ("please enter your email: ").strip()
usr = email [0:email.index("@")]
domain = email [email.index("@")+1: ]
print ("your username is '{}' and your doamin name is '{}'.".format(usr,domain))



##===============================06: Pass List===============================
### 06 - 及格名單（Pass list）
#### 請使用集合功能來完成各科級名單的判斷
##米花市帝丹小學一年级B班正舉辦期中考試
##數學及格的有：柯南、灰原、步美、美環、光彦
##英文及格的有：柯南、灰原、丸尾、野口、步美
##以上已列出全班所有人
##請分別列出<br>
##數學及格但英文不及格的同學名單<br>
##數學不及格但英文及格的同學名單<br>
##兩者皆及格名單<br>
##* Hint:差集(減法)、交集

mathpass = {"柯南", "灰原", "步美", "美環", "光彦"}
engpass = {"柯南", "灰原", "丸尾", "野口", "步美"}
print ("班上所有人:", mathpass | engpass)
print ("數學及格但英文不及格的同學: ", mathpass - engpass)
print ("數學不及格但英文及格的同學: ", engpass - mathpass)
print ("兩者皆及格的同學: ", mathpass & engpass)



##===============================07: Search File===============================
### 07 - 查詢路徑下所有檔案
#### 請使用者輸入路徑，自動抓取路徑下所有檔案名稱
##輸入(Input):data\testfile 或 D:\code\ML_202105\data\testfile  <br>
##輸出(Output):
    ##* 進階: 把file的學號抓出來，另存成一個新的csv檔

import os

# 指定要查詢的路徑
yourPath = input("enter path: ")
# 列出指定路徑底下所有檔案(包含資料夾)
allFileList = os.listdir(yourPath)
# print (allFileList)

# 逐一查詢檔案清單
for file in allFileList:
    if os.path.isdir(os.path.join(yourPath,file)):
        print("I'm a directory: " + file)
    #   使用isfile判斷是否為檔案
    elif os.path.isfile(os.path.join(yourPath,file)):
        print("I'm a File: " + file)
        

        #file = file.split('_')
        #print(file[1])



##===============================08: Shutil===============================
##在目前所在的目錄下建立一files資料夾
##令使用者輸入一數字N，並在files資料夾中建立f1, f2… fN等N個資料夾後列出files的資料夾內容
##將files資料夾裡的f1資料夾重新命名成folder1後再列出files的資料夾內容
##移除files資料夾中的folder1後再列出files的資料夾內容
##最後移除files資料夾
## ※須先退出files資料夾(os.chdir(../)) ![image.png](attachment:image.png)
import os
import shutil

#先判斷files存不存在
if os.path.exists('files'):
    shutil.rmtree('files')

os.mkdir('files')

n = int(input("please enter numbers of files: "))

os.chdir('files')
for i in range (1,n+1):
    os.mkdir('f'+str(i))
print(sorted(os.listdir()))
a = input ("Enter")  #設停損點等使用者按enter後才會進行之後的程式碼，debug時可用

os.rename ('f1','folder1')
print (sorted(os.listdir()))
a = input ("Enter")

os.rmdir('folder1')
print (sorted(os.listdir()))
a = input ("Enter")

os.chdir('../')  #同層路徑: ./ 可省略不寫；上一層路徑: ../
shutil.rmtree('files')


##===============================09: palindrome===============================
#### 請使用者輸入單字，判斷它是否為回文，也就是該單字前後對稱，例如 madam，從前讀到後或是從後讀到前的順序都是 madam。
##輸入(Input): 雨 滋 春 樹 碧 連 天  天 連 碧 樹 春 滋 雨 <br>
##輸出(Output):The text you have entered is a palindrome!<br>
##輸入(Input): 資工訓練班 <br>
##輸出(Output):The text you have entered is not a palindrome.

#請使用者輸入一串字串，先轉換字串為統一小寫
def convertInputString():
    rawInput = input("\nPlease enter a word, phrase, or a sentence \nto check if it is a palindrome: ") 
    rawString = rawInput.lower()
    rawList = list(rawString)
    return rawList

#去除相關標點符號
def stripAnalphabetics(dirtyList): 
    analphabeticList = [" ", "-", ".", ",", ":", ";", "!", "?", "'", "\""] 
    for character in analphabeticList:
        if character in dirtyList:
            dirtyList.remove(character)   #是list時才能用replace，這裡是string用remove
            return stripAnalphabetics(dirtyList)  #自己呼叫自己
    return dirtyList

def runPalindromeCheck(straightList):
    reversedList = straightList[::-1] #相當於[0::-1], 從[0]的位置到著看? [1,2,3,4]  --> [4,3,2,1] 若[2::-1]-->[3,2,1]
    if reversedList == straightList: 
        return "The text you have entered is a palindrome!" 
    else: 
        return "The text you have entered is not a palindrome." 

#建立主程式
def main(): 
    print("\nPalindrome checker") 
    originalList = convertInputString()
    originalList = stripAnalphabetics(originalList)
    PalindromeCheck = runPalindromeCheck(originalList)
    print (PalindromeCheck)

#呼叫主程式
main() 


##===============================10: 總成績計算===============================
##請讀取 `data/english_list.csv`與`data/math_list.csv`檔案(`utf-8`)後，將每位同學的英文與數學成績加總起來，並將檔案寫入至 `./Score.csv`中，編碼成`utf-8`<br>
##最後列印出每位學生姓名與加總後的分數<br>
fin_E = open('data/english_list.csv',"r",encoding='UTF-8')
fin_M = open('data/math_list.csv',"r",encoding='UTF-8')
lisE=[]
lisM=[]
name=[]
for line in fin_E.readlines():
    #print (line,end='')
    line = line.strip().split(",")
    #print (line)
    lisE.append(line[1])
    name.append(line[0])

for line in fin_M.readlines():
    #print (line,end='')
    line = line.strip().split(",")
    #print (line)
    lisM.append(line[1])
    
score=[]
fout = open("Score.csv","w")
line=''
for i in range(1,len(lisE)):
    score.append(int(lisE[i])+int(lisM[i]))
    list1 = [name[i],str(score[i-1]),"\n"]
    print(name[i],str(score[i-1]))
    line = ",".join(list1)
    fout.write(line)
fin_E.close()
fin_M.close()
fout.close()
# '''
# line=''
# fout = open("Score.csv","r")
# for i in (len(name)):
#     print()
# '''