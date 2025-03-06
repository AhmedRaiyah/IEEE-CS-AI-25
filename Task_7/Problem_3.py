
# probaility of A and check its num and +ve
while True:
    prior_a = float(input("P(A): "))
    if prior_a <= 0:
        print("Enter a positive number.")
    else:
        break

# probaility of B and check its num and +ve
while True:
    prior_b = float(input("P(B): "))
    if prior_b <= 0:
        print("Enter a positive number.")
    else:
        break

# Probability of B given A and check its num and +ve
while True:
    conditional_b_given_a = float(input("P(B|A): "))
    if conditional_b_given_a <= 0:
        print("Enter a positive number.")
    else:
        break


a_given_b = (conditional_b_given_a * prior_a) / prior_b


print("=> P(A|B): ", round(a_given_b, 2))
