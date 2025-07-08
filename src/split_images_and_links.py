from textnode import TextNode
from textnode import TextType
from extract_links import extract_markdown_images
from extract_links import extract_markdown_links
from split_delimiter import split_nodes_delimiter

def split_nodes_image(old_node):

    list_to_return = []
    #Extracts just the text from the string
    extracted_tuple = extract_markdown_images(old_node)
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
    
    list_to_return = []

    extracted_tuple = extract_markdown_link(old_node)
    if extracted_tuple == "":
        return [old_node]

    just_link = f"[{extracted_tuple[0]}]({extracted_tuple[1]})"
    split_list = old_node.split(just_link)
    
    for i in split_list:
        if split_list[i] == "":
            link_node = TextNode(extracted_tuple[0], TextType.LINK, extracted_tuple[1])
            list_to_return.append(link_node)
        else:
            text_node = TextNode(split_list[i], TextType.TEXT)
            list_to_return.append(text_node)

    return list_to_return

