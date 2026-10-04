print ("Temperature Station")
temperature_celsius=float(input("Enter temperature in celsius:"))
fahrenheit= (temperature_celsius * 9/5) + 32
print (f"Celsius:{temperature_celsius}°C\nFahrenheit{fahrenheit:.2f}F:")
#    to convert  fahrenheit to the celsius
temperature_fahrenheit = float(input("Enter Temperature in Fahrenheit:"))
celsius = (temperature_fahrenheit - 32) * 5 / 9
print(f"Temperature in Celsius: {celsius:.2f} °C")