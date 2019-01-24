def gcd(A, B):
    if(B == 0):
        return A
    else:
        return gcd(B, A%B)

n = int(input())
m = int(input())
z = int(input())
lcm = (n*m)//gcd(n, m)
print(z//lcm)


        