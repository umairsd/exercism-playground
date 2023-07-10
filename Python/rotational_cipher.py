def rotate(text, key):
    return "".join(rotate_character(c, key) for c in text)


def rotate_character(character, key):
    if not character.isalpha():
        return character

    start = ord('A') if character.isupper() else ord('a')
    x = ord(character) - start
    x = (x + key) % 26
    return chr(x + start)
