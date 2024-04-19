import math

def calcular_circunferencia(radio):
    pi = round(math.pi, 6)
    circunferencia = 2 * pi * radio
    return circunferencia

def imprimir_resultado(radio, circunferencia):
    print(f"Para un radio de {radio}, la circunferencia es: {circunferencia}")

# Calcular la circunferencia para diferentes radios
radio_1 = 3
circunferencia_1 = calcular_circunferencia(radio_1)
imprimir_resultado(radio_1, circunferencia_1)

radio_2 = 8
circunferencia_2 = calcular_circunferencia(radio_2)
imprimir_resultado(radio_2, circunferencia_2)

radio_3 = 10
circunferencia_3 = calcular_circunferencia(radio_3)
imprimir_resultado(radio_3, circunferencia_3)
