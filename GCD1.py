def gcd(A, B):
    if(B == 0):
        return A
    else:
        return gcd(B, A%B)

A = int(input())
B = int(input())
C = int(input())
print(gcd(gcd(A, B), C))

        