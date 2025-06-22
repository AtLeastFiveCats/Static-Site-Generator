from textnode import TextNode
from textnode import TextType

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes =[]
    processed_nodes = ""
    for node in old_nodes:
        if text_type != "TextType.TEXT":
            new_textnode = TextNode(node.text, text_type, node.url)
            new_nodes.extend(new_textnode)
        
        
        if "```" in node.text:
            deli_indicator = TextType.CODE

        if "**" in node.text:
            deli_indicator = TextType.BOLD

        if "__" in node.text:
            deli_indicator = TextType.ITALIC

        if "#" in node.text:
            deli_indicator = TextType.HEADING

        if "[]" in node.text:
            deli_indicator = TextType.LINK

        if "![]" in node.text:
            deli_indicator = TextType.IMAGE

        if "-" in node.text:
            deli_indicator = TextType.UNORDERED_LIST

        if "1." in node.text:
            deli_indicator = TextType.ORDER_LIST

        if ">" in node.text:
            deli_indicator = TextType.QUOTE

        split_node = node.text.split(delimiter)
    

