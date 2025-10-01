# Program #2: Math Quiz
# Write a program that gives simple math quizzes.  The program should display two random numbers to be added, such as

#     247

# + 129

# ------

# The program should allow the student to enter the answer.  
# If the answer is correct, a message of congratulations should be displayed.  
# If the answer is incorrect a message showing the correct answer should be displayed.  
# The program must use a function that accomplishes part of the needed tasks.
def sum_of_numbers(n1, n2):
    print(n1,"+" ,n2, "=")
    total = n1 + n2
    answer = int(input("What do you think the answers is? "))
    if answer == total:
        print("Correct!")
    else:
        print("Incorrect! The answer was: ", total)
    return total
sum_of_numbers(12, 13)

