import os

file_path = os.path.join("raw_data", "paragraph_1.txt")

paragraph = open(file_path, "r")

print(paragraph.read())