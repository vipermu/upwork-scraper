import re

def text(text: str):
    text = text.strip().lower()
    word_list = re.split('\W+', text)
    word_list = [word for word in word_list
                 if len(word) > 2 and not word.isdigit()]
    text = ' '.join(word_list)
    return text
