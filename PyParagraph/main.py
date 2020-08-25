import os
import re
import numpy as np

file_path1 = os.path.join("raw_data", "paragraph_1.txt")


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

    print(avg_letter_count)

paragraphSummary(file_path1)