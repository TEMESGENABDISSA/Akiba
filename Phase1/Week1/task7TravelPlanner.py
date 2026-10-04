print("Travel Planner")
destination=input("Enter your destination:")
distance=float(input("Enter distanncein kilometeres:"))
speed=float(input("Enter your Average speed:"))
Time= distance/speed
hours = int(Time)
minutes = int((Time - hours) * 60)
print( f" destination:{destination}\n Distance:{distance} km \n Average Speed:{speed} km/h\n EStimated travel time:{Time} hours {minutes} minutes")