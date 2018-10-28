def is_isogram(string):
    count = {}
    isogram = 1 # 1 = true; 0 = false
    if type(string) != str:
        raise TypeError('A string is required.')
    if string == "":
        return True
    for letter in string.strip().lower().replace(" ", "").replace("-", ""):
        if letter in count:
            count[letter] += 1
        else:
            count[letter] = 1
    for each in count.values():
        if each > 1:
            isogram = 0
    if isogram == 0:
        return False
    else:
        return True