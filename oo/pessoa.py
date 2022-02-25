class Pessoa:
    def cumprimentar(self):
        return f'Olá  {id(self)}'





if __name__ == '__main__':
    p = Pessoa()
    print(Pessoa.cumprimentar(p))
    print(id(p))
    print(p.cumprimentar())


f"""
Criada a classe pessoa, vamos criar um metodo, o qual é uma função dentro 
da classe.

class Pessoa:
    def cumprimentar(self):  Este é o corpo do metódo ou "função"
    return  'Olá '                     return é um mecanismo o qual retorna operação realizada dentro da função.
    
if __name__ == '__main__':
    p = Pessoa()                                    p = Pessoa() - p é uma instancia da classe. logo, ele pode usar todos os metódos dela.
    print(Pessao.cumprimentar(p))    Não é muito usual, mas seria o mais correto modelo de impressão da instacia.
    print(p.cumprimentar())                Esse é o modelo mais usado entre os pythonistas.   

"""






















