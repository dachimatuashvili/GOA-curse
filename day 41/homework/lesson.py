def multiply(a, b):
    return a * b




def even_or_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"




def number_to_string(num):
    return str(num)




def is_valid_walk(walk):
    if len(walk) != 10:
        return False

    north_south = walk.count('n') - walk.count('s')
    east_west = walk.count('e') - walk.count('w')
    
    return north_south == 0 and east_west == 0




def make_negative(number):
    return -abs(number)




def printer_error(s):
    errors = sum(1 for char in s if char not in 'abcdefghijklm')
    return f"{errors}/{len(s)}"




def bool_to_word(boolean):
    return "Yes" if boolean else "No"




def zero_fuel(distance_to_pump, mpg, fuel_left):
    return distance_to_pump <= mpg * fuel_left




def reverse_words(text):
    return ' '.join(text.split()[::-1])
