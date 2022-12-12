def pangrams(s):
    final = set(s.lower()) - set(' ')

    if len(final) == 26:
        return 'pangram'
    else:
        return 'not pangram'
