def prefix(string1, string2):
    string1 = string1.lower()
    string2 = string2.lower()

    i = 0

    limit = min(len(string1), len(string2))
    while i < limit:
        if string1[i] != string2[i]:
           break
        i += 1
    pre = string1[0 : i]
    return pre


def suffix(string1, string2):
    string1 = string1.lower()
    string2 = string2.lower()

    i1 = len(string1) - 1
    i2 = len(string2) - 1

    limit = min(len(string1), len(string2))
    for _ in range(limit):
        if string1[i1] != string2[i2]:
            break
        i1 -= 1
        i2 -= 1

    suf = string1[i1+1 : ]
    return suf