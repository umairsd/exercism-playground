def is_isogram(string):
    character_set = set()
    for c in string.lower():
        if c.isalpha():
            if c in character_set:
                return False
            character_set.add(c)
    return True
