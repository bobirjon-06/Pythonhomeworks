import collections
import string

def get_text():
    try:
        with open("sample.txt", "r") as file:
            return file.read().strip()
    except FileNotFoundError:
        content = input("Enter paragraph: ")
        with open("sample.txt", "w") as file:
            file.write(content)
        return content

def count_words(text):
    words = text.translate(str.maketrans('', '', string.punctuation)).lower().split()
    return len(words), collections.Counter(words)

def display_results(total, word_counts, top_n):
    print(f"Total words: {total}")
    for word, count in word_counts.most_common(top_n):
        print(f"{word} - {count}")

def save_report(total, word_counts, top_n):
    with open("word_count_report.txt", "w") as file:
        file.write(f"Total Words: {total}\n")
        for word, count in word_counts.most_common(top_n):
            file.write(f"{word} - {count}\n")

def main():
    text = get_text()
    total, word_counts = count_words(text)
    try:
        top_n = int(input("Top words to display? ") or 5)
    except ValueError:
        top_n = 5
    display_results(total, word_counts, top_n)
    save_report(total, word_counts, top_n)

if __name__ == "__main__":
    main()
