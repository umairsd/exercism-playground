VERSE = 'On the %s day of Christmas my true love gave to me: %s'
DAYS = ('zero', 'first', 'second', 'third', 'fourth', 'fifth', 'sixth',
        'seventh', 'eighth', 'ninth', 'tenth', 'eleventh', 'twelfth')
GIFTS = ("twelve Drummers Drumming, ", "eleven Pipers Piping, ",
         "ten Lords-a-Leaping, ", "nine Ladies Dancing, ",
         "eight Maids-a-Milking, ", "seven Swans-a-Swimming, ",
         "six Geese-a-Laying, ", "five Gold Rings, ",
         "four Calling Birds, ", "three French Hens, ",
         "two Turtle Doves, and ", "a Partridge in a Pear Tree.")


def recite(start_verse, end_verse):
    return [VERSE % (DAYS[i], "".join(GIFTS[-i:]))
            for i in range(start_verse, end_verse + 1)]
