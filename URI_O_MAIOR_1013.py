import math
ValorI = input().split(" ")
a ,b, c = ValorI 

Maior = (int(a) + int(b) + abs(int(a) - int(b)))/2
resultado = (int(Maior) + int(c) + abs(int(Maior) - int(c)))/2
print ("%d eh o maior" %resultado)
