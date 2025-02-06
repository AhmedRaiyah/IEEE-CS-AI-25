import math

num = int(input("Enter a positive integer: "))

factors = []
prime_factors = []

# Find all factors of the given number
for i in range(1, num + 1):  # Include num itself as a factor
    if num % i == 0:
        factors.append(i)

# Function to check if a number is prime
def is_prime(n):
    if n < 2:
        return False
    for j in range(2, int(math.sqrt(n)) + 1):
        if n % j == 0:
            return False
    return True

# Check which factors are prime
for i in factors:
    if is_prime(i):
        prime_factors.append(i)

# Print results
print("Prime factors:", prime_factors)
