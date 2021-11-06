# Create a program that will ask how many apples and oranges you want to buy.
# Display the total amount you need to pay if apple price is 20 pesos and orange is 25.
# Display the output in the following format.
# The total amount is ______.

def ask_apples_and_oranges_number_to_compute_price():
    apple_number = int(input("How many apples do you want to buy? "))
    apple_price = 20 * apple_number
    orange_number = int(input("How many oranges do you want to buy? "))
    orange_price = 25 * orange_number
    return apple_price, orange_price


apple, orange = ask_apples_and_oranges_number_to_compute_price()