list = []
for c in range(1, 6):
    peso = float(input('O peso da {}ª pessoa em (Kg): '.format(c)))
    list += [peso]
print('O maior peso lido foi de {}Kg'.format(max(list)))
print('O menor peso lido foi de {}Kg'.format(min(list)))
