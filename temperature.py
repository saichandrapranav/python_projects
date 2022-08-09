temperature = float(input('Enter the temperature in celsis '))
print(temperature, 'degree celsis')

fahrenheit = float(temperature * 1.8 + 32)
print(fahrenheit , 'degree fahrenheit')

if 25<temperature<35:
    print('It is hot')

else:
    print('it is not hot')

