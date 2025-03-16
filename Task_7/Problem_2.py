
# inout both events and check they are 0s and 1s only (used tuple since elements won't change)
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
    if num == 1 and event_A[i] == event_B[i]: # if event occured in A and B
        both_occur += 1
    i += 1

AnB_probability = both_occur / len(event_B) 

print(round(AnB_probability / A_probability, 2))
# how is the output 0.5 in the problems sheet?