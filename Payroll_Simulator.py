# Payroll Assignment Bootcamp

# This program is written to calculate the payroll for employees in a payroll cycle. 
# Program was written for a bootcamp assignment for our Fitntech Program for Fall 2022

# The program has a pretty straight forward approach and can be mostly used for 
# any businesses in the US to calculate payroll for their employees

# Coding Start from here

# Here we are taking the inputs for marital status, number of hours worked and hourly payrate
# We are using upper() in order to make sure the user's lower case entry of s or m doesn't
# create an error for marital status entry

Marital_Status = input("Please enter your Maritial Status. Enter 'S' for Single or 'M' for Married: ").upper()

# Using validations we are going to protect our program from invalid entries from user's below

# Using while loop we will make sure input for Payrate and Hours worked is in numerical format

while True:
    try:
        Payrate = float(input("Please enter your designated Hourly Payrate in dollars: $"))
        break
    except ValueError:
        print("Incorrect input value. Payrate must be in numerical digits format")

while True:
    try:
        Work_Hours = float(input("Please enter the number of hours you worked this month: "))
        break
    except ValueError:
        print("Incorrect input value. Hours Worked must be in numerical digits format")

# Now we have defined what the Basepay is and how it will be calculated
BasePay = Work_Hours * Payrate

# Bonus Amount input is being set up below
BonusAmount = input("Please enter if you received any bonuses this month? 'Y' for Yes and 'N' for no: ").upper()
if BonusAmount == 'Y':
    Bonus = float(input("Please Enter your Bonus Pay in Dollars: $"))
else:
    Bonus = 0
# We are now setting Monthly Gross_Income and how its calculated

Monthly_Gross_Income = BasePay + Bonus

# Importing sys for use of function and date in order to use for the packages later
import sys

# Here we are entering the Before-Tax Deductions and putting the Adjustments

Adjustments = float(input("Please enter any Adjustments(Medical, Parking Deductions, etc.) you have for the month: ")) 
# I am saying that the 401K contributions is going to be 8.75% and not more than that.
# This can be changed if you want to contribute more. I would just contribute up to what I'm matched by the company.
_401K = .0875 * Monthly_Gross_Income 
if _401K > 20000:
    print("401K contribution for all individuals has been capped at $20000 for the year")
    _401K = 20000
# Designated vaue for entry is zero for Dental, FlexMed and _403B entries below, but code here designed to take user's entry
Dental_Plus = float(input("Please enter designated amount for Dental Plan Contributions in dollars: $")) 
Flex_Med = float(input("Please enter designated amount for Flexmed(Medicine, Cyro, Vision) contributions in dollars: $"))
_403b = float(input("Please enter designated amount for 403b(Catch-Ups) contribution in dollars: $"))
if _403b > 7000:
    print("403b contributions has been capped at $7000 for the year")
    _403b = 7000

# BeforeTax_Deductions below is being defined as a variable with all the additions mentioned above
# Fed_Taxable_Gross is going to be defined as Montly_Gross_Income with the substraction of BeforeTax_Deductions
# I needed Fed_Taxable_Gross defined in order to use it on our next step making the function for the tax bracket 
# based on annual salary and Marital_Status

BeforeTax_Deductions = Adjustments + _401K + Dental_Plus + Flex_Med + _403b
Fed_Taxable_Gross = Monthly_Gross_Income - BeforeTax_Deductions

# Below I have defined a function Total_Tax_Bracket based on Marital_Status and Fed_Taxable_Gross in order to call later

def Total_Tax_Bracket(Marital_Status, Fed_Taxable_Gross):
    if Marital_Status == 'S':
        if Fed_Taxable_Gross >=0 and Fed_Taxable_Gross < 10275:
            Taxing_Rate = 0.1
        elif Fed_Taxable_Gross >= 10275 and Fed_Taxable_Gross < 41775:
            Taxing_Rate = 0.12
        elif Fed_Taxable_Gross >= 41775 and Fed_Taxable_Gross < 89075:
            Taxing_Rate = 0.22
        elif Fed_Taxable_Gross >= 89075 and Fed_Taxable_Gross < 170050:
            Taxing_Rate = 0.24
        elif Fed_Taxable_Gross >= 170050 and Fed_Taxable_Gross < 215950:
            Taxing_Rate = 0.32
        elif Fed_Taxable_Gross >= 215950 and Fed_Taxable_Gross < 539900:
            Taxing_Rate = 0.35
        elif Fed_Taxable_Gross >= 539901:
            Taxing_Rate = 0.37
    elif Marital_Status == 'M':
        if Fed_Taxable_Gross >= 0 and Fed_Taxable_Gross < 20550:
            Taxing_Rate = 0.1
        elif Fed_Taxable_Gross >= 20550 and Fed_Taxable_Gross < 83550:
            Taxing_Rate = 0.12
        elif Fed_Taxable_Gross >= 83550 and Fed_Taxable_Gross < 178150:
            Taxing_Rate = 0.22
        elif Fed_Taxable_Gross >= 178150 and Fed_Taxable_Gross < 340100:
            Taxing_Rate = 0.24
        elif Fed_Taxable_Gross >= 340100 and Fed_Taxable_Gross < 431900:
            Taxing_Rate = 0.32
        elif Fed_Taxable_Gross >= 431900 and Fed_Taxable_Gross < 647850:
            Taxing_Rate = 0.35
        elif Fed_Taxable_Gross >= 647850:
            Taxing_Rate = 0.37
    return Taxing_Rate

# Fed_Withholding is being defined and here we recall the function Total_Tax_Bracket to calculate it.
# Fed_MED_EE, Fed_OASDI_EE are all defined below using the Fed_Taxable_Gross Variable
# Total_Taxes is going to be all the three variables added below.

Fed_Withholding = Total_Tax_Bracket(Marital_Status, Fed_Taxable_Gross*12) * Fed_Taxable_Gross
Fed_MED_EE = 0.0145 * Fed_Taxable_Gross
Fed_OASDI_EE = 0.062 * Fed_Taxable_Gross
Total_Taxes = Fed_Withholding + Fed_MED_EE + Fed_OASDI_EE

# Employee_After_Tax_Income defined below is the final amount in dollars that the employee receives for his monthly paycheck
# after all the Before Tax Deductions and Federal Withholdings

Employee_After_Tax_Income = Fed_Taxable_Gross - Total_Taxes

# Below are all the variables printed with the print function. I have also used the imported date from datetime 
# to define which month's pay cycle it is.

from datetime import date 

print("Date: ", date.today().month, "-", date.today().year)

print(f"BasePay: {BasePay}")
print(f"Bonus: {Bonus}")
print(f" Monthly Gross Income: {Monthly_Gross_Income}")

print("\n \n Before Tax Deductions Below")

print(f"Adjustments(Medical, Parking Deduction, etc.): {Adjustments}")
print(f"401K: {_401K}")
print(f"Dental Plus Plan: {Dental_Plus}")
print(f"Flex Med (Vision, Medicine, Cyro): {Flex_Med}")
print(f"403b (Catch-Ups): {_403b}")

print(f"Total Deductions: {BeforeTax_Deductions}")

print(f"Fed Gross Taxable: {Fed_Taxable_Gross}")

print(" \n \n Total Taxes Below")

print(f"Total Taxes: {Total_Taxes}")

# Employee_After_Tax_Income is what each employee receives after all the deductions and withholdings

print(" After Tax Income: ", Employee_After_Tax_Income)


            



