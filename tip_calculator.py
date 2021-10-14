#Anthony Caccamo's App Project 1 - Tip Calculator

print() # I will use these empty print statements throughout to make the output easier to read. 

print('This is Tippy. I am here to calculate how much you should pay. Please follow the instructions below!') #This will just print an opening statement for the app. I used this and the last line

print()

#INPUT: The blocks of code from line 12 to 16 are inputs and require the user to enter information, which the app will depend on. This will use the 'input' function. 
#Additionally, 'float' is used to convert the input to a float, which will avoid TypeErrors. (which are due to adding/subtracing/multiplying/dividing different datatypes.)

food_costs = float(input('The total cost of the food is: ' ))

amount_of_people = float(input('The amount of people paying are: '))

tip_percent = float(input('The percent tip I want to pay is: '))

print()

#OUTPUT: This is the information the app will produce and is the end goal of the app - to find out how much each person(s) should pay on a restaurant or similar bill.
print('RESULTS:') # I added this to make the python output easier to read.

total_bill = ((food_costs * (tip_percent/100)) + (food_costs * .10)) + food_costs #This calculates the total tip of the bill, including tip and tax. The tip percentage is entered by the user. I divide by 100 to make the input a percent . The tax is set at 10% or .10. This variable is used in line 27.

Amount_to_pay = total_bill / amount_of_people #Takes the total bill (after tax and tip) and divides it by number of people. This variable is used in line 26.

print(f'Total bill: ${total_bill}')
print(f'Each person should pay ${round(Amount_to_pay,2)}')
print()
print('Thank you for using Tippy!') #I added this to add flair to