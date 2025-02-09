import math

num = int(input())

factors = []
prime_factors = []

for i in range(1, num + 1):  
    if num % i == 0:
        factors.append(i)

def is_prime(n):
    if n < 2:
        return False
    for j in range(2, int(math.sqrt(n)) + 1):
        if n % j == 0:
            return False
    return True

for i in factors:
    if is_prime(i):
        prime_factors.append(i)

print(f"Prime factors: {prime_factors}")
