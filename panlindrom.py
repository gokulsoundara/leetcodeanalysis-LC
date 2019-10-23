t = {}
def palind(n):
    if n in t:
        return t[n]
    if n ==1 or n==2:
        res = 1
    else:
        res = palind(n-1) + palind(n-2)
    t[n] = res
    return res

for i in range(1,10):
    print(palind(i))