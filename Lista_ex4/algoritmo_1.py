A = int(input("Digite o primeiro valor: "))
B = int(input("Digite o segundo valor: "))
C = int(input("Digite o terceiro valor: "))

if(A > 0 and B > 0 and C > 0):
     maior = A

if (B > maior):
        maior = B
if (C > maior):
        maior = C

print('Maior: ',maior)

menor = A

if (B < menor):
        menor = B
if (C < menor):
        menor = C

print('Menor: ',menor)

media = round((A+B+C)/3)

print(media)