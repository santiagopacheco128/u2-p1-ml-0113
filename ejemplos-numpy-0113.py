import numpy as np

califas=np.array([60,70,90])
print(" ----- ej 1 califas -----")
print(califas)#imprime la lista de califas
print(type(califas))#muestra el tipo de arreglo
print(" ----- ej 0 dimensiones de un array -----")
califas=np.array([60])
print(califas)
print("Dimension : ", califas.ndim)
print(" ----- ej 1 dimensiones de un array -----")
califas=np.array([60,70,90])
print(califas)
print("Dimension : ", califas.ndim)
print(" ----- ej 2 dimensiones de un array -----")
califas=np.array([
    [60,70,90],
    [50,89,96]
])# un arreglo de 2 dimensiones es como una tabla de excel
print(califas)
print("Dimension : ", califas.ndim)
print(" ----- ej 3 dimensiones de un array -----")
califas=np.array([
    [
    [60,70,90],
    [50,89,96]
    ],
    [
    [60,70,90],
    [50,89,96]
    ]
])# un arreglo de 2 dimensiones es como una tabla de excel
print(califas)
print("Dimension : ", califas.ndim)