
def validate_units(units):
    if int(units) < 0:
        return False
    else:
        return True

def calculate_first(units):
    validate = validate_units(units)

    if validate == False:
        return "Invalid units"

    if units <= 50:
        return units * 0.50
    else:
        return 50 * 0.50

def calculate_second(units):
    validate = validate_units(units)

    if validate == False:
        return "Invalid units"

    if units <= 50:
        return 0
    elif units <= 150:
        return (units - 50) * 0.75
    else:
        return 100 * 0.75

def calculate_third(units):
    validate = validate_units(units)

    if validate == False:
        return "Invalid units"

    if units > 150:
        return (units - 150) * 1.20
    else:
        return 0
   
def total_bill(units ,servicefee=0):
    first=calculate_first(units)
    second=calculate_second(units)
    third=calculate_third(units)
    total=first+second+third + servicefee
    return total



def generate_billing_summary(units, servicefee=0):
    
    if servicefee < 0:
        print("Error: Service fee cannot be negative!")
        return None

    if not validate_units(units):
        print("Error: Invalid electricity units!")
        return None

    first = calculate_first(units)
    second = calculate_second(units)
    third = calculate_third(units)
    total = total_bill(units, servicefee)

    
    summary = {
        "Title": "ELECTRICITY BILL",
        "Units": f"{units} units",
        "First Tier": f"{first:.2f} Birr",
        "Second Tier": f"{second:.2f} Birr",
        "Third Tier": f"{third:.2f} Birr",
        "Electricity Charge": f"{first + second + third:.2f} Birr",
        "Service Fee": f"{servicefee:.2f} Birr",
        "Total": f"{total:.2f} Birr"
    }

    print("\n========== ELECTRICITY BILL ==========")

    for key, value in summary.items():
        print(key, ":", value)

    print("======================================")

    return summary


print(generate_billing_summary(180,5 ))
