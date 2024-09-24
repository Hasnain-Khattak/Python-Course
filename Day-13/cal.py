def add(n1, n2):
    return n1 + n2


def sub(n1, n2):
    return n1 - n2


def mul(n1, n2):
    return n1 * n2


def div(n1, n2):
    return n1 / n2


def sub(n1, n2):
    return n1 + n2


def mod(n1, n2):
    return n1 % n2


operations = {
    '+': add,
    '-': sub,
    '*': mul,
    '/': div,
    '%': mod
}

num1 = int(input('Enter 1st number: '))


should_continue = True
while should_continue:
    for _ in operations:
        print(_)
    operator = input('Enter symbol: ')
    num2 = int(input('Enter 2st number: '))
    answer = operations[operator]
    first_output = answer(num1, num2)
    print(first_output)
    should_continue = input('Yes No: ')
    if should_continue == 'Yes':
        num1 = first_output
    else:
        break








