def dont_give_me_five(start, end):
    count = 0
    for n in range(start, end + 1):
        if '5' not in str(n):
            count += 1
    return count



def to_jaden_case(string):
    return ' '.join(word.capitalize() for word in string.split())




def lowercase_count(strng):
    return sum(1 for char in strng if char.islower())




def better_than_average(class_points, your_points):
    average = sum(class_points) / len(class_points)
    return your_points > average





from functools import reduce

def grow(arr):
    return reduce(lambda x, y: x * y, arr)





def smash(words):
    return " ".join(words)
