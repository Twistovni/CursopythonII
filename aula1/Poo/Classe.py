class Pessoa:
    def __init__(self, nome, idade, cpf, cartao):
        self.nome = nome
        self.idade = idade
        self.cpf = cpf
        self.cartao = cartao
        
    def apresentar(self):
        print(f"Olá, meu nome é {self.nome} e tenho {self.idade} anos, "
              f"meu cpf é {self.cpf} e o numero do meu cartão é {self.cartao}.")


pessoa1 = Pessoa("luiz", 20, "23064887890", "123456789")
pessoa2 = Pessoa("Fernando", 38, "23068552590", "987456321")
pessoa3 = Pessoa("Barbosa", 39, "02345678910", "741852963") 


print(vars(pessoa1))      
print(pessoa2.nome)      
pessoa3.apresentar()      