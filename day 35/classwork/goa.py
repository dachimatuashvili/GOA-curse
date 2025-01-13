






def max_multiple(divisor, bound):
    return (bound // divisor) * divisor





def sum_digits(number):
    return sum(int(digit) for digit in str(abs(number)))




def sum_digits(number):
    return sum(int(digit) for digit in str(abs(number)))




def dont_give_me_five(start, end):
    return sum(1 for n in range(start, end + 1) if '5' not in str(n))




def fizzbuzz(n):
    result = []
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            result.append("FizzBuzz")
        elif i % 3 == 0:
            result.append("Fizz")
        elif i % 5 == 0:
            result.append("Buzz")
        else:
            result.append(i)
    return result




def invert(lst):
    return [-x for x in lst]





def sum_array(arr):
    if len(arr) <= 2:
        return 0
    arr.sort()
    return sum(arr[1:-1])




