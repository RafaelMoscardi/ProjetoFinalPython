from lib import interface
from lib import arquivo
from time import sleep

arq = 'cursoemvideo.txt'

if not arquivo.arquivoExiste(arq):
    arquivo.criarArquivo(arq)

while True:
    resposta = interface.menu(['Ver pessoas cadastradas', 'Cadastrar nova Pessoa', 'Sair do Sistema'])
    if resposta == 1:
        # Opção de listar o conteúdo de um arquivo.
        arquivo.lerArquivo(arq)
    elif resposta == 2:
        # Opção de cadastrar uma nova pessoa.
        interface.cabeçalho('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = interface.leiaInt('Idade: ')
        arquivo.cadastrar(arq, nome, idade)
    elif resposta == 3:
        # Opção de sair do sistema.
        interface.cabeçalho('Saindo do sistema... Até logo!')
        break
    else:
        # Digitou uma opção errada no menu.
        print('\033[31mERRO! digite uma opção válida!\033[m')
    sleep(1.3)
