import math

x1 = int(input("Coordenada x1 de P1: "))
y1 = int(input("Coordenada y1 de P1: "))
x2 = int(input("Coordenada x2 de P1: "))
y2 = int(input("Coordenada y2 de P1: "))

d = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

print(" Distância entre P1 e P2 é: ", d)
