x1 = int(input("Digite o valor do x1: "))
x2 = int(input("Digite o valor de x2: "))
x3 = int(input("Digite o valor de x3: "))
if x1 > x2 > x3:
    print(" O maior valor é: ", x1, "e o menor número é", x3)
if x2 > x3 > x1:
    print(" O maior valor é: ", x2, "e o menor número é", x1)
if x3 > x1 > x2:
    print(" O maior valor é: ", x3, "e o menor número é", x2)
if x1 > x3 > x2:
    print(" O maior valor é: ", x1, "e o menor número é", x2)
if x2 > x1 > x3:
    print(" O maior valor é: ", x2, "e o menor número é", x3)
if x3 > x2 > x1:
    print(" O maior valor é: ", x3, "e o menor número é", x1)
