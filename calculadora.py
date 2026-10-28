from unittest import case

def soma(n1, n2):
    return n1 + n2

def sub(n1, n2):
    return n1 - n2

def mult(n1, n2):
    return n1 * n2

def calculadora(operacao, n1, n2):

    match operacao:
        case 1:
            return soma(n1, n2)
        case 2:
            return sub(n1, n2)
        case 3:
            return mult(n1, n2) 