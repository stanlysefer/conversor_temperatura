#programa para convertir una cantidad dada de grados centigrados a su equivalente en farenheit y kelvin
print("-------------------------------")
print("--VALOR DE GRADOS CENTIGRADOS--")
print("-------------------------------")

#input
c = int(input("digite el valor de grados centigrados: "))

#processing

k = ( c +273.15)
f = ( c *1.8+32)

# output

print("-----------------------------")
print("--------- RESUTADOS ---------")
print("-----------------------------")
print("Resultados grados kelvin " + str(k))
print("Resultados grados fahrenheit " + str(f))