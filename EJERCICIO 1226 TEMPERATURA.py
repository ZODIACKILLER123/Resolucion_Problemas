t = int(input())
if (t > 30):
    print("hace calor")
    if t>=100:
        print("hierve")
elif (t < 10):
    print("hace frio")
    if (t <= 0):
        print("se congela")
elif (t>=10 and t<=30):
    print("esta bien")