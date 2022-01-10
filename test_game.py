import loteria
import pytest


def test_ganhou():
    numeros = '9,37,39,41,43,49' 
    result = loteria.sorteio(numeros) # ['ganhou', 'valor']

    assert result[0] == 'ganhou' and result[1] == '2.307.162,23'

def test_perdeu():
    numeros = '9,37,39,41,43,1'
    result = loteria.sorteio(numeros) # ['perdeu', '0']

    assert result[0] == 'perdeu' and result[1] == '0'

def test_numeros_sem_virgula():
    numeros = '937394143;1'
    with pytest.raises(ValueError) as error:
        loteria.sorteio(numeros)
    assert str(error.value) == "Digite os numeros separdos por virgula(ex: 10,5,8,1,9,60)."    

def test_numeros_repetidos():
    numeros = '5,6,7,8,9,5'
    with pytest.raises(ValueError) as error:
        loteria.sorteio(numeros)
    assert str(error.value) == "Não digite numeros repetidos."

def test_menos_de_6_numeros():
    numeros = '5,6,7,8,9'
    with pytest.raises(ValueError) as error:
        loteria.sorteio(numeros)
    assert str(error.value) == "É necessario digital 6 numeros(ex: 10,5,8,1,9,60)."        

def test_mais_de_6_numeros():
    numeros = '5,6,7,8,9,50,51'
    with pytest.raises(ValueError) as error:
        loteria.sorteio(numeros)
    assert str(error.value) == "É necessario digital 6 numeros(ex: 10,5,8,1,9,60)." 

def test_numeros_maiores_que_60():
    numeros = '5,6,7,8,9,61'
    with pytest.raises(ValueError) as error:
        loteria.sorteio(numeros)
    assert str(error.value) == "Digite numeros entre 1-60." 
