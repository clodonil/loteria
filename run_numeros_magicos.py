import loteria

numeros = loteria.numeros_magicos()

print("Os 10 numeros mais sorteados na mega sena:")
for numero in numeros:
    print(numeros.index(numero)+1,"-->", numero[0],"saiu", numero[1], "vezes")