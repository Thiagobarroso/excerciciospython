n1 = float(input('Digite a altura da parede: '))
n2 = float(input('Digite a largura da parede: '))

a = n1 * n2
b = a / 2

print("Sua parede tem a dimensão de {}x{} e sua área é de {}m² \n"
      " você precisará de {:.2f} litros de tinta, para pintar essa parede.".format(n1,n2,a,b))