# Declare and initialize variables here
employee_name = input("Enter the employee's name: ")
number_of_shifts = int(input("Enter the number of shifts: "))
number_of_transactions = int(input("Enter the number of transactions: "))
transaction_dollar_value = float(input("Enter the transaction dollar value: "))

# Calculate productivity score
productivity_score = (transaction_dollar_value / number_of_transactions) / number_of_shifts

# Determine the bonus using nested if statements
if productivity_score <= 30:
    bonus = 50.00
else:
    if productivity_score <= 69:
        bonus = 75.00
    else:
        if productivity_score <= 199:
            bonus = 100.00
        else:
            bonus = 200.00

# Print the output
print("Employee Name: " + employee_name)
print("Employee Bonus: $" + str(bonus))