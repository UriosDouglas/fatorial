n = int(input('Deseja a tabuada para qual valor?'))
stop = int(input('Deseja que a tabuada vá até qual número?'))
stop = stop+1
for multiplica in range(1, stop, 1):
    resultado = multiplica*n
    print(f' {n} x {multiplica} = {resultado}')
