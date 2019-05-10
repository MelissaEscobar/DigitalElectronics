

#compare two binary strings, check where there is one difference
def compBinary(s1,s2):
    count = 0
    pos = 0
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            count+=1
            pos = i
    if count == 1:
        return True, pos
    else:
        return False, None

def cambiarDiferencia(s1, s2):

    compStrings = compBinary(s1, s2)

    if (compStrings[0] == True):

        arrayS1 = []

        #Agrego cada char del string a una lista, para hacer el cambio respectivo segun el  indice
        #en el que cambian las dos cadenas
        for i in s1:
            arrayS1.append(i)

        #Se hace el cambio del caracter por '-'
        arrayS1[compStrings[1]] = '-'

        #lo  regreso nuevamente como una cadena
        str1 = ''.join(str(e) for e in arrayS1)

        return str1

    else :
        return False 

#Test:

print(cambiarDiferencia( '0100', '0000'))

print(cambiarDiferencia( '0110', '0000'))