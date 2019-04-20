
#Davide Clemente
#pyhton

expressao = list(input('Digita a expressão a ser avaliada. '))
cont = 0
bad_index = 0
balanco = 0
invalida = False
for i, carater in enumerate(expressao):
    if carater == ' ':
        expressao.pop(i)
        cont -= 1
    if carater == ')':
        if cont == 1:
            print('Expressão inválida!')
            invalida = True
            break
        balanco -= 1
        bad_index = expressao.index(carater)
    if carater == '(':
        cont = 0
        balanco += 1
        if bad_index < expressao.index(carater):
            print('Expressão inválida!')
            invalida = True
            break
    cont += 1

if invalida == False:
    if balanco != 0:
        print('Expressão inválida!')
    else:
        print('Expressão válida')
