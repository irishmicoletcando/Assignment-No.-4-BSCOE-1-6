# Create a program which you will enter the amount of money you have, it will also ask for the price of an apple.
# Display the maximum number of apples that you can buy and the remaining money that you will have.
# Display the output in the following format.
# You can buy ___ apples and your change is ___ pesos.

def money_apple_maxnumber_change():
    _money = float(input("How much money do you have? "))
    _apple = float(input("What is the price of an apple per piece? "))
    max_number_apples = int(_money // _apple)
    _change = _money % _apple
    return _money, _apple, max_number_apples, _change


money, apple, maxi_apples, change = money_apple_maxnumber_change()
display(maxi_apples, change)