def nth_even(n):
    return 2 * (n - 1)



def add_length(str_):
    words = str_.split()

    result = [f"{word} {len(word)}" for word in words]
    
    return result



import math
def square_or_square_root(arr):
    result = []
    for num in arr:
        if math.isqrt(num) ** 2 == num:
            result.append(math.isqrt(num))
        else:
            result.append(num ** 2)
    return result




def array(string):
    parts = string.split(',')

    if len(parts) <= 2:
        return None

    return ' '.join(parts[1:-1])




def find_difference(a, b):
    return abs((a[0] * a[1] * a[2]) - (b[0] * b[1] * b[2]))

