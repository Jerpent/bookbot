def count_words(text):
    return len(text.split())

def count_letters(text):
    text = text.lower()
    letter_count = {}
    for letter in text:
        if letter.isalpha():
            letter_count[letter] = letter_count.get(letter, 0) + 1
    return letter_count


