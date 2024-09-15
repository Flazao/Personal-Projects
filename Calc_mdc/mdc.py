from math import gcd #Importando a biblioteca de math

#Inicio pra separar e ficar bonitinho
print('-='*30)
print('Calculo de MDC')
print('-='*30) 

lista = [] #criando uma lista vazia pra adicionar os valores aqui

while True: #estrutura de repetição pra colocar o quanto de numeros voce quiser
    
    valor = int(input('Determine Os valores utilizados para o Mdc [0 para parar]: ')) #pedindo informação ao usuário
    if valor == 0: #caso valor for igual a 0
        break #pare o codigo inteiro
    lista.append(valor) #adicionando os valores a lista

def calc_mdc(listas): #função para calcular a lista
    if not lista: #se nao estiver na lista
        return None #retorne nada
    
    mdc_atual = lista[0] #criando nova variavel para adicionar o valor da lista no index 0
    for num in lista[1:]: #para cada numero na lista começando no index 1 (para nao printar 0)
        mdc_atual = gcd(mdc_atual, num) #utilizando o gcd (função mdc da biblioteca math) na variavel da lista e em cada numero dela
    return mdc_atual #retorna o mdc de todos os numeros

if lista: #se tiver coisa na lista
    mdc = calc_mdc(lista) #chama a função em uma nova variavel
    print(f'Os valores determinados foram: {lista} ', end='') # printa os valores, end='' serve pra continuar a linha de baixo
    print(f'e o MDC deles foi: {mdc}') #printa o mdc
else: #se nao tiver nada na lista
    print('Você não colocou valor algum...') # printa isso