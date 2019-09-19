rotor = ['a','b','c','d','e','f']

def rotate(rotor):
    tmp_r = rotor.pop(0)
    rotor.append(tmp_r)
    return rotor

if __name__ == "__main__":
    rotate(rotor)
    print(rotor)

