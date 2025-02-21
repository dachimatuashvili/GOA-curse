def alphabetic(i):
    return i == ''.join(sorted(i))






\
def max_multiple(divisor, bound):
    #გავიგოთ რა რაოდენობა იკავებს divisor-ი bound-ის ფარგლებში ამისათვის გავყოთ bound-ი divisor-ით
    return (bound // divisor) * divisor






def min_value(digits):
    # ამოვიღოთ დუბლიკატები  დავალაგოტ ციფრები და გავაერთიანოდ ერთ რიცხვად
    return int(''.join(map(str, sorted(set(digits)))))

