from musica import Musica

colecao = Musica()

nome = input("Insira o nome: ")
autor = input("Insira o autor: ")
genero = input("Insira o genero: ")

colecao.save(nome, autor, genero)