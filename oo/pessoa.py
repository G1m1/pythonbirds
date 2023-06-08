class Pessoa():
    def __init__(self, * filhos, nome=None,idade=35): # atributo dado| instância da classe.
        self.nome = nome
        self.idade = idade
        self.filhos = list(filhos)  # *filhos = recebe uma quantidade variavel de parâmetros | estou criando uma lista, se liga, lista aceita qualquer tipo de variavel.

    def cumprimentar(self): # método
        return 'ola'

if __name__ == '__main__':
    renzo = Pessoa(nome='Renzo') # pai do luciano
    luciano = Pessoa(renzo, nome='Luciano') # filho do renzo

    print(luciano.cumprimentar())
    print()
    print(luciano.nome)
    print(luciano.idade)
    print()
    print()
    for filho in luciano.filhos:
        print(filho.nome)





