print("Welcome!")
print("Welcome to Personal Finance Analyzer.")
print("This program helps you understand your monthly financial situation.")

# Personal Information
print("   Personal Information   ")
full_name = input("What is your name?")

# Monthly Income
print("   Monthly Income   ")
Monthly_salary = float(input("Monthly salary (JOD)"))

# Monthly Expenses
print("   Monthly Expenses   ")
Rent = float(input("Rent"))
Food = float(input("Food"))
Transportation = float(input("Transportation"))
Shopping = float(input("Shopping"))
other_expenses = float(input("other expenses"))

# Saving Goal
saving_goal = float(input("What is your monthly saving goal?"))

# Input Validation
if Monthly_salary <= 0:
    print("Invalid salary")
    exit()

if Rent < 0 or Food < 0 or Transportation < 0 or Shopping < 0 or other_expenses < 0:
    print("Invalid expenses")
    exit()

if saving_goal < 0:
    print("Invalid Value")
    exit()

# Financial Calculations
Total_expenses = Rent + Food + Transportation + Shopping + other_expenses

Remaining_Balance = Monthly_salary - Total_expenses
Expense_Percentage = (Total_expenses / Monthly_salary) * 100
Remaining_Balance_Percentage = (Remaining_Balance / Monthly_salary) * 100
Savings_Goal_Difference = Remaining_Balance - saving_goal

Rent_Percentage = (Rent / Monthly_salary) * 100
Food_Percentage = (Food / Monthly_salary) * 100
Transportation_Percentage = (Transportation / Monthly_salary) * 100
Shopping_Percentage = (Shopping / Monthly_salary) * 100
Other_Expenses_Percentage = (other_expenses / Monthly_salary) * 100

# Financial Report
print("========== Financial Report ==========")

print(f"Customer Name: {full_name}")
print(f"Monthly Income = {Monthly_salary:.2f} JOD")
print(f"Total Expenses = {Total_expenses:.2f} JOD")
print(f"Remaining Balance = {Remaining_Balance:.2f} JOD")
print(f"Expense Percentage = {Expense_Percentage:.2f}%")
print(f"Remaining Balance Percentage = {Remaining_Balance_Percentage:.2f}%")
print(f"Saving Goal = {saving_goal:.2f} JOD")
print(f"Savings Goal Difference = {Savings_Goal_Difference:.2f} JOD")

# Expense Breakdown
print("========== Expense Breakdown ==========")

print(f"Rent Percentage = {Rent_Percentage:.2f}%")
print(f"Food Percentage = {Food_Percentage:.2f}%")
print(f"Transportation Percentage = {Transportation_Percentage:.2f}%")
print(f"Shopping Percentage = {Shopping_Percentage:.2f}%")
print(f"Other Expenses Percentage = {Other_Expenses_Percentage:.2f}%")

# Financial Analysis
print("========== Financial Analysis ==========")

# Expenses Warning
if Total_expenses > Monthly_salary:
    print("Warning! Your expenses exceed your monthly income.")

# Spending Level
if Expense_Percentage < 50:
    print("Spending Level: Low Spending")
elif Expense_Percentage <= 80:
    print("Spending Level: Moderate Spending")
else:
    print("Spending Level: High Spending")

# Savings Analysis
if Remaining_Balance > saving_goal:
    print("Congratulations! You exceeded your savings goal.")

elif Remaining_Balance == saving_goal:
    print("You achieved your savings goal exactly.")

else:
    print("You have not reached your savings goal yet.")
    Short_fall = saving_goal - Remaining_Balance
    print(f"Your savings shortfall is {Short_fall:.2f} JOD")

# Financial Status
print("========== Financial Status ==========")

if Remaining_Balance > 0:
    print("Financial Status: Surplus")
elif Remaining_Balance < 0:
    print("Financial Status: Deficit")
else:
    print("Financial Status: Break-even")

# Income Usage
if Remaining_Balance == 0:
    print("Your income was fully used.")

# Financial Recommendations
print("========== Financial Recommendations ==========")

# Recommendation based on Financial Status
if Remaining_Balance < 0:
    print("Recommendation: Review and reduce your expenses.")

# Recommendation based on Spending Level
if Expense_Percentage > 80:
    print("Recommendation: Try to reduce unnecessary spending.")

# Recommendation based on Savings Goal
if Remaining_Balance < saving_goal:
    print("Recommendation: Consider increasing your savings.")

# Positive Savings Recommendation
if Remaining_Balance > saving_goal:
    print("Recommendation: Keep maintaining your saving habits.")