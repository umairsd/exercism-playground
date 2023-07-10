def encode(plain_text):
    encoded_text = [encode_decode_character(c) for c in plain_text]
    encoded_text = ''.join(encoded_text).strip()
    encoded_chunks = [encoded_text[i: i + 5]
                      for i in range(0, len(encoded_text), 5)]

    return ' '.join(encoded_chunks).strip()


def decode(ciphered_text):
    decoded_text = [encode_decode_character(c) for c in ciphered_text]
    return ''.join(decoded_text).strip()


def encode_decode_character(character):
    if character.isdigit():
        return character
    if character.isalpha():
        base = ord('a')
        delta = ord(character.lower()) - base
        flipped = 26 - (delta + 1)
        return chr(base + flipped)

    return ''



print(encode('test'))

print(encode('x123 yes'))
print(decode('gsvjf rxpyi ldmul cqfnk hlevi gsvoz abwlt'))