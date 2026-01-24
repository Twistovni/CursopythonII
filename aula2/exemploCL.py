class pessoa:
    def __init__(self, nome, idade, classe, periodo, ra):
        self.nome = nome
        self.idade = idade
        self.classe = classe
        self.periodo = periodo
        self.ra = ra

    def apresentar(self):
        print(f"Olá, meu nome é {self.nome} e tenho {self.idade} anos, "
              f"sou da Classe {self.classe} e estudo no período de {self.periodo}.")

    def __str__(self):
        return f"Instância do aluno: {self.nome}"

# Entrada de dados
nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
classe = input("Digite a Classe: ")
periodo = input("Digite o período: ")

# Criando o objeto (instância)
# Note que agora os argumentos batem exatamente com o __init__
aluno1 = Aluno(nome, idade, classe, periodo)

# Testando os métodos
print(aluno1)        # Aciona o __str__
aluno1.apresentar()  # Aciona o método apresentarLuiz