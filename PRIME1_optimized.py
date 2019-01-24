def sieve(n):
    is_prime = [True] * (n+1)
    is_prime[1] = False
    for i in range(2, n+1):
        if(is_prime[i]):
            for j in range(2*i, n+1, i):
                is_prime[j] = False
    return is_prime

n = int(input())
is_prime = sieve(10000000)
for i in range(n):
    k = int(input())
    if(is_prime[k]):
        print("YES")
    else:
        print("NO")