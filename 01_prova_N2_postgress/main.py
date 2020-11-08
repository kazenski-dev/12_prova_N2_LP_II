from operacao_banco import Operacoes

operar = Operacoes()
#id_musica = int(input("Insira o identificador: "))
nome = str(input("Digite o nome da musica: "))
autor = str(input("Digite o autor: "))
genero = str(input("Digite o genero da musica: "))

operar.salvar(nome, autor, genero)
operar.buscar()
"""
while True:
    opcao = input("Digite 1 para inserir novamente ou 0 para sair:")
    if opcao == "1":
        nome = str(input("Digite o nome da musica: "))
        autor = str(input("Digite o autor: "))
        genero = str(input("Digite o genero da musica: "))
        operar.salvar(nome, autor, genero)
        operar.buscar()
    else: 
        break
"""