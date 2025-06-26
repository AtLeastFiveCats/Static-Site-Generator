from textnode import TextNode
from textnode import TextType

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes =[]
    deli_indicator = TextType.TEXT

    if old_nodes.text_type != TextType.TEXT:
        new_nodes.append(old_nodes)

    if "```" in old_nodes.text:
        deli_indicator = TextType.CODE

    if "**" in old_nodes.text:
        deli_indicator = TextType.BOLD
        
    if "__" in old_nodes.text:
        deli_indicator = TextType.ITALIC

    if "[" in old_nodes.text:
        deli_indicator = TextType.LINK

    if "![" in old_nodes.text:
        deli_indicator = TextType.IMAGE

    split_nodes = old_nodes.text.split(delimiter)
   
    if len(split_nodes) % 2 == 0:
        raise Exception("Invalid markdown, please use a closing delimiter")
    
    for i in range(len(split_nodes)):
        if i % 2 == 0:
            new_text = TextNode(split_nodes[i], TextType.TEXT)
        if i % 2 != 0:
            new_text = TextNode(split_nodes[i], deli_indicator)
        
        new_nodes.append(new_text)

    return new_nodes
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

