import loteria

def test_os_10_numeros_mais_sorteados_na_mega():
    numero = loteria.numeros_magicos()
    # [ ['53',257], ['numero','quantidade']]
    
    assert numero[0][0] == '053' and numero[0][1] == 279 
    assert numero[1][0] == '010' and numero[1][1] == 276
    assert numero[2][0] == '005' and numero[2][1] == 267 
    assert numero[3][0] == '042' and numero[3][1] == 267  
    assert numero[4][0] == '004' and numero[4][1] == 264 
    assert numero[5][0] == '037' and numero[5][1] == 264 
    assert numero[6][0] == '033' and numero[6][1] == 263
    assert numero[7][0] == '023' and numero[7][1] == 261 
    assert numero[8][0] == '030' and numero[8][1] == 260 
    assert numero[9][0] == '027' and numero[9][1] == 260 
 
