keyR = {"add": 32, "sub": 34, "mult": 24, "div": 26, "and": 36, "or": 37, "slt": 42}
keyI = {"addi": 8, "andi": 12, "ori": 13, "lw": 35, "sw": 43, "slti": 10, "beq": 4, "bne": 5}
keyJ = {"j": 2}


def dec_to_bi(n, digit):
    binary = ""
    while n > 0:
        binary += str(n % 2)
        n = n // 2
    for i in range(digit - len(binary)):
        binary += '0'
    binary = binary[::-1]
    return binary


def translate():
    with open('instructions.txt', 'w') as clear:
        clear.write('')

    with open('assembly.txt', 'r') as f:
        for line in f:
            ins = line[:-1]
            print(ins)
            ins = ins.split(' ')

            if(keyR.get(ins[0]) != None):
                print("R type instruction")
                to_separate = typeR(ins)

            elif (keyI.get(ins[0]) != None):
                print("I type instruction")
                to_separate = typeI(ins)

            elif (keyJ.get(ins[0]) != None):
                print("J type instruction")
                to_separate = typeJ(ins)
            else:
                pass

            divide(to_separate)


def typeR(ins):
    string = "000000"
    string += dec_to_bi(int(ins[2]), 5)  # rs
    string += dec_to_bi(int(ins[3]), 5)  # rt
    string += dec_to_bi(int(ins[1]), 5)  # rd
    string += "00000"
    string += dec_to_bi(keyR.get(ins[0]), 6)  # func
    return string


def typeI(ins):
    string = ""
    string += dec_to_bi(keyI.get(ins[0]), 6)
    string += dec_to_bi(int(ins[2]), 5)
    string += dec_to_bi(int(ins[1]), 5)
    string += dec_to_bi(int(ins[3]), 16)
    return string


def typeJ(ins):
    string = ""
    string += dec_to_bi(keyJ.get(ins[0]), 6)
    string += dec_to_bi(int(ins[1]), 26)
    return string


def divide(string):
    final = []

    final.append(string[0:8])
    final.append(string[8:16])
    final.append(string[16:24])
    final.append(string[24:32])
    print(final)
    write(final)


def write(final):
    with open('instructions.txt', 'a') as f:
        for i in final:
            f.write(i)
            f.write('\n')


def openfile():
    with open('assembly.txt', 'r') as f:
        for line in f:
            a = line[:-1]
            print(a)


translate()
