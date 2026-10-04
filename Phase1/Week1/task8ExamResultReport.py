print("Exam Result Report")
name= input("Enter your name:")
python=  int(input("Enter python score:"))
English = int(input("Enter Enlish score:"))
mathematics=int(input("Enter your mathematics score:"))
 
#calculate the average
average= python+English+mathematics/3

print("Student Result")
print(f"Student:{name}\n python: {python}\n English:{English}\n Mathematics:{mathematics}\n Average:{average:.2f}")