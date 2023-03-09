import sys

def main():
    if len(sys.argv) > 1:
        expression = format_expression(sys.argv[1])
        result = evaluate(expression, 0)[0]
        print(result)


def format_expression(expression):
    exp = []
    expression = leave_certain_chars(expression, ")0123456789.+-*/ eE")
    expression = detach_brackets(expression)
    expression = expression.split()
    for item in expression:
        if is_number(item):
            exp.append(item)
        else:
            for character in item:
                if is_operator(character) or character == ')':
                    exp.append(character)
    return exp

def leave_certain_chars(string, chars):
    return ''.join([char for char in string if char in chars])

def detach_brackets(string):
    return string.replace(')', ' )')

def evaluate(exp, i):
    operator = exp[i]
    operands, index_of_bracket = find_operands(exp, i + 1)
    result = compute(operator, operands)
    return result, index_of_bracket

def find_operands(exp, i):
    operands = []
    index = i
    while exp[index] != ')':
        if is_number(exp[index]):
            operands.append(exp[index])
        else:
            new_value, new_index = evaluate(exp, index)
            operands.append(new_value)
            index = new_index
        index += 1
    return operands, index

def is_operator(string):
    return string in ['+', '-', '*', '/']

def is_number(string):
    try:
        float(string)
        return True
    except ValueError:
        return False

def compute(operator, operands):
    if not all([is_number(operand) for operand in operands]):
        return operands[0]

    if len(operands) == 0:
        return '0'

    result = float(operands[0])
    for operand in operands[1:]:
        if operator == '+':
            result += float(operand)
        elif operator == '-':
            result -= float(operand)
        elif operator == '*':
            result *= float(operand)
        elif operator == '/':
            if float(operand) == 0:
                return "Cant"
            result /= float(operand)

    return int(result)

if __name__ == '__main__':
    main()