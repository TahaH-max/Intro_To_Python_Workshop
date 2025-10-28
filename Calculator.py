def main():
    name = (input('Hello, what is your name?: '))
    print('Hello, ', name)
    while True:
        user_input = input('Enter your equation or press q to quit: ')
        if user_input == 'q':
            break
        equation = user_input.split()
        a = float(equation[0])
        b = equation[1]
        c = float(equation[2])
        print(ops(a, b, c))

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    try:
        return a/b
    except ZeroDivisionError:
        return 'Syntax error: dividing by zero'

def power(a, b):
    r = a
    for i in range(b-1):
        r = r * a
    return r

def ops(a, b, c):
    if b == '+':
        return add(a, c)
    elif b == '-':
        return subtract(a, c)
    elif b == '*':
        return multiply(a, c)
    elif b == '/':
        return divide(a, c)
    elif b == '^':
        return power(a, c)
    else:
        return "Invalid input"
main()

