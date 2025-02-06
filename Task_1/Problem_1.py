
sum = 0

while True:
    num = int(input())
    if num != -1:
        sum += num
    else:
        break

print(f"Sum: {sum}")