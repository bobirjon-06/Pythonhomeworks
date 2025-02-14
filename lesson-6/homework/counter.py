import collections
import string

def get_text():
    try:
        with open("sample.txt", "r") as file:
            return file.read()
    except FileNotFoundError:
        print("File not found.")
        content = input("Enter paragraph: ")
        with open("sample.txt", "w") as file:
            file.write(content)
        return content

def count_words(text):
    words = text.translate(str.maketrans('', '', string.punctuation)).lower().split()
    total_words = len(words)
    word_counts = collections.Counter(words)
    return total_words, word_counts

def display_results(total, word_counts, top_n):
    print(f"Total words: {total}")
    print(f"Top {top_n} most common words:")
    for word, count in word_counts.most_common(top_n):
        print(f"{word} - {count} times")

def save_report(total, word_counts, top_n):
    with open("word_count_report.txt", "w") as file:
        file.write("Word Count Report\n")
        file.write(f"Total Words: {total}\n")
        file.write(f"Top {top_n} Words:\n")
        for word, count in word_counts.most_common(top_n):
            file.write(f"{word} - {count}\n")

def main():
    text = get_text()
    total, word_counts = count_words(text)
    top_n = int(input("How many top words to display? ") or 5)
    display_results(total, word_counts, top_n)
    save_report(total, word_counts, top_n)
    print("Report saved to word_count_report.txt")

if __name__ == "__main__":
    main()
