n1 = float(input('Valor do produto: '))

soma = (70/100) * n1
desconto = n1 - soma

print('O valor do produto é de R${}\n'
      'O valor do produto com 5% de desconto R${}'.format(n1,desconto))
