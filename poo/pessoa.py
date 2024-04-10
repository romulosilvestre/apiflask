class Pessoa:
    """
      Na classe Pessoa defina três atributos

      nome,idade,cpf=None    
    """
    def __init__(self,nome,idade,cpf=None):
        self.nome = nome
        self.idade = idade
        self.cpf = cpf


if __name__ == "__main__":
    pessoa = Pessoa()
    pessoa.nome = "Edir Mais Cedo."