print('*** TABUADA SIMPLES ***')
divisor = int(input('Informe o divisor '))

# para criar o loop usaremos a função for e range
for i in range(10):
    print('{} / {} = {:.2f}'.format(i*divisor, divisor, i))
