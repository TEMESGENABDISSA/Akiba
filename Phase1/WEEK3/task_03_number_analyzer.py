def is_prime(number): 
    if number<=1:
        return  "  insert above 1 "
    for i in range(2,number):
        if number%i==0:
         return  " is not prime numbers"
    else:
        return "its  prime numbers "
print(is_prime(5))
print(is_prime(10))
print(is_prime(0))
print(is_prime(-1))

def get_divisors(number):
   divisors=[]
   if number==0:
        return divisors
   for i in range(1,abs(number)+1):
      if number%i==0:
            divisors.append(i)

   return divisors
print(get_divisors(5))

def sum_of_digits(number):
    totalsum=0;
    for i in range(abs(number)):
     totalsum= totalsum + i
    return totalsum
print(sum_of_digits(5))


def reverse_number(number):
    reverse = str(abs(number))
    reverse = reverse[::-1]
    return reverse
    
print(reverse_number(-544444))

def analyze_number(number):
   print("____this is Analyzer")
   analyzer={
      "numbers is":"even" if number %2==0 else "odd",
      "  this numbers":is_prime(number),
      " the sum of digits":sum_of_digits(number),
      "the reversed value is":reverse_number(number),
      " the divisors is ":get_divisors(number)
   }
   return analyzer
print(analyze_number(-25))