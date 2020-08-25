import os
import re

file_path1 = os.path.join("raw_data", "paragraph_1.txt")

def paragraphSummary(file_path):
    paragraph = open(file_path, "r")
    
    paragraph = paragraph.read()

    words = paragraph.split(" ")
    word_count = len(words)

    sentences = re.split("(?<=[.!?]) +", paragraph)

    sentence_count = len(sentences)
    print(sentence_count)
    
paragraphSummary(file_path1)