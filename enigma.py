import sys

alphet_to_num = {"A":0,"B":1,"C":2,"D":3,"E":4,"F":5,"G":6,"H":7,"I":8,"J":9,"K":10,"L":11,"M":12,"N":13,"O":14,"P":15,"Q":16,"R":17,"S":18,
				"T":19,"U":20,"V":21,"W":22,"X":23,"Y":24,"Z":25}
num_to_alphet = {0:"A",1:"B",2:"C",3:"D",4:"E",5:"F",6:"G",7:"H",8:"I",9:"J",10:"K",11:"L",12:"M",13:"N",14:"O",15:"P",16:"Q",17:"R",18:"S",
				19:"T",20:"U",21:"V",22:"W",23:"X",24:"Y",25:"Z"}


def encode(input):
	output = list()
	global num_to_alphet
	nonlocal plugboard, rotorI, rotorII, rotorIII, reflector, arrow, RIII_outside, RII_outside, RI_outside
	for char in input:
			rotorIII, RIII_outside = rotate(rotorIII, RIII_outside)

			if rotorII[1] == arrow[1] and rotorIII[0] != arrow[0]:
				rotorII, RII_outside = rotate(rotorII, RII_outside)
				rotorI, RI_outside = rotate(rotorI, RI_outside)
			if rotorIII[0] == arrow[0]:
				rotorII, RII_outside = rotate(rotorII, RII_outside)

	return output
	

if __name__ == "__main__":
	main()