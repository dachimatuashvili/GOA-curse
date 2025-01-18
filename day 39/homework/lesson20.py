def litres(time):
    return int(time * 0.5)








def open_or_senior(data):
    result = []
    for age, handicap in data:
        if age >= 55 and handicap >= 7:
            result.append("Senior")
        else:
            result.append("Open")
    return result








def xo(s):
    s = s.lower()
    
    return s.count('x') == s.count('o')











def high_and_low(numbers):
    num_list = list(map(int, numbers.split()))
    
    return f"{max(num_list)} {min(num_list)}"









def disemvowel(string_):
    vowels = "aeiouAEIOU"

    return ''.join([char for char in string_ if char not in vowels])








def is_isogram(string):
    string = string.lower()
    
    string = ''.join([char for char in string if char.isalpha()])

    return len(string) == len(set(string))





