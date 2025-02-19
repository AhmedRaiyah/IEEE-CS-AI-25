
n = int(input())
arr = map(int, input().split())


unique_times = sorted(set(arr))

print(unique_times[len(unique_times) - 2])