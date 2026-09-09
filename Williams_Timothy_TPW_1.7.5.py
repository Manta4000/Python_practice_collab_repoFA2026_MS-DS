"Williams_Timothy_TPW_1.7.5"
##9.9.2026 -- practice for user input to calculate some value from fixed price classes
##Solved in 12 lines, QUESTION: Not sure how to force the output to use 2 decimal places everytime
one_liter_ = 0.00
more_than_one = 0.00
def deposit__calc__(one_liter_, more_than_one):
    one_liter_ = float(input("How many containers were one liter or less in size?: ", ))
    more_than_one = float(input("How many containters were one or more liters in size?: ", ))
    refund__ = (one_liter_*0.10) + (more_than_one*0.25)
    print("Calculating refund amount...")
    if refund__ >= 1000:
        print("Your refund amount should be: ", f"{refund__:,}", "USD")
    else:
        print("Your refund amount should be: ", refund__, "USD")

deposit__calc__(one_liter_, more_than_one)