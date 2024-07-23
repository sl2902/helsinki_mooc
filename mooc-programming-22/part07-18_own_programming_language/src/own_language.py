# Write your solution here
def value(x, data):
    characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if x in characters:
        return data[characters.index(x)]
    else:
        return int(x)
 
def condition(a, condition, b):
    if condition == "==":
        return a == b
    if condition == "!=":
        return a != b
    if condition == "<":
        return a < b
    if condition == "<=":
        return a <= b
    if condition == ">":
        return a > b
    if condition == ">=":
        return a >= b
 
def run(program):
    length = len(program)
    row = 0
    characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    data = [0]*26
    result = []
    while True:
        if row == length:
            break
        parts = program[row].split(" ")
        if parts[0] == "PRINT":
            result.append(value(parts[1], data))
        if parts[0] == "MOV":
            data[characters.index(parts[1])] = value(parts[2], data)
        if parts[0] == "ADD":
            data[characters.index(parts[1])] += value(parts[2], data)
        if parts[0] == "SUB":
            data[characters.index(parts[1])] -= value(parts[2], data)
        if parts[0] == "MUL":
            data[characters.index(parts[1])] *= value(parts[2], data)
        if parts[0] == "JUMP":
            row = program.index(parts[1]+":")
            continue
        if parts[0] == "IF":
            if condition(value(parts[1], data), parts[2], value(parts[3], data)):
                row = program.index(parts[5]+":")
                continue
        if parts[0] == "END":
            break
        row += 1
    return result

if __name__ == "__main__":
    program1 = []
    program1.append("MOV A 1")
    program1.append("MOV B 2")
    program1.append("PRINT A")
    program1.append("PRINT B")
    program1.append("ADD A B")
    program1.append("PRINT A")
    program1.append("END")
    result = run(program1)
    print(result)

    program2 = []
    program2.append("MOV A 1")
    program2.append("MOV B 10")
    program2.append("begin:")
    program2.append("IF A >= B JUMP quit")
    program2.append("PRINT A")
    program2.append("PRINT B")
    program2.append("ADD A 1")
    program2.append("SUB B 1")
    program2.append("JUMP begin")
    program2.append("quit:")
    program2.append("END")
    result = run(program2)
    print(result)

    program3 = []
    program3.append("MOV A 1")
    program3.append("MOV B 1")
    program3.append("begin:")
    program3.append("PRINT A")
    program3.append("ADD B 1")
    program3.append("MUL A B")
    program3.append("IF B <= 10 JUMP begin")
    program3.append("END")
    result = run(program3)
    print(result)

    program4 = []
    program4.append("PRINT A")
    program4.append("END")
    result = run(program4)
    print(result)

    program5 = []
    result = run(program5)
    print(result)

    program6 = []
    program6.append('MOV A 10')
    program6.append('start:')
    program6.append('PRINT A')
    program6.append('SUB A 1')
    program6.append('IF A > 0 JUMP start')
    program6.append('END')
    result = run(program6)
    print(result)

    program7 = []
    program7.append("MOV A 1")
    program7.append("MOV B 1")
    program7.append("start:")
    program7.append("MUL A 2")
    program7.append("ADD B 1")
    program7.append("IF B != 101 JUMP start")
    program7.append("PRINT A")
    result = run(program7)
    print(result)

    program8 = []
    program8.append("MOV A 1")
    program8.append("MOV B 999")
    program8.append("start:")
    program8.append("ADD A 1")
    program8.append("SUB B 1")
    program8.append("ADD C 1")
    program8.append("IF A == B JUMP end")
    program8.append("JUMP start")
    program8.append("end:")
    program8.append("PRINT C")
    result = run(program8)
    print(result)

    program9 = []
    program9.append('MOV N 100')
    program9.append('PRINT 2')
    program9.append('MOV A 3')
    program9.append('start:')
    program9.append('MOV B 2')
    program9.append('MOV Z 0')
    program9.append('test:')
    program9.append('MOV C B')
    program9.append('new:')
    program9.append('IF C == A JUMP virhe')
    program9.append('IF C > A JUMP pass_by')
    program9.append('ADD C B')
    program9.append('JUMP new')
    program9.append('virhe:')
    program9.append('MOV Z 1')
    program9.append('JUMP pass_by2')
    program9.append('pass_by:')
    program9.append('ADD B 1')
    program9.append('IF B < A JUMP test')
    program9.append('pass_by2:')
    program9.append('IF Z == 1 JUMP pass_by3')
    program9.append('PRINT A')
    program9.append('pass_by3:')
    program9.append('ADD A 1')
    program9.append('IF A <= N JUMP start')
    result = run(program9)
    print(result)
