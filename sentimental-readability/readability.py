"""
Recall that the Coleman-Liau index is computed as 0.0588 * L - 0.296 * S - 15.8, where L
is the average number of letters per 100 words in the text, and S is the average number
of sentences per 100 words in the text.
"""

# iniciate variables
alpha_count = 0
word_count = 1
sentence_count = 0


def main():
    text = input("Text: ").lower()
    alpha_count, sentence_count, word_count = update_counters(text)
    coleman_index = get_coleman_index(alpha_count, sentence_count, word_count)
    # conditional output
    if coleman_index < 1:
        print("Before Grade 1")
    elif coleman_index > 16:
        print("Grade 16+")
    else:
        print(f"Grade {coleman_index}")


def get_coleman_index(alpha_count, sentence_count, word_count):
    # define S, L and coleman index
    cole_l = alpha_count * 100 / word_count
    cole_s = sentence_count * 100 / word_count
    coleman_index = round(0.0588 * cole_l - 0.296 * cole_s - 15.8)
    return coleman_index


def update_counters(text):
    global alpha_count
    global word_count
    global sentence_count
    # loop through text to find characters and add count
    for char in text:
        if char.isalpha():
            alpha_count += 1
        if char == "." or char == "!" or char == "?":
            sentence_count += 1
        if char == " ":
            word_count += 1
    return alpha_count, sentence_count, word_count


if __name__ == "__main__":
    main()

