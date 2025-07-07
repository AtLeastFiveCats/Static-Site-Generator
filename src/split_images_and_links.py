from textnode import TextNode
from textnode import TextType
from extract_links import extract_markdown_images
from extract_links import extract_markdown_links
from split_delimiter import split_nodes_delimiter

def split_nodes_image(old_node):

    #Extracts just the text from the string
    just_image = extract_markdown_images(old_node)
    #Handles incorrect images or textnodes without images
    if just_image = "":
        return [old_node]

    split_list = old_node.split(just_image)
    #I realize this will not handle multiple images. I just want to get this function done

    for i in split_list:
        if split_list[i] == just_image:
            


def split_nodes_links(old_node):
    

