even_numbers = []

for num in range(201):
    if num % 2 == 0:
        even_numbers.append(num)

print(even_numbers)




favorite_names = []

for i in range(5):
    name = input(f"Enter your favorite name #{i+1}: ")
    favorite_names.append(name)

print("Your top 5 favorite names are:", favorite_names)




numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


for i in range(len(numbers)):
    if i % 2 != 0:  
        print(numbers[i])




string = "Hello, World!"


length_of_string = len(string)

print("The length of the string is:", length_of_string)







my_list = [10, 20, 30, 40, 50]

index = int(input("Enter the index of the element you want to get (0-4): "))

if 0 <= index < len(my_list):
    print(f"The element at index {index} is: {my_list[index]}")
else:
    print("Invalid index! Please enter a number between 0 and 4.")







my_list = [10, 20, 30, 40, 50]


list_length = len(my_list)


print("The length of the list is:", list_length)







