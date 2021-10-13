import math

while True:
    
    a=int(input())
    b=int(input())

    print("calculator")

    print("+ sum")
    print("- sub")
    print("* mul")
    print("/ div")
    print("sin")
    print("cos")
    print("tan")
    print("cot")
    print("log")
    
    print("exit")

    op = input()

    if op == '+':
        result = a+b
    elif op == '-':
        result = a-b
    elif op == '*':
        result = a*b
    elif op == '/':
        if b != 0:
            result = a/b
        elif a == 0:
            print("can not divided by 0")
    elif op == 'sin':
        result = math.sin(a)
    elif op == 'cos':
        result = math.cos(a)
    elif op == 'tan':
        result = math.tan(a)
    elif op == 'cot':
        result = math.cot(a)    
    elif op == 'exit':
        break
    print(result)        
