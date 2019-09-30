import random 
def randomPlugboard(): 
	plug = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25] #原始plugboard 
	alreadyUseList = [] #用來記錄哪些已經換過了 
	i = 1 
	while i <= 6: 
		firstNum = random.randint(0,25)#random 第1個數字(0~25) 
        secondNum = random.randint(0,25)#random 第2個數字(0~25) 
                
        #if兩個數字其中一個已經換過了(存在於alreadyUseList) 
        if firstNum in alreadyUseList: 
			continue 
        elif secondNum in alreadyUseList: 
			continue 
                        
        #else if兩個數字相同         
        elif firstNum == secondNum: 
			continue 
                
        else: 
            #plugboard兩個數字交換位置 
            firstNumIndex = plug.index(firstNum) 
            secondNumIndex = plug.index(secondNum) 
            plug[firstNumIndex] = secondNum 
            plug[secondNumIndex] = firstNum 
                        
            #記錄用過的兩個數字到alreadyUseList(alreadyUseList.append) 
            alreadyUseList.append(firstNum) 
            alreadyUseList.append(secondNum) 
                        
            #成功交換i++ 
            i += 1
			
    return plug 
