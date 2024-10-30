import re
import plagchaker_linklist 

def preprocess(text):

    text = text.lower()
    text = re.sub(r'\W', ' ', text)
    text = re.sub(r'\s+', ' ', text)
    return text.split()

def linklist_txt(text):

    linked_list = plagchaker_linklist.LinkedList()
    for word in text:
        linked_list.append(word)
    return linked_list

def read_text(filepath):

    try:
        with open(filepath, 'r', encoding='utf-8') as file:
            content = file.read()
        return content
    except FileNotFoundError:
        print(f"Error: The file '{filepath}' was not found.")
        return ""
