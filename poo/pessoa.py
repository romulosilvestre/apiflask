class Pessoa:
    
    def __init__(self,nome,idade,cpf=None):
        self.nome = nome
        self.idade = idade
        self.cpf = cpf


if __name__ == "__main__":
    pessoa = Pessoa()
    pessoa.nome = "Joaquim da Silva"