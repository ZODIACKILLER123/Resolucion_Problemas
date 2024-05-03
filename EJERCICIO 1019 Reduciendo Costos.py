for i in range(int(input())):
    x, y, z = map(int, input().split())
    if (x<=y and x >=z) or (x>=y and x<=z):
        print(f"Case {i+1}: {x}" )
    elif (y<=x and y >=z) or (y>=x and y<=z):
        print(f"Case {i+1}: {y}" )
    elif (z<=y and z >=x) or (z>=y and z<=x):
        print(f"Case {i+1}: {z}" )