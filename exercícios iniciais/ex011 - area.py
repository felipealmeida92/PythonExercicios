l = float(input('Qual a largura da sua parede? '))
a = float(input('Qual a altura da sua parede? '))
m2 = l * a
t = m2 / 2
print('A área da sua parede é de {:.2f} m2 e será necessário {:.2f} l de tinta para pintá-la'.format(m2,t))