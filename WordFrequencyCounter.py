# Word Frequency Counter
def clean_text(text):
    # Remove punctuation and convert to lowercase
    punctuation = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    cleaned = ""
    for char in text:
        if char not in punctuation:
            cleaned += char.lower()
    return cleaned

def count_words(filename):
    try:
        with open(filename, 'r') as file:
            text = file.read()
            text = clean_text(text)
            words = text.split()

            word_count = {}

            for word in words:
                if word in word_count:
                    word_count[word] += 1
                else:
                    word_count[word] = 1

            # Sort dictionary by values (frequency) in descending order
            sorted_words = sorted(word_count.items(), key=lambda x: x[1], reverse=True)

            print("\nTop 5 most frequent words:\n")
            for word, freq in sorted_words[:5]:
                print(f"{word} : {freq}")

    except FileNotFoundError:
        print("Error: File not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage:
filename = input("Enter the text file name (e.g., sample.txt): ")
count_words(filename)
