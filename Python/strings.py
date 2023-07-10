"""Functions for creating, transforming, and adding prefixes to strings."""


def add_prefix_un(word):
    """Take the given word and add the 'un' prefix.

    :param word: str - containing the root word.
    :return: str - of root word prepended with 'un'.
    """
    return 'un' + word


def make_word_groups(vocab_words):
    """Transform a list containing a prefix and words into a string with the prefix followed by the words with prefix prepended.

    :param vocab_words: list - of vocabulary words with prefix in first index.
    :return: str - of prefix followed by vocabulary words with
            prefix applied.

    This function takes a `vocab_words` list and returns a string
    with the prefix and the words with prefix applied, separated
     by ' :: '.

    For example: list('en', 'close', 'joy', 'lighten'),
    produces the following string: 'en :: enclose :: enjoy :: enlighten'.
    """
    prefix = vocab_words[0]
    words = vocab_words[1:]

    words_with_prefix = " :: ".join([prefix + w for w in words])
    return prefix + " :: " + words_with_prefix


def remove_suffix_ness(word):
    """Remove the suffix from the word while keeping spelling in mind.

    :param word: str - of word to remove suffix from.
    :return: str - of word with suffix removed & spelling adjusted.

    For example: "heaviness" becomes "heavy", but "sadness" becomes "sad".
    """

    without_ness = word[:-4]
    if without_ness[-1] == 'i':
        return without_ness[:-1] + 'y'

    return without_ness


def adjective_to_verb(sentence, index):
    """Change the adjective within the sentence to a verb.

    :param sentence: str - that uses the word in sentence.
    :param index: int - index of the word to remove and transform.
    :return: str - word that changes the extracted adjective to a verb.

    For example, ("It got dark as the sun set", 2) becomes "darken".
    """

    word = sentence.split()[index].strip('.,')
    return word + 'en'

input_data = ['Look at the bright sky.',
              'His expression went dark.',
              'The bread got hard after sitting out.',
              'The butter got soft in the sun.',
              'Her eyes were light blue.',
              'The morning fog made everything damp with mist.',
              'He cut the fence pickets short by mistake.',
              'Charles made weak crying noises.',
              'The black oil got on the white dog.']
index_data = [-2, -1, 3, 3, -2, -3, 5, 2, 1]
result_data = ['brighten', 'darken', 'harden', 'soften',
               'lighten', 'dampen', 'shorten', 'weaken', 'blacken']
number_of_variants = range(1, len(input_data) + 1)

for variant, sentence, index, result in zip(number_of_variants, input_data, index_data, result_data):
    print(adjective_to_verb(sentence, index))