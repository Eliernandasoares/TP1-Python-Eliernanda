texto= "Olá, laço for"
for item in texto:
    print ("caractere: ", item)



#En Python al utilizar la funcion range (start, stop), el valor de stop NO está incluido en el rango. Por lo tanto, para iterar entre 1 y 10 (con el 10 incluido), debo usar range (1,11)
for numero in range (1,11):
    print ("Número do intervalo ", str (numero))
