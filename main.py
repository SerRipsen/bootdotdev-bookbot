def count_words(text):
    word_list = text.split()
    return len(word_list)


def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

def main():
    path_to_books = "./books"
    books = get_book_text(f"{path_to_books}/frankenstein.txt")
    count = count_words(books)
    print(count)

main()
