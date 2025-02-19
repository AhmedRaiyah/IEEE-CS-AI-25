import math

# receive input as one line and convert to list
def get_numbers():
    try:
        numbers = list(map(float, input().split())) # receive input as one line and convert to list
        return numbers if numbers else [] 
    except ValueError: # to check numbersay is all numbers
        print("Invalid input! Please enter only numbers.")
        return []

def find_min(numbers):
    return min(numbers) if numbers else None  

def find_max(numbers):
    return max(numbers) if numbers else None  

def find_mean(numbers):
    sum = 0
    for num in numbers:
        sum += num

    return sum / len(numbers)

def find_mode(numbers):
    frequency = {}
    for num in numbers: # counting number of incidents of each number
        if num in frequency:
            frequency[num] += 1
        else:
            frequency[num] = 1

    max_count = max(frequency.values())  
    if max_count == 1:
        return None  # No mode if all numbers appear once

    mode = []
    for num, count in frequency.items(): # in case multiple values repated the same number of times
        if count == max_count:
            mode.append(num)

    return mode

    
def find_median(numbers):
    sorted_numbers = sorted(numbers)  # Sort a copy, not the original list
    i = len(sorted_numbers) // 2

    if len(sorted_numbers) % 2 == 0:
        return (sorted_numbers[i] + sorted_numbers[i - 1]) / 2
    else:
        return sorted_numbers[i]

    
def find_range(numbers):
    max = find_max(numbers)
    min = find_min(numbers)

    return max - min

def find_variance(numbers):
    if len(numbers) < 2:  
        return None

    mean = find_mean(numbers)
    sum = 0
    for num in numbers: 
        x = (num - mean) ** 2 
        sum += x

    return round(sum / (len(numbers) - 1), 2)

def find_STD(numbers):
    variance = find_variance(numbers)
    if variance is None:
        return None
    return round(math.sqrt(variance), 2)

def find_quariles(numbers):
    sorted_numbers = sorted(numbers)  # Sort the list first
    n = len(sorted_numbers)

    Q2 = find_median(sorted_numbers)  

    if n % 2 == 0:
        lower_half = sorted_numbers[:n // 2]
        upper_half = sorted_numbers[n // 2:]
    else:
        lower_half = sorted_numbers[:n // 2]
        upper_half = sorted_numbers[n // 2 + 1:]

    Q1 = find_median(lower_half)
    Q3 = find_median(upper_half)

    return Q1, Q2, Q3


def find_IQR(numbers):
    Q1, _, Q3 = list(find_quariles(numbers))
    IQR = Q3 - Q1

    return IQR

def control_function(): # to run and print all previous numbers
    numbers = get_numbers()

    print(f"\nMinimum: {find_min(numbers)}")
    print(f"Maximum: {find_max(numbers)}")
    print(f"Mean: {find_mean(numbers)}")
    print(f"Mode: {find_mode(numbers)}")
    print(f"Median: {find_median(numbers)}")
    print(f"Range: {find_range(numbers)}")
    print(f"Variance: {find_variance(numbers)}")
    print(f"Standard Deviation: {find_STD(numbers)}")
    print(f"Quartiles: {find_quariles(numbers)}")
    print(f"IQR: {find_IQR(numbers)}")


# Program
control_function()