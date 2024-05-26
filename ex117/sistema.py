from ex117.lib.interfaces import *
from ex117.lib.arquivos import *
from time import sleep

arq = 'cursoemvideo.txt'
if not arquivoExiste(arq):
    criarArquivo(arq)

# Programa Principal
while True:
    resposta = menu(['Listar usuários cadastrados', 'Cadastrar novo usuário', 'Sair do sistema'])
    if resposta == 1:
        # Opção de listar o conteúdo do arquivo
        lerArquivo(arq)
    elif resposta == 2:
        cabecalho('Opção 2')
    elif resposta == 3:
        cabecalho('Saindo do sistema... Até logo!')
        break
    else:
        print('\033[31mErro! Entrada inválida. Escolha uma opção correta\033[m')
    sleep(2)
