def sequence_sum(begin_number, end_number, step):
    if begin_number > end_number or step == 0:
        return 0
    return sum(range(begin_number, end_number + 1, step))





def filter_list(l):
    return [item for item in l if not isinstance(item, str)]





def to_jaden_case(string):
    return ' '.join(word.capitalize() for word in string.split())




def sum_mix(arr):
    return sum(int(x) for x in arr)


 

def array_plus_array(arr1, arr2):
    return sum(arr1) + sum(arr2)




def reverse_words(s):
    return ' '.join(s.split()[::-1])




def sum_str(a, b):
    return str(int(a or '0') + int(b or '0'))



