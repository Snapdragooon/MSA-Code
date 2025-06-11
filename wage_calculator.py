# create a program to calculate yearly wage based on hours and wage

# GET DAILY HOURS FROM USER
# convert input to float
# check that daily hours are not over 24 or under 0, if so, reprompt user
while True:
    try:
        daily_hours = float(input("Enter the number of hours worked daily: "))
        if daily_hours <= 0:
            print("ERROR: Enter a value greater than 0")
            continue
        elif daily_hours >= 24:
            print("ERROR: Enter a value less than 24")
            continue
        else:
            break 
    except:
        print("ERROR: Please enter a number")

# GET HOURLY WAGE FROM USER
# covnert input to float
# check that hourly wage fits criteria, if not, reprompt user
while True:
    try:
        hourly_wage = float(input("Enter the hourly wage: "))
        if hourly_wage < 0:
            print("ERROR: Enter a value greater than 0")
            continue
        else:
            break 
    except:
        print("ERROR: Please enter a number")
print("\n")

# PROCESSING
# calculate yearly wage, tax amount, and wage minus taxes
DAYS_WORKED = 350
TAX_PERCENTAGE = 0.12
wage_before_taxes = (daily_hours*hourly_wage)*DAYS_WORKED
tax_amount = wage_before_taxes*TAX_PERCENTAGE
wage_after_taxes = wage_before_taxes - tax_amount

# OUTPUT
# print all the information to the user with 2 decimal places
print("Pay Advice \n-------------")
print(f"Hours Worked: ${daily_hours:.2f}")
print(f"Hourly Wage: ${hourly_wage:.2f}")
print(f"Wages Before Taxes: ${wage_before_taxes:.2f}")
print(f"Tax Amount: ${tax_amount:.2f}")
print(f"Annual Wage After Taxes: ${wage_after_taxes:.2f}")