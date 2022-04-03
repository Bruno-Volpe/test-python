"""
1 - Receber um numero inteiro
2 - Saber se o numero eh multiplo de 3 e 5
    Bacon com Ovos
3- Saber se um numeor eh multiplo somento de 3
    Bacon
4- Saber se um mutiplo eh mutiplo somente de 5
    Ovos
5- Saber se o numero nao eh multiplo de 3 e 5
    Passa fome
"""


def bacon_com_ovos(n):
    assert isinstance(n, int), 'n deve ser int'

    if n % 3 == 0 and n % 5 == 0:
        return 'Bacon com Ovos'

    elif n % 3 == 0:
        return 'Bacon'

    elif n % 5 == 0:
        return 'Ovos'

    else:
        return 'Passar fome!'
