def translate(text):
    words = text.split()
    return " ".join([transform(word) for word in words])

vowels = ["a", "e", "i", "o", "u"]

def transform(word):
  return pig_rotate(word) + "ay"

def pig_rotate(word):
    starts_with_vowel = word[0] in vowels
    starts_with_qu = word[:2] == "qu"
    starts_with_y_no_vowel = word[0] == "y" and word[1] not in vowels
    starts_with_xr_or_yt = word[:2] in ["xr", "yt"]

    if starts_with_vowel or starts_with_xr_or_yt or starts_with_y_no_vowel:
        return word

    if starts_with_qu:
        return word[2:] + word[:2]

    return pig_rotate(word[1:] + word[0])