def soma(x, y)
    """ Soma x e y
    >>> soma(10, 20)
    30

    >>> soma(-10, 20)
    10

    >>> soma(1.5 , 1.5)
    3

    >>> soma('10', 10)
    Traceback (most recent call last)

    """
    assert isinstance(x, (int, float)), 'x precisa ser int ou float'
    assert isinstance(y, (int, float)), 'y precisa ser int ou float'
    return x + y

def subtrai(x, y):
    """
    >>> subtrai(2, 1)
    1

    >>> subtrai ('2', 1)
    Traceback (most recent call last)
    
    """

    assert isinstance(x, (int, float)), 'x precisa ser int ou float'
    assert isinstance(y, (int, float)), 'y precisa ser int ou float'
    
    return x - y

if __name__ == '__main__'
    import doctest
    doctest.testmod(verbose=True)