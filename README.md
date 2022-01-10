__Exercício sobre loteria__
=========================

* 1. Faça um programa que mostra os 10 números mais sorteados na mega-sena.
* 2. Faça um gamer: O usuário deve entrar com 6 números e o programa deve retornar se os números informados já foram sorteados em alguma mega-sena e qual o valor do prêmio.

```bash
git clone git@github.com:clodonil/loteria.git
```
Instalação da dependencias:

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

Executando o programa para executar os 10 números mais sorteados na mega-sena

```python
python run_numeros_magicos.py
```

Executando o gamer:
```python
python run_gamer.py
```