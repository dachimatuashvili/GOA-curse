def greet():
    return "hello world!"


def boolean_to_string(b):
    return str(b)


def what_century(year):
    return (year - 1) // 100 + 1


def positive_sum(arr):
    return sum(x for x in arr if x > 0)


def no_space(s):
    return s.replace(" ", "")


def boolean_to_string(b):
    return str(b)


def will_you_make_it(bridge_crossing_cost, time_left, percent_of_cost_saved):
    return bridge_crossing_cost * (1 - percent_of_cost_saved) <= time_left


def remove_char(s):
    return s[1:-1]


def array_plus_array(arr1, arr2):
    return sum(arr1) + sum(arr2)


def array_diff(a, b):
    return [item for item in a if item not in b]
