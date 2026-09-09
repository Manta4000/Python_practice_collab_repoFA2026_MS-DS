"Williams_Timothy_TPW_1.7.7"
##Sum the first n positive integers -- once again reading the input from a user and uses base logic to sum all integers from 0 --> n
##SOLVED: was able to succinctly solve the problem using a concise function which takes input and converts all to an int() value, does not work with float() values as intended
n = 0
def __sum__(n):
    n = int(input("Input any integer greater than 0: ", ))
    sum = int((n*(n + 1))/2)
    print("The sum of all integers from 0 --> n is: ", sum)
    return
__sum__(n)