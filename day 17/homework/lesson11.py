
fruits = ["apple", "banana", "orange", "kiwi", "peach"]

for index, item in enumerate(fruits):
    print(f" {index}: {item}")




fruit = ["apple", "banana", "orange", "kiwi", "peach", "grape", "watermelon", "cherry", "plum", "pineapple"]

for item in fruit:
    print(item)






numbers = [5, 12, 3, 18, 9, 25, 8, 30, 7, 10]

for number in numbers:
    if number > 10:
        print(number)





my_list = [42, "hello", 3.14, True, None, [1, 2, 3], {"key": "value"}]


for item in my_list:
    print(f"Element: {item} | Data type: {type(item)}")
