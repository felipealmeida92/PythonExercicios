from urllib import request
from urllib import error


try:
    site = request.urlopen('https://www.google.com/')
except error.URLError:
    print('O site Google não está acessível no momento.')
else:
    print('Consegui acessar o site Google com sucesso!')

