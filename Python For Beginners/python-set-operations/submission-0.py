from typing import List

def count_unique_words(words: List[str]) -> int:
    list_set = set(words)
    if len(list_set) == 0:
        return 0
    else:
        return len(list_set)

# do not modify code below this line
print(count_unique_words(["hello", "world", "hello", "goodbye"]))
print(count_unique_words(["hello", "world", "i", "am", "world"]))
print(count_unique_words(["hello", "hello", "hello"]))
print(count_unique_words([]))
