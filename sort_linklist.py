from plagchaker_linklist import LinkedList, Node

def merge_sort(head):
    if not head or not head.next:
        return head
    
    mid = get_middle(head)
    next_mid = mid.next
    mid.next = None  

    left = merge_sort(head)       
    right = merge_sort(next_mid)  
    
    return sorted_merge(left, right)  

def get_middle(head):
    if not head:
        return head
    
    first = head
    last = head.next
    
    while last and last.next:
        first = first.next
        last = last.next.next
    
    return first

def sorted_merge(left, right):
    if not left:
        return right
    if not right:
        return left
    
    if left.data < right.data:
        result = left
        result.next = sorted_merge(left.next, right)
    else:
        result = right
        result.next = sorted_merge(left, right.next)
    
    return result

def sort_linklist(linked_list):
    linked_list.head = merge_sort(linked_list.head)
