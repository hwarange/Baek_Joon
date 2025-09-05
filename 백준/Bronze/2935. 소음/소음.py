question = [input() for i in range(3)]
if question[1] == '*':
    print(int(question[0])*int(question[2]))
else:
    print(int(question[0])+int(question[2]))