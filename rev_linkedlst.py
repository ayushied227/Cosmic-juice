# reverse linked list question by google

import Node

def reverseList(head : Node):
    prev = None
    curr = head

    while curr:
        temp_next = curr.next
        curr.next = prev
        prev = curr 
        curr = temp_next
    return prev
