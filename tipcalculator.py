#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

print("Wecome to the tip calculator!")
bill = float(input("What is the total bill?\n"))
tip_percentage = int(input("How much tip would you like to give 10, 12, 15 or 18?\n"))
split = int(input("How many people are splitting the bill?\n"))

tip = tip_percentage / 100

total_tip = tip * bill
total_bill = bill + total_tip
total_bill_rounded = round(total_bill, 2)
total_bill_rounded = "{:.2f}".format(total_bill_rounded)
each_bill = total_bill / split
each_bill_rounded = round(each_bill, 2)
each_bill_rounded = "{:.2f}".format(each_bill_rounded)
print(f"Your total bill is {total_bill_rounded}")
print(f"Each person's share is ${each_bill_rounded}")



