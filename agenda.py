def main():
        #instrução
    print("Bem vindo(a) a sua agenda, observe abaixo os comandos com cuidado e escolha o de sua neccessidade.")

    def cmd():
                #comandos
        print('1 - Adicionar nome e data de aniversário;\n'
              '2 - Listar todos os nomes;\n'
              '3 - Listar todas as datas de aniversário;\n'
              '4 - Apagar nome;\n'
              '5 - Apagar todos os nomes ;\n'
              '6 - Apagar data;\n'
              '7 - Apagar todas as datas;\n'
              '8 - Mostrar agenda')

            #vetores
        nomes = []
        datasAniversario = []
        agenda = [nomes, datasAniversario]


        while True:
                 cmd = int(input("Insira o comando:"))    #entrada de dados para os comandos


                 if cmd == 1:
                    nome = input("Digite um nome:")
                    data = input("Agore digite a respectiva data de aniversário:")
                    nomes.append(nome)
                    datasAniversario.append(data)


                 if cmd == 2:
                     print(nomes)

                 if cmd == 3:
                    print(datasAniversario)

                 if cmd == 4:
                    remover = input("Digite o nome que deseja remover:")
                    nomes.remove(remover)


                 if cmd == 5:
                     nomes.clear()


                 if cmd == 6:
                     excluir = input("Digite a data que deseja remover:")
                     datasAniversario.remove(excluir)



                 if cmd == 7:
                     datasAniversario.clear()

                 if cmd == 8:
                     print(agenda)


    return cmd()

main()



