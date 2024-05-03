n = int(input())
c = 1

while(c<=n):
    for i in range(1, n+1):
        print(f"{c}/{i}")
    c+=1