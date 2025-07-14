from textnode import TextNode
from textnode import TextType

def split_nodes_delimiter(nodes, delimiter, text_type):
    new_nodes =[]
    deli_indicator = TextType.TEXT

    for old_nodes in nodes:
        if old_nodes.text_type != TextType.TEXT:
            new_nodes.append(old_nodes)

        if "```" in old_nodes.text:
            deli_indicator = TextType.CODE

        if "**" in old_nodes.text:
            deli_indicator = TextType.BOLD
        
        if "__" in old_nodes.text:
            deli_indicator = TextType.ITALIC

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

