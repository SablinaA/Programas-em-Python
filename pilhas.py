class Pilha():
    def __init__(self):
        self.p = []


    def exibirPilha(self):
        return self.p

    def adicionarElemento(self, elemento):
        self.p.append(elemento)


    def inverter(self):
        self.p = self.p[::-1]


print("    Comandos: \n"
      "1- Adicionar elemento;  \n"
      "2- Exibir pilha; \n"
      "3- Inverter pilha;")

pilha = Pilha()

while True:

    opcao = int(input("O que deseja fazer:"))


    if opcao == 1:
        while True:
            adicionar = input("Digite o elemento para inserir:")
            if adicionar == "sair":
                break
            pilha.adicionarElemento(adicionar)

    if opcao == 2:
        pilha.exibirPilha()


    if opcao == 3:
        print(pilha.inverter())