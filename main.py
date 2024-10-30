import preprocess
from similertychak import similarity
import sort_linklist

def maiin():
    print("Welcome to Plagchaker")
    print("Enter the path of the first file:")
    filepath1 = input()
    print("Enter the path of the second file:")
    filepath2 = input()


    doc1 = preprocess.read_text(filepath1)
    doc2 = preprocess.read_text(filepath2)
    
    if not doc1 or not doc2:
        print("One or both files could not be read. Please check the file paths.")
        return
    
    file1 = preprocess.preprocess(doc1)
    file2 = preprocess.preprocess(doc2)


    list1 = preprocess.linklist_txt(file1)
    list2 = preprocess.linklist_txt(file2)


    sort_linklist.sort_linklist(list1)
    sort_linklist.sort_linklist(list2)


    similarity_score = similarity(list1, list2)
    print(f"The similarity between the two files is: {similarity_score:.2f}%")


maiin()
