from statistics import mean
nota1 = float(input('Digite a 1ª nota do aluno '))
nota2 = float(input('Digite a 2ª nota do aluno '))
media = mean([nota1, nota2])
if media < 5:
    print('Sua média foi {:.1f} e está abaixo da média [5.00] (\033[1;31mREPROVADO!\033[m)'.format(media))
elif (media >= 5) and (media <= 6.9):
    print('Sua média foi {:.1f} e você está de (\033[1;33mRECUPERAÇÃO!\033[m)'.format(media))
else:
    print('Sua média foi {:.1f} e você está (\033[1;34mAPROVADO!\033[m)'.format(media))
    if media == 10:
        print('Parabéns, você é o melhor!')