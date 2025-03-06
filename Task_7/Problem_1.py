
data = tuple(map(int, input().split()))
frequency = {}

for num in data:
    if num in frequency:
        frequency[num] += 1  
    else:
        frequency[num] = 1 

probability = {key: value / len(data) for key, value in frequency.items()}

print(probability)