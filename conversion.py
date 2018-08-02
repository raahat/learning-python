from math import factorial

temp_format = "%9.1f| %7d|"
print "Farenheit|", "Celsius|"
for celsius  in range(0, 101, 5):
    farenheit = 9. / 5 * celsius + 32
    print(temp_format % (farenheit, celsius))


def farenheit_from_celsius(celsius):
    return 9. / 5 * celsius + 32


assert 212.0 == farenheit_from_celsius(100)


print type(farenheit_from_celsius(100))


def factorial(number):
    if type(number) != type(7):
       print('the number must be an integer')
       return
    if number < 0: 
       print('the number must greater or equal to 0')
       return
    fact = 1
    for i in range(2, number + 1):
        fact = fact * i
    return fact

def rec_factorial(number):
    if number == 1 or number == 0:
        return 1
    return number * factorial(number - 1)
assert 120 == factorial(5)  
print rec_factorial(5)

