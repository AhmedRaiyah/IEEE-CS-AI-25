
num = int(input())

divisors = []
    
for i in range(1, num):
    if num % i == 0:
        divisors.append(i)

if sum(divisors) == num:
    print(f"{num} is a perfect number.")
else:
    print(f"{num} is NOT a perfect number.")

