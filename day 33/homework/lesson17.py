def double_integer(i):
    return i * 2



def friend(x):
    return [name for name in x if len(name) == 4]



def grow(arr):
    result = 1
    for num in arr:
        result *= num
    return result



def find_average(numbers):
    return sum(numbers) / len(numbers) if numbers else 0



def goals(laLiga, copaDelRey, championsLeague):
    return laLiga + copaDelRey + championsLeague
#I liked this Question


 
def double_char(s):
    return ''.join([char * 2 for char in s])



def remove_url_anchor(url):
    return url.split('#')[0]



def sum_cubes(n):
    return sum(i ** 3 for i in range(1, n + 1))









def modify_list():
    Players = ["Messi", "Ronaldo", "Neymar", "Puyol", "Maldini"]
    
    Players.pop(2)

    Players.insert(0, 99) 

    return Players
  



def power(Something, Anything):
    return Something ** Anything





def check_list_length(lst):
    if len(lst) % 2 == 0:
        return "List length is even"
    else:
        return "List length is odd"
