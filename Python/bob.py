def hey(phrase):
    phrase = phrase.strip()
    if phrase.endswith("?"):
        if phrase.isupper():
            return "Calm down, I know what I'm doing!"
        else:
            return "Sure."
    else:
        if phrase == "" or phrase == " ":
            return 'Fine. Be that way!'
        elif phrase.isupper():
            return 'Whoa, chill out!'
        else:
            return "Whatever."