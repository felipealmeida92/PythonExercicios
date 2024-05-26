from math import radians, sin, cos, tan
ang = float(input('Digite um ângulo qualquer '))
seno = sin(radians(ang))
cos = cos(radians(ang))
tan = tan(radians(ang))
print('O ângulo de {:.2f} tem o seno é {:.2f} o cosseno é {:.2f} e a tangente é {:.2f} '.format(ang, seno, cos, tan))