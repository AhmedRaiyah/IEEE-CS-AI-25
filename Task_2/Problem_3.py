
N = int(input())
nums_list = []

for num_of_commands in range(N):
    command = input().split()

    if command[0].lower() == "insert":
        nums_list.insert(int(command[1]), int(command[2]))
    elif command[0].lower() == "print":
        print(nums_list)
    elif command[0].lower() == "remove":
        nums_list.remove(int(command[1]))
    elif command[0].lower() == "append":
        nums_list.append(int(command[1]))
    elif command[0].lower() == "sort":
        nums_list.sort()
    elif command[0].lower() == "pop":
        nums_list.pop()
    elif command[0].lower() == "reverse":
        nums_list.reverse()
