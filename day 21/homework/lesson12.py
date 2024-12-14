#Indexing:   გამოიყენება მხოლოდ ერთიანი ელემენტის მისაღებად. 
# მასში ინდექსი პირდაპირ მიუთითებს იმ ელემენტზე, რომლის მიღებაც გვინდა.

#Slicing:გამოიყენება სეგმენტების (საბოლოო სერიების) მისაღებად.
# slicing-ში ორი მნიშვნელობა უნდა იყოს მითითებული: დასაწყისი და დასასრული.


cars = ["Toyota", "Mercedes", "BMW", "Tesla", "Audi"]
print(cars[-3:])  




numbers = [3, 7, 10, 12, 15, 1, 8, 20, 9, 6]


filtered_numbers = [num for num in numbers if num >= 10]
print(filtered_numbers)  






last_name = input("Please enter your last name: ")


convert_to_upper = input("Do you want your last name to be converted to uppercase? (yes/no): ").lower()


if convert_to_upper == "yes":
    print(last_name.upper())
elif convert_to_upper == "no":
    print(last_name)
else:
    print("Invalid response")

    





