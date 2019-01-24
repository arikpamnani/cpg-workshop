def sieve(n):
    is_prime = [True] * (n+1)
    is_prime[1] = False
    spf = [-1] * (n+1)
    for i in range(2, n+1):
        if(is_prime[i]):
            spf[i] = i
            for j in range(2*i, n+1, i):
                is_prime[j] = False
                if(spf[j] == -1):
                    spf[j] = i
    return spf

spf = sieve(1000000)
t = int(input())
for i in range(t):
    n = int(input())
    print(spf[n])