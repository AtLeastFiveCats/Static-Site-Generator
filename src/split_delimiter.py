from textnode import TextNode
from textnode import TextType

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes =[]
    if old_nodes.TextType != TextType.TEXT:
        new_nodes.append(old_nodes)

    split_nodes = old_nodes.split(delimiter)
    for node in split_nodes:
        
'''

If old is not textype.text extend it to the list as is
Split the old nodes on the given delimiter
If there is not a matching closing delimiter raise an exception
Loop through the split nodes
If a node matches the delimiter remove it
Create a new textnode with the current node and add the correct textype to it
Extend the newly made textnode to the list
Return the list

'''

