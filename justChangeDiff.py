def cambiarDiferencia(s1, s2, diff): #diff es la posicion donde esta la dferencia
    
    arrayS1 = []
    #Agrego cada char del string a una lista, para hacer el cambio respectivo segun el  indice
    #en el que cambian las dos cadenas
    for i in s1:
        arrayS1.append(i)
    #Se hace el cambio del caracter por '-'
    arrayS1[diff] = '-'
    #lo  regreso nuevamente como una cadena
    str1 = ''.join(str(e) for e in arrayS1)
 
    return str1

print(cambiarDiferencia('000100', '000000', 3))