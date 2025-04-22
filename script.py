def calculate_discount(price, discount_percent):
    discounted_price = 0

    if (discount_percent >= 20):     #Applying discount if the percentage is 20% or more
        discounted_price = price - ((discount_percent/100) * price)
        print(discounted_price)

    else:                            #Do not apply discount if the percentage is less than 20%
        print(price)

#Prompting the user to enter the required parameters
print("Enter the original price of an item and the discount percentage (without units)")

#Declaring variables to store the parameters
original_price = int(input())
discount_percentage = int(input())

#Calling the function to calculate the discount
calculate_discount(original_price, discount_percentage)