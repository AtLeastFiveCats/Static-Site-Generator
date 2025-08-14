from blocktype import BlockType
from blocktype import block_to_block_type
from split_blocks import markdown_block_splitter
from htmlnode import HTMLNode
from text_to_nodes import markdown_to_textnode
from textnode import TextType
from enum import Enum
from parentnode import ParentNode
from leafnode import LeafNode

# Func to split text into blocks
def markdown_to_blocks(markdown: str):

    grandparent_html_list: list = []
    blocks: list = markdown_block_splitter(markdown)
    for block in blocks:
        block_type: str = block_to_block_type(block)
        match block_type:
            case BlockType.PARAGRAPH:
                parent_wrapper_node = LeafNode(value = None, children = para_to_html(block))
            case BlockType.HEADING:
                parent_wrapper_node = LeafNode(value = None, children = heading_to_html(block))
            case BlockType.QUOTE:
                parent_wrapper_node = LeafNode(value = None, children = quote_md_to_html(block))
            case BlockType.CODE:
                parent_wrapper_node = ParentNode(tag = "<pre></pre>", children = code_md_to_html(block))
            case BlockType.UNORDERED_LIST:
                parent_wrapper_node = ParentNode(tag = "<ul></ul>", children = uo_list_to_html(block))
            case BlockType.ORDERED_LIST:
                parent_wrapper_node = ParentNode(tag = "<ol></ol>", children = o_list_to_html(block))
        if block_type != BlockType.CODE: 
            parent_wrapper_node.children: list = inline_to_html(block)
        grandparent_html_list.append(parent_wrapper_node)
    grandparent_html_node = ParentNode(tag = "<div></div>", children = grandparent_html_list)
    return grandparent_html_node


# Func to deal with inline
def inline_to_html(block):
    child_nodes: list = []    
    markdown_nodes: list = markdown_to_textnode(block)
    # Converts the markdown blocks into child html nodes and appends them to a list to be assigned to a parent html node
    for node in markdown_nodes:
        child_html_node = HTMLNode(node.text, node.text_type)
        child_nodes.append(child_html_node)
    return child_nodes

# Dealing with code blocks
def code_md_to_html(text: str):
    clean_text: str = text.replace("```", "")
    return f"<code>{clean_text}</code>"
    # Need to nest code inside a html node with pre tag

# Quote to html
def quote_md_to_html(text: str):
    front_tag: str = text.replace("> ", "<blockquote>")
    return f"{front_tag}</blockquote>"

# Unordered lists to html
def uo_list_to_html(text: str):
    front_tag: str = text.replace("- ", "<li>")
    return f"{front_tag}</li>"
    # Need to nest inside a html node with ul tag

# Ordered list to html
def o_list_to_html(text: str):
    split_block: list = text.split("\n")
    fixed_tags: list = [f"<li>{line}</li>" for line in split_block]
    return fixed_tags
    # Need to nest this inside a html node with ol tag

# Headings to html
def heading_to_html(text: str):
    heading: str = ""
    for i in range(6):
        heading += "#"
        if text.startswith(f"{heading} "):
            return f"<h{i}>{text}</h{i}>"

# Paragraph to html
def para_to_html(text: str):
    return f"<p>{text}</p>"

