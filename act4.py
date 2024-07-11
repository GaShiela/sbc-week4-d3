sentence_list = []
input_text = input("Enter a sentence or multiple sentences: ")

def process_sentences(input_text):
    sentences = []
    temp = ""
    for char in input_text:
        if char in ['.', '', '']:
            sentences.append(temp.strip())
            temp = ""
        else:
            temp += char
    if temp:
        sentences.append(temp.strip())
    return sentences