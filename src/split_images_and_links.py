from textnode import TextNode
from textnode import TextType
from extract_links import extract_markdown_images
from extract_links import extract_markdown_links
from split_delimiter import split_nodes_delimiter

def split_nodes_links(node_list):
    
    list_to_return = []
    if not node_list:
        return []
   
    for old_node in node_list:
        if old_node.text_type != TextType.TEXT:
            list_to_return.append(old_node)
        else:
            copied_old_node = old_node.text
            extracted_tuple = extract_markdown_links(copied_old_node)
            for current_tuple in extracted_tuple:
                alt_text, url = current_tuple
                markdown_link = f"[{alt_text}]({url})"
            #Split the textnode once based on where the link was and create a textnode before that point and a link node after that point
                split_list = copied_old_node.split(markdown_link, maxsplit=1)
                text_node = TextNode(split_list[0], TextType.TEXT)
                link_node = TextNode(alt_text, TextType.LINK, url)
            #Then append both the list and assign the old node the section that wasn't split
                list_to_return.append(text_node)
                list_to_return.append(link_node)
                copied_old_node = split_list[1]

            if copied_old_node != "":
                text_node = TextNode(copied_old_node, TextType.TEXT)
                list_to_return.append(text_node)

    return list_to_return

def split_nodes_image(node_list):
    if not node_list:
        return []

    list_to_return = []   
    
    for old_node in node_list:
        if old_node.text_type != TextType.TEXT:
            list_to_return.append(old_node)
        else:
            copied_old_node = old_node.text
            extracted_tuple = extract_markdown_images(copied_old_node)
        
            for current_tuple in extracted_tuple:
                alt_text, url = current_tuple
                markdown_image = f"![{alt_text}]({url})"
                split_list = copied_old_node.split(markdown_image, maxsplit=1)
                text_node = TextNode(split_list[0], TextType.TEXT)
                image_node = TextNode(alt_text, TextType.IMAGE, url)

                list_to_return.append(text_node)
                list_to_return.append(image_node)
                copied_old_node = split_list[1]
   
            #Checking if the old node has any string left to append 
            if copied_old_node: 
                text_node = TextNode(copied_old_node, TextType.TEXT)
                list_to_return.append(text_node)

    return list_to_return


