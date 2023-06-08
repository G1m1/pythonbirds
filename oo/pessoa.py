class Pessoa():
    olhos = 2 # atributo de classe | significa que o valor vai único para todos os objetos. Otimiza seu tempo.

    def __init__(self, * filhos, nome=None,idade=35): # atributo dado| instância da classe.
        self.nome = nome
        self.idade = idade
        self.filhos = list(filhos)  # *filhos = recebe uma quantidade variavel de parâmetros | estou criando uma lista, se liga, lista aceita qualquer tipo de variavel.

    def cumprimentar(self): # método
        return 'Ola, bom dia !'

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

    luciano.sobrenome = 'Ramalho' # atributo Dinâmico - vc não esta instanciando, isso significa que os outros objetos não partilharam desse atributo.
    print(luciano.sobrenome)             # apenas o que vc acabou de fazer.
    print(luciano.__dict__)                   # o atributo especial dict te fala todos os atributos de um objeto do tipo classe
    print(renzo.__dict__)                       # luciano e renzo são diferentes.
    print()
    del luciano.filhos # não é muito usual, mas é possivel excluir um atributo, apenas para conhecimento
    luciano.olhos = 1 # vc pode mudar o atributo de classe so para um objeto, sem alterar os demais.
    print()
    print()
    print(luciano.olhos)
    print(Pessoa.olhos) # olha que legal, por ser um atributo da classe, ele também consegue ser acessado via Classe.
    print()
    print()
    print(f'{luciano.cumprimentar()} sou o {luciano.nome} tenho {luciano.idade} anos de idade.')
    print()
    print(luciano.olhos,Pessoa.olhos) # o objeto mudou a quantidade de olhos, mas a classe não foi alterada o  seu valor.




