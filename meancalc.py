# Write a code to do the following: the code takes in five numbers A, B, C, D and E.
# It then calculates the mean of the five numbers and gives the message "The mean of A, B, C, D and E is 'mean'
# " where 'mean' is the mean of the five numbers.

A = input("Enter number 1: ")
B = input("Enter number 2: ")
C = input("Enter number 3: ")
D = input("Enter number 4: ")
E = input("Enter number 5: ")

# To calculate the mean, we add all the numbers together and then divide by the total count of numbers.
mean = (int(A) + int(B) + int(C) + int(D) + int(E)) / 5

# Finally, we print the result in string
print(f"The mean of {A}, {B}, {C}, {D} and {E} is {str(mean)}")