while True:
    try:
        n = int(input('Digite a quantidade de casos de testes que serao digitados:'))
        break
    except ValueError:
        print('EROO! digite um numero inteiro.')

coelho = 0
sapo = 0
rato = 0
soma = 0
porcento_coelho = 0
porcento_sapo = 0
porcento_rato = 0

for i in range(n):
    while True:
        try:
            cobaias = int(input('Quantidade de cobaias:'))
            break
        except ValueError:
            print('EROO! digite um numero inteiro.')

    tipo_cobaia = input('Tipo de cobaia:')

    if tipo_cobaia == 'C':
        coelho += cobaias
    elif tipo_cobaia == 'R':
        rato += cobaias
    elif tipo_cobaia == 'S':
        sapo += cobaias
    else:
        print('tipo incorreto. não será contabilizado nenhum valor.')

soma = coelho + rato + sapo
porcento_coelho = (coelho / soma) * 100
porcento_rato = (rato / soma) * 100
porcento_sapo = (sapo / soma) * 100

print('RELATORIO FINAL:')
print(f'Total: {soma} cobaias')
print(f'Total de coelhos:{coelho}')
print(f'Total de ratos: {rato}')
print(f'Total de sapos:{sapo}')
print(f'Percentual de coelhos:{porcento_coelho:.2f}')
print(f'Percentual de ratos:{porcento_rato:.2f}')
print(f'Percentual de sapos:{porcento_sapo:.2f}')
