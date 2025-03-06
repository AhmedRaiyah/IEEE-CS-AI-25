
event_A = tuple(int(x) for x in input("Event A: ").split() if x in ('0','1'))
event_B = tuple(int(x) for x in input("Event B: ").split() if x in ('0','1'))

# Probability of A
occured = 0
for num in event_A:
    if num == 1:
        occured += 1

A_probability = occured / len(event_A)

# probability of AnB
both_occur = 0
i = 0
for num in event_B:
    if num == 1 and event_A[i] == event_B[i]:
        both_occur += 1
    i += 1

AnB_probability = both_occur / len(event_B) 

print(round(AnB_probability / A_probability, 2))