import os
from io import open_code

nome = str(input("Digite seu nome: "))
n1 = float(input("Digite nota av1: "))
n2 = float(input("Digite nota av2: "))

media = (n1 + n2) / 2
print("A media do aluno: {:.1f}".format(media))
print("--------------------------------------")

opc = (0);

while opc != (2):
    print("Digite 1 para repetir: ")
    print("Digite 2 para sair: ")
    opc = int(input("Digite a opção desejada: "))

    if opc == (1):
        nome = str(input("Digite seu nome: "))
        n1 = float(input("Digite sua nota av1: "))
        n2 = float(input("Digite sua nota av2: "))

        media = (n1 + n2) / 2

        print("A media do aluno: {:.1f}".format(media))

    elif opc == (2):
        print("Programa finalizado!")

    else:
        print("Opção invalida!")


        
manipulador = open('bancoDados.txt','r')
backup = manipulador.readlines()

manipulador = open('bancoDados.txt','w')
manipulador.writelines(backup)
manipulador.write('Aluno: ')
manipulador.write(nome)
manipulador.write('\n')
manipulador.write('Tem a media: ')
manipulador.write(format(media))
manipulador.writelines('\n')
manipulador.close()

manipulador = open('bancoDados.txt')
print(os.path.abspath(manipulador.name))
print(manipulador)

manipulador = open('bancoDados.txt')
print('Nome do manipulador:', manipulador.name)
print('Modo do manipulador:', manipulador.mode)
print('Manipulador fechado?', manipulador.closed)

manipulador.close()

print('Manipulador fechado?', manipulador.closed)

manipulador = open('bancoDados.txt', 'r')
print('\nMetodo read():\n')
print(manipulador.read())
print('\nTipo do conteudo:\n', type(manipulador))
print(repr(manipulador))

manipulador.seek(0)

print('\nMetodo readline():\n')
print(manipulador.readline())
print(manipulador.readline())
print('\nTipo do conteudo:\n', type(manipulador))
print(repr(manipulador))

manipulador.seek(0)

print('\nMetodo readlines:\n')
print(manipulador.readlines())
print('\nTipo do conteudo:', type(manipulador))
print(repr(manipulador))

manipulador.seek(0)
print("---------------------------------------")
manipulador = open('bancoDados.txt')
for linha in manipulador:
    print(repr(linha))

manipulador.close()
