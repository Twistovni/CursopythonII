class Animal:
    def __init__(self, nome, idade, peso, raca, especie):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.raca = raca
        self.especie = especie
        
    def emitir_som(self):
        return "Som genérico"

    def __str__(self):
        return f"{self.nome} ({self.especie}) - Raça: {self.raca}"

class Cachorro(Animal):
    def emitir_som(self):
        return "Au Au! (Late)"

class Gato(Animal):
    def emitir_som(self):
        return "Miau! (Mia)"

class Porco(Animal):
    def emitir_som(self):
        return "Oinc Oinc! (Grunhe)"

# Instanciando os objetos
# Note que no Porco corrigi a falta de vírgula entre "Sus" e "Suino"
cachorro1 = Cachorro("Pingo", 2, "10Kg", "Shitsu", "Canino")
gato1 = Gato("Ton", 4, "6Kg", "Vira-Lata", "Felino")
porco1 = Porco("Baby", 7, "32Kg", "Sus", "Suino")

# Testando a melhoria
animais = [cachorro1, gato1, porco1]

for animal in animais:
    print(f"{animal} faz: {animal.emitir_som()}")