from typing import List, Union, Tuple, Dict, Callable

# Primitivos
numero: int = 10
flutuate: float = 10.8
bolleano: bool = True
string: str = 'Ola mundo'

# Sequencias
lista: List[int] = [1, 2, 3]
lista_str_int: List[Union[int, str]] = ['Bruno', 15]

tupla: Tuple[int, int, int, str] = (1, 2, 3, 'Bruno')

#Dicionarios e conjuntos
pessoa: Dict[Union[str, int]] = {'nome':'bruno', 'sobrenome': 'Volpe', 'idade':25}

pessoa2: Dict[str, n] = {'nome':'bruno', 'sobrenome': 'Volpe', 'idade':25}

MeuDict = Dict[str, int, List[str], Lista[int]]  #Alias
pessoa3: MeuDict = {'nome':'bruno', 'sobrenome': 'Volpe', 'idade':25}

# Meu outro tipo
UserId = NewTIpe('UserId', int)
user_id = UserId(1234456)

#Funcoes
def retorna_funcao(funcao: Callable[[int, int], int]) -> Callable
    return funcao

def fala_oi():
    print('Oi')

def soma(x: int, y: int) -> int:
    return x + y

retorna_funcao(fala_oi)()
retorna_funcao(soma)(10, 20)

#Classes
class Pessoa():
    def __init__(self, nome: str, idade: int) -> None
        self.nome: str = nome
        self.idade: int = idade
    
    def fala() -> None
        print(self.nome, 'Esta falando... ')