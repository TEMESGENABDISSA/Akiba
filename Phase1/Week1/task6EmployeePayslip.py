print("EMPLOYEE PAYSLIP")
name=input("Enter your name:")
salary=float(input("Enter basic salary:"))
transport=float(input("Enter Transport allowance:"))
food=float(input("Enter Food allowance:"))
# Calculate gross salary
gross_salary = salary + transport+ food

print(" EMPLOYEE PAYSLIP")
print(f"Employee Name : {name}")
print(f"Basic Salary : {salary:.2f}") 
print(f"Transport Allowance : {transport:.2f}") 
print(f"Food Allowance : {food:.2f}") 
print(f"Gross Salary : {gross_salary:.2f}") 