def no_dups(s):
    # Split string
    # Iterate split string into dict
    # Iterate list(dict) into string via append

    s = s.split()
    words = {}
    new_s = ""
    for w in s:
        words[w] = None
    
    for w in list(words):
        new_s += w
        if len(new_s.split()) < len(list(words)):
            new_s += " "
    
    return new_s




if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))