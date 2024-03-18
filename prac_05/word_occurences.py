"""
Word Occurrences
Estimate: 15 minutes
Actual: 20 minutes
"""

word = input("Text: ")
words = word.split()
word_count = {}
for word in words:
    word = word.lower()
    word_count[word] = word_count.get(word, 0) + 1

words = list(word_count.keys())
words.sort()

max_length = max((len(word) for word in words))

for word in words:
    print(f"{word:{max_length}}: {word_count[word]}")