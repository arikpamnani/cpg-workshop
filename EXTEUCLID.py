def egcd(A, B):
    """return (g, x, y) such that a*x + b*y = g = gcd(x, y)"""
    if(B == 0):
        return (A, 1, 0)
    else:
        g, x, y = egcd(B, A%B)
        return (g, y, x - (A//B) * y)

a = int(input())
b = int(input())
c = int(input())
(g, x, y) = egcd(a, b)

if(c%g!=0):
    print("NO")
else:
    print("YES")
    print(x*(c//g))
    print(y*(c//g))
