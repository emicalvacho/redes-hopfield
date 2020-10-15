import matplotlib.pyplot as plt
import numpy as np

# Cada elemento de la matriz representa una neurona con su carga asociada (positiva, negativa)

# Matriz general de pesos: suma de cada matriz de pesos que resulta de cada patron
# La matriz de pesos asociada a un patron se obtiene multiplicando:
# patron(vector) transpuesto * patron(vector) - identidad
def learn(pw, ph, patterns):
    identity = np.identity(pw * ph)
    generalWeightMatrix = np.zeros((pw * ph, pw * ph))
    for i in range(patterns.shape[0]):
        generalWeightMatrix += np.dot(patterns[i].reshape(pw * ph, 1), patterns[i].reshape(1,pw * ph)) - identity
    return generalWeightMatrix

# Proceso de búsqueda de patrón asociado
# Se multiplica el patron erroneo por la matriz general de pesos general
# al resultado de la misma se le aplica np.sign() 
# debido a que una neurona esta activada cuando su valor es > 0 y descativada si su valor es < 0
# el vector obtenido es la nueva entrada a la red y asi sucesivamente
# cuando desppues de varias iteraciones sin modificarse la entrada, la red se estabiliza 
# porque ha encontrado un patrón asociado a la entrada dada
def searchPattern(patternFail, mgw):
    newInfo = np.dot(patternFail, mgw)
    input = np.sign(newInfo)
    count = 0
    for i in range(10):
        if count == 3:
            print("La red encontro un patron despues de "+ str(i) + " iteraciones")
            break
        tmp = input
        newInfo = np.dot(input, mgw)
        input = np.sign(newInfo)
        if (tmp == input).all():
            count+=1

    return input