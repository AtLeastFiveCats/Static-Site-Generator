from textnode import TextNode
from textnode import TextType
from split_delimiter import split_nodes_delimiter
from split_images_and_links import split_nodes_image
from split_images_and_links import split_nodes_links
import extract_links

def markdown_to_textnode(text):
    new_node = [TextNode(text, TextType.TEXT)]
    
    inline_node = split_nodes_delimiter(new_node, "```", TextType.TEXT)       
    inline_node = split_nodes_delimiter(inline_node, "**", TextType.TEXT)
    inline_node = split_nodes_delimiter(inline_node, "__", TextType.TEXT) 
    
    image_node = split_nodes_image(inline_node)
    link_node = split_nodes_links(image_node)
    return link_node

