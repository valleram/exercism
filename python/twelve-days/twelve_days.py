days = [
    "first",
    "second",
    "third",
    "fourth",
    "fifth",
    "sixth",
    "seventh",
    "eighth",
    "ninth",
    "tenth",
    "eleventh",
    "twelfth"
]

gifts = [
    "a Partridge in a Pear Tree.",
    "two Turtle Doves, and",
    "three French Hens,",
    "four Calling Birds,",
    "five Gold Rings,",
    "six Geese-a-Laying,",
    "seven Swans-a-Swimming,",
    "eight Maids-a-Milking,",
    "nine Ladies Dancing,",
    "ten Lords-a-Leaping,",
    "eleven Pipers Piping,",
    "twelve Drummers Drumming,"
]


def recite(start_verse, end_verse):
    start_verse = start_verse - 1
    end_verse = end_verse - 1
    first_part = [f"On the {days[i]} day of Christmas my true love gave to me: " for i in
                  range(end_verse, start_verse-1, -1)]
    second_part = [" ".join(gifts[i::-1]) for i in range(end_verse, start_verse - 1, -1)]
    final_verse = ["".join(first_part[i] + second_part[i]) for i in range(len(first_part))]
    return final_verse[::-1]
