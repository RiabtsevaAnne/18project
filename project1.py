import matplotlib.pyplot as plt
import string

def histogram(file_path):
    letter_freq = {letter: 0 for letter in string.ascii_lowercase}

    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read().lower()

        for char in content:
            if char.isalpha():
                letter_freq[char] += 1

    letters = list(letter_freq.keys())
    freq = list(letter_freq.values())

    plt.bar(letters, freq)
    plt.xlabel('Літера')
    plt.ylabel('Частота')
    plt.title('Гістограма частот англійських літер')
    plt.show()

histogram('phantomoftheopera.txt')
