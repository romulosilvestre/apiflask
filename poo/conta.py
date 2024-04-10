#a classe é um conjunto de objetos
class Conta:
    #o que uma classe tem?
  
    def __init__(self,descricao,valor,id=None):
        self.id = id
        self.descricao = descricao
        self.valor = valor

    """      
       construtor
       atributos
       funções (métodos)
         get
         set
         workers (trabalho)
        objetos
    """