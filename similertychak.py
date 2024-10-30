import plagchaker_linklist

def similarity(list1, list2):
    current1 = list1.head
    current2 = list2.head
    match_count = 0
    total_count = 0
    

    while current1:
        total_count += 1
        current1 = current1.next
        
    while current2:
        total_count += 1
        current2 = current2.next


    current1 = list1.head
    current2 = list2.head


    while current1 and current2:
        if current1.data == current2.data:
            match_count += 1
            current1 = current1.next
            current2 = current2.next
        elif current1.data < current2.data:
            current1 = current1.next
        else:
            current2 = current2.next


    if total_count > 0:
        similarity_score = (2 * match_count) / total_count
    else:
        similarity_score = 0

    return similarity_score * 100
