print("BMI HEALTH INFORMATION")
name=input("Enter your name:")
weight=float(input("Enter your weight:"))
height=float(input("Enter your height:"))

BMI = weight / (height *height)

# display the result
print("==============================\nBMI REPORT\n==============================")

print( f" Name:{name}\n Weight:{weight} KG \n height:{height} M \n BMI:{BMI}\n ==============================")