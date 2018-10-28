def verify(isbn):
    last_int = 0 # will be used if last element is X
    total = 0
    mult = 10 # mutiplier value
    isbn = isbn.replace('-', "").upper()

    if len(isbn) != 10: # check length of ISBN
        return False
    else:
        if isbn[-1] == "X": #check if last "digit" is an X
            last_int = 10
            isbn = isbn.replace("X", "") # replace final X if there is one

        try:
            for i in range(len(isbn)): #applying the formula
                total = total + int(isbn[i])*mult
                mult -= 1 #everytime a digit is added times its multiplier, the multiplier decreases
        except: #if error, such as a letter in the ISBN, false
            return False

        total += last_int #add final digit if it was X
        if total%11 == 0:
            return True
        else:
            return False