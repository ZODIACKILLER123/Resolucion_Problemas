
h, m, s = map(int, input().split())
s+=1
if (s > 59):
    m+=1
    s = 0
    if m > 59:
        m = 0
        h+=1
        if h > 23:
            h = 0
            print("{:02d}:{:02d}:{:02d}".format(h, m, s))
        else:
            print("{:02d}:{:02d}:{:02d}".format(h, m, s))
    else:
        print("{:02d}:{:02d}:{:02d}".format(h, m, s))
else:
    print("{:02d}:{:02d}:{:02d}".format(h, m, s))

