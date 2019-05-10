#!/usr/bin/env python3
# coding=utf-8
# Description: mc Cluskey algorithm 
# feedback: melissa.escobar@utp.edu.co, UTP2019.


#if __name__ ==  __main__ :


class Minterm(object):
    def __init__(self, numDecim, numBinary, numOf1):
        self.numDecim = numDecim
        self.numBinary = numBinary
        self.numOf1 = numOf1

    def getNumDecim(self):
        return self.numDecim

    def getNumBinary(self):
         return self.numBinary
    
    def getNumOf1(self):
        return self.numOf1
    
    def __str__(self):
        return (self.numDecim, self.numBinary, self.numOf1)


#----------------------------------------------

    
  
def convertBinary(dec):
    binary = ''
    while dec // 2 != 0:
        binary = str(dec % 2) + binary
        dec = dec // 2
    return str(dec) + binary


#function to count the number of ones of a binary number
def contOnes(numBinary):
    contOfOnes = 0
    for i in numBinary:  
        if (i== '1'):
            contOfOnes +=1
    return contOfOnes

# ----------------------------------

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

#

 #-----------     main    --------------



def main():
    #Obtener el numero de minterms que se ingresarán:
    numMinterms = int(input("Ingrese por favor el numero de minterms que componen la lista: "))

    #numero máximo de bits requeridos para expresar los numeros de la lista
    numBits = int(input("Ingrese por favor el numero máximo de bits requeridos para expresar los numeros de la lista: "))

    #lista donde se guardarán los valores decimales de los minterms:
    mintermsList = []

    #Lista de minterms convertida a binario
    
    #obtener los minterms de la lista
    print ("Por favor ingrese a continuación los números decimales que componen la lista de minterms:")

    for i in range (numMinterms):
        minDecim = int(input("minterm: "))
        numBinary = ''
        lista =[]
        
        #convertir el numero decimal a binario para agregarlo al objeto y luego a la lista

        n = convertBinary(minDecim)

        #Si el tamaño del numero decimal es menor a la cantidad requerida de bits, se llenará con ceros 

        if (numBits > len(n)):
            numBinary = (numBits - len(n)) * '0' + n
        
        else:
            numBinary = n

        #calcular cuantos unos tiene el binario

        cO = contOnes(numBinary)        

        # Se agrega la cantidad de unos  a la lista auxiliar
        lista.append(cO)

        #print(cO)

        #se crea un objeto de tipo minterm y se envia su decimal, su binario y el numero de 1s que tiene el binario
        objMinterm = Minterm(minDecim, numBinary, cO )

        mintermsList.append(objMinterm)

        #for e in mintermsList:
            #print(e.__str__())



        #Ahora se ordenará la lista según la cantidad de unos

        
    listaOrdenada = sorted(mintermsList, key = lambda object : object.numOf1 )

    for e in listaOrdenada:
        print(e.__str__())

    for  i in (len(listaOrdenada)):
        j= i+1
        #Si el mintermino siguiente tiene la misma cantidad de unos mas 1 que la posicion actual,  
        # entonces hará lo que se propone en la siguiente condicion:

        for j in (len(listaOrdenada)):
            if (listaOrdenada[j].numOf1 == listaOrdenada[i].numOf1 +1):
                while (listaOrdenada[j].numOf1 == listaOrdenada[i].numOf1 +1):

                    print("Tiene "+ str(j) +"cantidad de unos")

                    #va a comparar el termino para saber si se pueden combinar(en caso de que solo tengan 
                    # una posicion distinta) y cual es la posicion que se debe cambiar por el caracter 
                    # especial, para este caso se usará '-'

                    j +=1




            else:
                j +=1




main()

