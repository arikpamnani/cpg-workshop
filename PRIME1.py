def is_prime(k):
	if(k < 2):
		return False
	i = 2
	while(i*i<=k):
		if(k % i == 0):
			return False
		i += 1
	return True

n = int(input())

for i in range(n):
    k = int(input())
    if(is_prime(k)):
        print("YES")
    else:
        print("NO")