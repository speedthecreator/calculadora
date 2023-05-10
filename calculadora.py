def calculator(num1, num2, operator):
    if operator == "+":
        result = num1 + num2
    elif operator == "-":
        result = num1 - num2
    elif operator == "*":
        result = num1 * num2
    elif operator == "/":
        result = num1 / num2
    else:
        print('Operação inválida!')
        return
    print('O resultado é: {:.2f}'.format(result))


calculator(2, 5, "+")
