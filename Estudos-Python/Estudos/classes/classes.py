# Classes e Programação orientada a Objetos

class Vendedor():
    def __init__(self, nome):
        self.nome = nome
    
    def vendeu(self,vendas):
        self.vendas = vendas
    
    def meta(self,meta):
        if self.vendas >= meta:
            print(self.nome, "Bateu A meta Com o total de:", self.vendas, "Vendas")
        else:
            print(self.nome, "Não Bateu a meta de: ", meta, "Vendas")

vendedores = []
for x in range(2):
    vendedor1 = Vendedor(input("Nome: "))
    vendedor1.vendeu(int(input("Vendas: ")))
    vendedor1.meta(int(input("Meta: ")))
    vendedores.append(vendedor1)

print("Tivemos o total de: ", len(vendedores), "Vendedores")