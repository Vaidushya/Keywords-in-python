# -- Homework -- #

# Program to calculate customer due amount after paying a bill

total_bill = 49

# Get the amount paid by the customer

print("Total bill:", total_bill)
amount_paid = int(input("Enter the amount paid by the customer: "))

# Calculate the due amount

if amount_paid < total_bill:
    due_amount = total_bill - amount_paid
    print("Customer has a due amount of:", due_amount)
elif amount_paid == total_bill:
    due_amount = 0
    print("No due amount, bill is fully paid. Now go and enjoy your meal!")
elif amount_paid > total_bill:
    due_amount = amount_paid - total_bill
    print("Customer has overpaid by:", due_amount)
else:
    due_amount = 0
    print("No due amount, bill is fully paid.")