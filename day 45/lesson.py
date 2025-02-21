def swap_values(args):
    args[0], args[1] = args[1], args[0]  




values = [1, 2]
swap_values(values)
print(values) 




def same_case(a, b):
    if not (a.isalpha() and b.isalpha()):  
        return -1
    return int((a.islower() and b.islower()) or (a.isupper() and b.isupper()))

print(same_case('a', 'b')) 
print(same_case('A', 'B')) 
print(same_case('a', 'B')) 
print(same_case('A', 'z'))  
print(same_case('1', 'A'))  




def sum_mul(n, m):
    if n <= 0 or m <= 0:  
        return "INVALID"
    
    return sum(range(n, m, n))  

print(sum_mul(2, 9))   
print(sum_mul(3, 10)) 
print(sum_mul(4, 20))  
print(sum_mul(5, 5))   
print(sum_mul(0, 10)) 
print(sum_mul(-3, 10)) 







def calculate_age(year_of_birth, current_year):
    difference = current_year - year_of_birth
    
    if difference == 0:
        return "You were born this very year!"
    elif difference == 1:
        return "You are 1 year old."
    elif difference > 1:
        return f"You are {difference} years old."
    elif difference == -1:
        return "You will be born in 1 year."
    else:
        return f"You will be born in {abs(difference)} years."

print(calculate_age(2000, 2025))  
print(calculate_age(2025, 2000))  
print(calculate_age(2023, 2023)) 
print(calculate_age(2010, 2011))  
print(calculate_age(2025, 2024))  

