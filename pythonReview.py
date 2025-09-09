message = "Welcome to Internship Ready!"
print(message, "FIU", 2025)
print(type(message))
print(type(2025))
print(type(3.14))
print(type(3==6/2))

first_name = "greg"
last_name = "reis"
print(first_name + last_name)
print(first_name + " " + last_name)
print(first_name, last_name)

print('2' + '3')

a = 2
b = 3
print(a + b) # addition
print(a - b) # subtraction
print(a * b) # multiplication
print(b / a) # division
print(b // a) # integer division
print(a ** b) # exponentiation
print(7 % 4) # Modulus (remainder of division)

professors = ["richard", "kianoosh", "debra", "leo", "jason", "sadjadi"]

print(type(professors))
print(professors[0])
print(professors[-1])
print(professors[2:5]) # accessing elements 2, 3, and 4
print(professors[:3]) # from beginning to position 2
print(professors[2:]) # from position 2 to the end
print(professors[:])

professors.append("agoritsa")
print(professors)
professors.extend(["kevin","todd","heather"])
print(professors)
print(len(professors))
professors.insert(1,"greg")
print(professors)

professors.remove("kianoosh")
print(professors)

x=professors.index("todd")
print(x)

y=professors.pop(8)
print(professors,y)

z = professors.count("kianoosh")
print(z)

professors.reverse()
print(professors)

professors.sort(reverse=True)
print(professors)

for i in professors:
    if len(i) > 4:
        print(i.lower())
    else:
        print(i.upper())

# Dictionaries

water_data = {
    "date" : ["09/02/2025","09/03/2025","09/04/2025"],
    "temperature" : [89.2, 92.3, 90.7],
    "oxygenConcentration" : [6.14, 6.7, 7.8]
}
print(water_data)

import pandas as pd

df = pd.DataFrame(water_data)
print(df)