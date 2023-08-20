def generate_sentences(word_lists, current_sentence, index, result):
    if index == len(word_lists):
        result.append(" ".join(current_sentence))
        return
    
    for word in word_lists[index]:
        current_sentence.append(word)
        generate_sentences(word_lists, current_sentence, index + 1, result)
        current_sentence.pop()

def print_all_sentences(word_lists):
    result = []
    generate_sentences(word_lists, [], 0, result)
    
    for sentence in result:
        print(sentence)

# Example usage
word_lists = [
    ["I", "You"],
    ["love", "hate"],
    ["programming", "coding"]
]

print_all_sentences(word_lists)
