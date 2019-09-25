import sys
from itertools import permutations

alphet_to_num = {"A":0,"B":1,"C":2,"D":3,"E":4,"F":5,"G":6,"H":7,"I":8,"J":9,"K":10,"L":11,"M":12,"N":13,"O":14,"P":15,"Q":16,"R":17,"S":18,
				"T":19,"U":20,"V":21,"W":22,"X":23,"Y":24,"Z":25}
num_to_alphet = {0:"A",1:"B",2:"C",3:"D",4:"E",5:"F",6:"G",7:"H",8:"I",9:"J",10:"K",11:"L",12:"M",13:"N",14:"O",15:"P",16:"Q",17:"R",18:"S",
				19:"T",20:"U",21:"V",22:"W",23:"X",24:"Y",25:"Z"}

def read_file(filename):
	global alphet_to_num
	f = open(filename, "r")
	lines = f.readlines()
	string = ""
	for line in lines:
		line.strip('\n')
		string = string+line
	lst = list(string)
	file = [alphet_to_num[char] for char in lst]
	return file

RI = read_file('RI.txt')
RII = read_file('RII.txt')
RIV = read_file('RIV.txt')
RV = read_file('RV.txt')


'''
print('---- Test  4 pick 2 ----')
test = ['A','B','C','D']
testResult = list(permutations(test,2))
print(testResult)
'''

print('Rotor Permutations')
rotors = [['RI',RI],['RII',RII],['RIV',RIV],['RV',RV]]
result = list(permutations(rotors,2))

for i in range(len(result)):
    print(result[i][0][0],result[i][1][0])
print('All Permutations:',len(result))