n, k = map(int, input().split())
number = 0
count = 0
lista = []

while n!=0:
    digito = n%10
    lista.insert(0, digito)
    n//=10
    count+=1

for i in range(len(lista)):
    if i == k-1:
        number = lista[i]

print(count, number)