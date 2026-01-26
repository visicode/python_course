# WRITE YOUR SOLUTION HERE:
class Node:
    """ Class is modeling single node in binary tree """
    def __init__(self, value, left_child:'Node' = None, right_child:'Node' = None):
        self.value = value
        self.left_child = left_child
        self.right_child = right_child

def greatest_node(tr: Node)->int:
    gr=tr.value
    if tr.left_child!=None:
        ret=greatest_node(tr.left_child)
        if ret>gr:
            gr=ret
    if tr.right_child!=None:
        ret=greatest_node(tr.right_child)
        if ret>gr:
            gr=ret
    return gr
    
