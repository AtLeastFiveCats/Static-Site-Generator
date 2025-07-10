from textnode import TextNode
from textnode import TextType
from extract_links import extract_markdown_images
from extract_links import extract_markdown_links
from split_delimiter import split_nodes_delimiter

def image_testing(old_node):

    list_to_return = []
    #Extracts just the text from the string
    extracted_tuple = extract_markdown_images(old_node.text)
    #Handles incorrect images or textnodes without images
    if extracted_tuple == "":
        return [old_node]
    
    just_image = f"![{extracted_tuple[0]}]({extracted_tuple[1]})"

    split_list = old_node.split(just_image)
    #I realize this will not handle multiple images. I just want to get this function done

    for i in split_list:
        if split_list[i] == "":
            image_node = TextNode(extracted_tuple[0], TextType.IMAGE, extracted_tuple(1))
            list_to_return(image_node)
        else:
            text_node = TextNode(split_list[i], TextType.TEXT)
            list_to_return.append(text_node)
    
    return list_to_return


def split_nodes_links(old_node):

    copied_old_node = old_node
    list_to_return = []
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

def split_nodes_image(old_node):
    copied_old_node = old_node
    list_to_return = []
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


