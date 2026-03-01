# getting Input

Name = input("Enter First Name Only: ")
sex = input("Enter 'Male' Or 'Female' As Gender: ").upper()
Children = int(input("Enter number of children: "))
Hours_Worked = float(input("Enter the number of hours worked in a week: "))

# Calculations

if sex == "MALE":
    Regular_Rate = 500
else:
    Regular_Rate = 550

overtime_rate = Regular_Rate * 1.5

if Hours_Worked <= 40:
    Regular_Hours = Hours_Worked
    overtime_hours = 0
   
    overtime_pay = 0
else:
    Regular_Hours = 40
    overtime_hours = Hours_Worked - Regular_Hours
   
# Payments
Regular_pay = Regular_Hours * Regular_Rate
overtime_pay = overtime_hours * overtime_rate

# Total pay before Deduction
Gross_Pay = Regular_pay + overtime_pay

#Taxes
IncomeTax = 0.15 * Gross_Pay
E_Levy =  0.025 * Gross_Pay
District_Tax =  0.01 *  Gross_Pay

if Children > 3:
    excess_children = Children - 3
    if sex == "MALE":
        edufund = excess_children * 10
    else:
        edufund = excess_children * 20
else:
    edufund = 0

Total_Deductions = IncomeTax + E_Levy + District_Tax + edufund

NetPay =  Gross_Pay - Total_Deductions

print(f"NAME OF EMPLOYEE: {Name}")
print("GEnder", sex)
print(f"Number of Children {Children}")
print("Gross Pay", Gross_Pay)
print("Total Deductions", Total_Deductions)
print(f"Your Netpay after taxes is {NetPay}")

print("THANK YOU")
  
    

