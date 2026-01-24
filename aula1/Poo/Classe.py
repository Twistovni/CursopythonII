class Pessoa:
    def __init__(self, nome, idade, cpf, cartao):
        self.nome = nome
        self.idade = idade
        self.pet = pet
        self.cpf = cpf
        self.cartao = cartao
        
    def apresentar(self):
        print(f"Olá, meu nome é {self.nome} e tenho {self.idade} anos, "
              f"meu cpf é {self.cpf} e o numero do meu cartão é {self.cartao}.")


pessoa1 = Pessoa("luiz", 20, "23064887890", "123456789")
pessoa2 = Pessoa("Fernando", 38, "23068552590", "987456321")
pessoa3 = Pessoa("Barbosa", 39, "02345678910", "741852963") 
pessoa4 = Pessoa("santos", 39, "02345679010", "741852243") 


print(vars(pessoa1))      
print(pessoa2.nome)


nome = input ("Digite o nome do seu objeto:")
idade = int(input("Digite a idade do seu objeto:"))
pet = input ("Digite qual pet ele tem")
if (pet == "Sim"):
    animal = input("Digite qual pet ele tem")
Else:
    animal = "Não"

pessoa5 = Pessoa(nome,idade)      
pessoa5.apresentar()      