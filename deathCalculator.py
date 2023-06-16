""" This is a simple calculator that will calculate how long will you live based on your current age"""

currentAge = int(input('Enter your current age: '))

ageRemain = 90 - currentAge  # Assuming that average life span of an Individual being 90 years.

# This is the part where we calculate all our data

yearsRemain = ageRemain * 365
weeksRemain = ageRemain * 52
monthsRemain = ageRemain * 12

print(f"You have {yearsRemain} years, {weeksRemain} weeks and {monthsRemain} months left")


