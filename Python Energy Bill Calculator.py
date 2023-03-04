#Assignment1

'''
program description: This program will calculate the total of the utilities expenses.
The user will need to type the next information: account number, month to calculate,
electricity and gas plan, electricity and gas used in the month to calculate and the province.
Aditional to the consumption of the gas and electricity there's a fixed fee for every user.
Author: Ana Joselyn Alarcon
Date: Sept 26, 2022
'''
print("Welcome to the Global Energy bill calculator! ")
#Every user pays a fixed fee
gge_fee = 120.62

input_accountnumber = int(input("Enter your account number\n "))

input_month = input("Enter the month number (e.g., for January, enter 1) \n")

#Electricity
#The electricity rate depends on the plan and the amount spended.
input_elec_plan = input("Enter your electricity plan (EFIR or EFLR)  \n")

input_elec_amount = float(input("Enter the amount of electricity you used in month " + input_month + " (in kWh)  \n       "))

if input_elec_plan == "EFIR":
    if input_elec_amount <=1000:
        elec_expense = input_elec_amount *8.36
    else:
        elec_expense = ((input_elec_amount-1000)*9.41)+(1000*(8.36))
else:
    elec_expense = input_elec_amount * 9.11


#Gas expense
#The gas rate depends on the plan and the amount spended.
input_gas_plan = input("Enter your gas plan (GFIR or GFLR)  \n")

input_gas_amount = float(input("Enter the amount of gas you used in month " + str(input_month) + "   (in GJ)  \n"))

if input_gas_plan == "GFIR":
    if input_gas_amount <=950:
        gas_expense = input_gas_amount *4.56
    else:
        gas_expense = ((input_gas_amount-950) * 5.89)+(950*4.56)
else:
    gas_expense = input_gas_amount * 3.93



#Province
#Depending on the province the tax rate may vary.
input_province = input("Enter the abbreviation for your province of residence (two letters)  \n")
tax_rate = 0
if input_province == "AB" or "BC" or "MB" or "NT" or "NU" or "QC" or "SK" or "YT":
    tax_rate = 0.05
elif input_province == "ON":
    tax_rate = 0.13
else:
    tax_rate = 0.15


subtotal = ((gas_expense + elec_expense)*0.01)
total = (subtotal + gge_fee)* (1 + tax_rate)
print("Thank you! Your amount due now is: $" +str(round(total,2)))
