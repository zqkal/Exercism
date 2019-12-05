def is_pangram(sentence):
    sentence_given = str(sentence).lower()
    letters = "abcdefghijklmnopqrstuvwxyz"
    result2 = [l for l in letters if l in sentence_given]
    print(result2)
    print(len(result2))
    if len(result2) == 26:
        return True
    else:
        return False
