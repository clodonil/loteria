from scrapy_table import Scrapy_Table

def numeros_mega():
     url="http://loterias.caixa.gov.br/wps/portal/loterias/landing/megasena/!ut/p/a1/04_Sj9CPykssy0xPLMnMz0vMAfGjzOLNDH0MPAzcDbwMPI0sDBxNXAOMwrzCjA0sjIEKIoEKnN0dPUzMfQwMDEwsjAw8XZw8XMwtfQ0MPM2I02-AAzgaENIfrh-FqsQ9wNnUwNHfxcnSwBgIDUyhCvA5EawAjxsKckMjDDI9FQE-F4ca/dl5/d5/L2dBISEvZ0FBIS9nQSEh/pw/Z7_HGK818G0K8DBC0QPVN93KQ10G1/res/id=historicoHTML/c=cacheLevelPage/=/"
     site_connect = Scrapy_Table(url)
     dados = site_connect.get_tables(0)
     return dados

def numeros_magicos():
     numeros = {}

     for linha in numeros_mega():
       if len(linha) > 3:   
          lista_numeros_sorteados = [linha[3], linha[4], linha[5], linha[6], linha[7], linha[8] ] 

          for numero_sorteado in lista_numeros_sorteados:     
               if not numero_sorteado in numeros:  
                 numeros[numero_sorteado] = 1
               else:
                 numeros[numero_sorteado] += 1

     numeros_magicos = []
     for i in sorted(numeros, key = numeros.get, reverse=True):
       numeros_magicos.append([i, numeros[i]])
       if len(numeros_magicos) == 10:
            break
   
     return numeros_magicos

def validacao(numeros):
    if not ',' in numeros:
        raise ValueError("Digite os numeros separdos por virgula(ex: 10,5,8,1,9,60).")
    numeros = numeros.split(',')
    if len(numeros) != 6:
        raise ValueError("É necessario digital 6 numeros(ex: 10,5,8,1,9,60).")

    if len(set(numeros)) < 6:
        raise ValueError("Não digite numeros repetidos.")

    numeros = [int(x) for x in numeros]
    for numero in numeros:
         if numero > 60:
            raise ValueError("Digite numeros entre 1-60.")
    return numeros

def sorteio(numeros):
     result = ['perdeu','0']
     numeros = validacao(numeros)
     for linha in numeros_mega():
       if len(linha) > 3:   
          lista_numeros_sorteados = [int(linha[3]), int(linha[4]), int(linha[5]), int(linha[6]), int(linha[7]), int(linha[8]) ] 
          if sorted(numeros) == sorted(lista_numeros_sorteados):
               result = ['ganhou', linha[12]]
     return result          
