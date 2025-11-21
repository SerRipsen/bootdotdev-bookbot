from stats import count_words, count_characters, create_report


def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

def main():
    path_to_book = "./books/frankenstein.txt"
    book = get_book_text(f"{path_to_book}")

    word_count = count_words(book)
    char_count = count_characters(book)
    report = create_report(char_count)
    
    # Output the final report to the terminal
    print(
        "============ BOOKBOT ============\n",
        f"Analyzing book found at {path_to_book}...\n",
        "----------- Word Count ----------\n",
        f"Found {word_count} total words\n",
        "--------- Character Count -------")
    
    for pair in report:
        k0, v0 = list(pair.items())[0]
        k1, v1 = list(pair.items())[1]
        if v0.isalpha():
            print(f"{v0}: {v1}")

    
    print("============= END ===============")

main()
