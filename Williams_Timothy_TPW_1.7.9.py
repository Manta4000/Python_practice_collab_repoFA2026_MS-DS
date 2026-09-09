"Williams_Timothy_TPW_1.7.9"
##Compound Interest -- Calculation based on user input for interest at an annual rate of 4%
##SOLVED: 
__interest__ = 0.04 #Annual Interest rate
__principal__ = 0.00
def savings__calc__(__interest__, __principal__):
    __principal__ = float(input("Principal? ", ))
    y = 1
    while y <= 3:
        __savings__total = (1+(__interest__/1))**(1*y)*__principal__
        print("Savings after Y"+f"{y}" , round(__savings__total, 2))
        y += 1
    return

savings__calc__(__interest__, __principal__)