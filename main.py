from stats import count_words


def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

def main():
    path_to_books = "./books"
    books = get_book_text(f"{path_to_books}/frankenstein.txt")
    count = count_words(books)
    print(f"Found {count} total words")

main()
