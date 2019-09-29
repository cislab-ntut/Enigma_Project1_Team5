## 加密
## 流程圖
```
明文 -> plugboard -> rotorIII -> rotorII -> rotorI -> reflector -> rotorI -> rotorII -> rotorIII -> plugboard -> 密文	
```

## 流程說明
- [明文 -> plugboard](#明文--gt-plugboard)
- [plugboard -> rotorIII](#plugboard--gt-rotorIII)
- [rotorIII -> rotorII](#rotorIII--gt-rotorII)
- [rotorII -> rotorI](#rotorII--gt-rotorI)
- [rotorI -> reflector](#rotorI--gt-reflector)
- [reflector -> rotorI](#reflector--gt-rotorI)
- [rotorI -> rotorII](#rotorI--gt-rotorII)
- [rotorII -> rotorIII](#rotorII--gt-rotorIII)
- [rotorIII -> plugboard -> 密文](#rotorIII--gt-plugboard--gt-密文)

### 明文 -> plugboard
plugboard本身是一個list，用明文當作index來找到對應的字母，EX: 明文A -> plugboard B
### plugboard -> rotorIII
使用前面得到的字母當作內圈的index找到rotorIII的內圈字母，接著找到外圈字母的位置，舉例來說，假設內圈字母為C，需要找到的就是外圈中字母C的位置，EX: [Y,Z,A,B,C,.....]以這個list為例，C的位置是4
### rotorIII -> rotorII
跟上面一樣，使用剛剛在rotorIII找到的外圈位置，以上面的例子來說就是4，用這個當作rotorII內圈的index，接著就找該字母在rotorII外圈所在的位置。
### rotorII -> rotorI
同rotorIII -> rotorII
### rotorI -> reflector
與明文->plugboard一樣，使用前一步所得到的字母當作index找到對應的字母
### reflector -> rotorI
假設前一步得到的字母為S，轉換成數字就是18(A = 0, B = 1,....)，則在這一步驟中，我們要先找到rotorI外圈index=18的字母是甚麼，假設外圈index=18找到的字母是Z，接下來就是找到內圈中Z在哪個位置，也就是內圈中Z的index是多少
### rotorI -> rotorII
上一步會得到一個index，在這一步驟中要做的事情跟上面是一樣的，藉由前面得到的index找到外圈字母，接著再藉由外圈字母找到內圈該字母所在的位置，EX: 前一步所得到的index為2，在rotorII外圈中index=2為F，接下來去找到內圈中F的位置，假設為19
### rotorII -> rotorIII
同rotorI -> rotorII
### rotorIII -> plugboard -> 密文
就跟一開始一樣，用前一步得到的字母當作index，找到對應的字母，並將此字母回傳
