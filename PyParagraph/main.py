import os
import re
import numpy as np

file_path1 = os.path.join("raw_data", "paragraph_1.txt")

file_path2 = os.path.join("raw_data", "paragraph_2.txt")


def paragraphSummary(file_path):
    paragraph = open(file_path, "r")
    
    paragraph = paragraph.read()

    words = paragraph.split(" ")
    word_count = len(words)

    sentences = re.split("(?<=[.!?]) +", paragraph)
    sentence_count = len(sentences)

    word_lengths = []

    for i in np.arange(0, word_count):
        word_length = len(words[i])
        word_lengths.append(word_length)
    
    avg_letter_count = round(np.mean(word_lengths), 1)

    sentence_lengths = []

    for i in np.arange(0, sentence_count):
        sentence_length = sentences[i].split(" ")
        sentence_length = len(sentence_length)
        sentence_lengths.append(sentence_length)
    
    avg_sentence_length = np.mean(sentence_lengths)

    print("Paragraph Analysis")
    print("-----------------")
    print(f"Approximate Word Count: {word_count}")
    print(f"Approximate Sentence Count: {sentence_count}")
    print(f"Average Letter Count: {avg_letter_count}")
    print(f"Average Sentence Count: {avg_sentence_length}")

paragraphSummary(file_path1)
print("")
paragraphSummary(file_path2)