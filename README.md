__Exercício sobre loteria__
=========================

* __1. Faça um programa que mostra os 10 números mais sorteados na mega-sena.__
* __2. Faça um gamer: O usuário deve entrar com 6 números e o programa deve retornar se os números informados já foi sorteado em alguma mega-sena e qual o valor do prêmio.__

```bash
git clone git@github.com:clodonil/loteria.git
```
Instalação das dependências:

```bash
pip install -r requirements.txt
```

Executando testes unitários:

```python
pytest -v
=============================================================== test session starts ================================================================
platform linux -- Python 3.8.10, pytest-6.2.5, py-1.11.0, pluggy-1.0.0 -- /mnt/c/Users/clodo/Documents/WorkSpace/loteria/venv/bin/python3
cachedir: .pytest_cache
rootdir: /mnt/c/Users/clodo/Documents/WorkSpace/loteria
collected 8 items

test_game.py::test_ganhou PASSED                                                                                                             [ 12%]
test_game.py::test_perdeu PASSED                                                                                                             [ 25%]
test_game.py::test_numeros_sem_virgula PASSED                                                                                                [ 37%]
test_game.py::test_numeros_repetidos PASSED                                                                                                  [ 50%]
test_game.py::test_menos_de_6_numeros PASSED                                                                                                 [ 62%]
test_game.py::test_mais_de_6_numeros PASSED                                                                                                  [ 75%]
test_game.py::test_numeros_maiores_que_60 PASSED                                                                                             [ 87%]
test_numeros_magicos.py::test_os_10_numeros_mais_sorteados_na_mega PASSED                                                                    [100%]

================================================================ 8 passed in 13.42s ================================================================
````

Executando o programa para obter os 10 números mais sorteados na mega-sena:

```python
python run_numeros_magicos.py
Os 10 numeros mais sorteados na mega sena:
1 --> 053 saiu 279 vezes
2 --> 010 saiu 276 vezes
3 --> 005 saiu 267 vezes
4 --> 042 saiu 267 vezes
5 --> 004 saiu 264 vezes
6 --> 037 saiu 264 vezes
7 --> 033 saiu 263 vezes
8 --> 023 saiu 261 vezes
9 --> 030 saiu 260 vezes
10 --> 027 saiu 260 vezes
```

Executando o gamer:

```bash
python run_game.py
Game da Mega-Sena (digite sair para finalizar)
Digite os 6 numeros:1,8,14,28,33,43
Resultado: Você ganhou o valor de 18.661.679,61
Digite os 6 numeros:sair
Fim do game.
```