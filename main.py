print('Bem-vindo à Calculadora de Triângulos.''\n')

sair = False

while sair == False:

    escolha = input('Faça a sua escolha, Calcular: ( ÁREA DO TRIÂNGULO / ÂNGULO DO TRIÂNGULO ou SAIR?:' '\n')

    if escolha == 'area':
        altura = int(input('Digite a altura do triãngulo: '))
        base = int(input('Digite a base do triãngulo: '))
        area = (base * altura) / 2
        print('A área do triãngulo é:', area)

    if escolha == "sair":
       sair = True
       print('Até Breve!!!')

    elif escolha == 'angulo':
     lA = float(input('Informe o lado Direito: '))
     lB = float(input('Informe o lado Esquerdo: '))
     lC = float(input('Informe a Base do Triangulo: '))

     if lA < lB + lC and lB < lA + lC and lC < lA + lB:
        print('Os dados acima, PODEM FORMAR TRIANGULO ', end='')
        if lA == lB == lC:
         print('EQUILÁTERO')
        elif lA != lB != lC != lA:
         print('ESCALENO')
        else:
         print('ISÓSCELES')
     else:
         print('Os dados acima, NÃO PODEM FORMAR TRIANGULO:')

