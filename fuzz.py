#4-function calculator
def simpleCalc(n1, n2, operation):
    res = 0
    if (operation == '+'):
        res = n1 + n2
    elif operation == '-':
        res = n1 - n2
    elif operation == '*':
        res = n1 * n2
    elif operation == '/':
        res = n1 / n2
    return res

def checkNonOperation():
    operation_ = '='
    simpleCalc(50, 5, operation_)

def calcFuzzer():
    checkNonOperation()

if __name__ == '__main__':
    n1, n2, op = 50, 5, '+'
    data = simpleCalc(n1, n2, op)
    print('Operation: {}\nResult: {}'.format(op, data))
    calcFuzzer()

def greaterThan(var, comp):
    if (var > comp):
        return True
    elif var < comp:
        return False
