def find_substring_iter(needle, haystack):
    i = 0

    while (i < len(haystack)):
        substr = haystack[i : i + len(needle)]
        print(substr)
        if substr == needle:
            return i
        i += 1

    return -1

i = find_substring_iter('cat', 'My cat zophie')
print(i)

def find_substring_recur(needle, haystack, i = 0):

    if i > len(haystack):
        return -1

    if haystack[i : i + len(needle)] == needle:
        return i

    return find_substring_recur(needle, haystack, i + 1)


i = find_substring_recur('cat', 'My cat zophie')
print(i)