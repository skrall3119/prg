# Program 8.3 finds the most common letter in a given string.
def most_freq_char(word):

    char_set = ''.join(sorted(word))

    max_count = 0
    max_char = None

    for letter in char_set.lower():         # counts the number of times a letter appears in a string,
                                            #  and sets the max when finished
        let_count = word.count(letter)

        if let_count > max_count:
            max_count = let_count
            max_char = letter

    print(max_char, max_count)

most_freq_char('banana')
