def is_pangram(sentence):
    character_set = set("abcdefghijklmnopqrstuvwxyz")
    for c in sentence.lower():
        character_set.discard(c)

    return len(character_set) == 0


print(is_pangram("the quick brown fox jumps over the lazy dog"))