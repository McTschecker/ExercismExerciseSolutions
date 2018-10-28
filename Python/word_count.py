def word_count(phrase):
    count = {}
    for c in phrase:
        if not c.isalpha() and not c.isdigit() and c != "'":
            phrase = phrase.replace(c, " ")
    for word in phrase.lower().split():
        word = word.strip("\'")
        if word not in count:
            count[word] = 1
        else:
            count[word] += 1
    return count