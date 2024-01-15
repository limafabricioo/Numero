def pos_neg_zer(**kwargs):
    estado = 'Zero'
    for numero in kwargs:
        if kwargs[numero] > 0:
            estado = 'Positivo'
        elif kwargs[numero] < 0:
            estado = 'Negativo'
        else:
            estado = 'Zero'
    return estado
while True:
    numeros = int(input('Digite um número: '))
    resultado = pos_neg_zer(numero = numeros)
    print(f'O número {numeros} é : {resultado}')
    continuar = input('Deseja continuar? S - SIM e N - NÃO')
    if continuar.lower() == 'n':
        break