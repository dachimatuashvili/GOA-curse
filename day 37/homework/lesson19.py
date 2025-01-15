def array(string):

    parts = string.split(',')
    
    if len(parts) <= 2:
        return None
    
    return ' '.join(parts[1:-1])





def temple_strings(obj, feature):
    return f"{obj} are {feature}"





def contamination(text, char):
    if not text or not char:
        return ""
    return char * len(text)
  




def is_palindrome(s):
    return s.lower() == s.lower()[::-1]





def obfuscate(email):
    return email.replace('@', ' [at] ').replace('.', ' [dot] ')



