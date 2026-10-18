
def count_words(words):
    count = len(words.split())
    return count


def count_character(words):
    count = len(words.replace(" ", ""))
    return count


def count_vowels_Constants(words):
    vowel = "aeiou"
    constants = "bcdfghjklmnpqrstvwxyz"

    count_vowel = 0
    count_constant = 0

    for character in words.lower():
        if character in vowel:
            count_vowel += 1
        elif character in constants:
            count_constant += 1

    return count_vowel, count_constant


def clean_text(words):
    punctuation = ".,!?;:()[]{}\"'"
    words = words.lower()

    for character in punctuation:
        words = words.replace(character, "")

    return words


def find_longest(words):
    words = clean_text(words).split()

    if len(words) == 0:
        return ""

    longest = words[0]

    for word in words:
        if len(word) > len(longest):
            longest = word

    return longest


def count_each_word(words):
    words = clean_text(words).split()
    word_counts = {}

    for word in words:
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1

    return word_counts


def find_repeated_words(words):
    word_counts = count_each_word(words)
    repeated = []

    for word in word_counts:
        if word_counts[word] > 1:
            repeated.append(word)

    return repeated


def five_most_frequent(words):
    word_counts = count_each_word(words)
    frequent = []

    for word in word_counts:
        frequent.append([word, word_counts[word]])

    frequent.sort(key=lambda item: item[1], reverse=True)

    return frequent[:5]


def analyze_text(words):
    print("Text Statistics and Word Analyzer")
    print("---------------------------------")
    print("Words:", count_words(clean_text(words)))
    print("Characters excluding spaces:", count_character(words))
    print("Vowels and consonants:", count_vowels_Constants(words))
    print("Longest word:", find_longest(words))
    print("Word frequencies:", count_each_word(words))
    print("Repeated words:", find_repeated_words(words))
    print("Five most frequent words:", five_most_frequent(words))


text = "Python is useful and Python is powerful."

analyze_text(text)
