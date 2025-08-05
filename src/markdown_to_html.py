from blocktype import BlockType
from blocktype import block_to_block_type
from split_blocks import markdown_block_splitter
from htmlnode import HTMLNode
from text_to_node import markdown_to_textnode
from textnode import TextType
from enum import Enum

# Func to split text into blocks
def markdown_to_blocks(markdown: str):
    Types = Enum("Types", ["BlockType.PARAGRAPH", "BlockType.HEADING", "BlockType.CODE", "BlockType.QUOTE", "BlockType.UNORDERED_LIST", "BlockType.ORDERED_LIST"])

    grandparent_html_list: list = []
    blocks: list = markdown_block_splitter(markdown)
    for block in blocks:
        block_type: str = block_to_block_type(block)
        match block_type:
            case Types.PARAGRAPH:
                parent_wrapper_node = HTMLNode(children = para_to_html(block))
            case Types.HEADING:
                parent_wrapper_node = HTMLNode(children = heading_to_html(block))
            case Types.QUOTE:
                parent_wrapper_node = HTMLNode(children = quote_md_to_html(block))
            case Types.CODE:
                parent_wrapper_node = HTMLNode(value = "<pre></pre>", children = code_md_to_html(block))
            case Types.UNORDERED_LIST:
                parent_wrapper_node = HTMLNode(value = "<ul></ul>", children = uo_list_to_html(block))
            case Types.ORDERED_LIST:
                parent_wrapper_node = HTMLNode(value = "<ol></ol>", children = o_list_to_html(block))
        parent_wrapper_node.children: list = inline_to_html(parent_wrapper_node, block_type)
        grandparent_html_list.append(parent_wrapper_node)
    grandparent_html_node = HTMLNode(value = "<div></div>", children = grandparent_html_list)
    return grandparent_html_node


# Func to deal with inline
def inline_to_html(block, block_type):
    child_nodes: list = []    
    if block_type == BlockType.CODE:
        return code_md_to_html(block)
    markdown_nodes: list = markdown_to_textnode(block)
    # Converts the markdown blocks into child html nodes and appends them to a list to be assigned to a parent html node
    for node in markdown_nodes:
        child_html_node = HTMLNode(node.text, node.TextType)
        child_nodes.append(child_html_node)
    return child_nodes

# Dealing with code blocks
def code_md_to_html(block: str):
    clean_block: str = block.replace("```", "")
    return f"<code>{clean_block}</code>"
    # Need to nest code inside a html node with pre tag

# Quote to html
def quote_md_to_html(block: str):
    front_tag: str = block.replace("> ", "<blockquote>")
    return f"{front_tag}</blockquote>"

# Unordered lists to html
def uo_list_to_html(block: str):
    front_tag: str = block.replace("- ", "<li>")
    return f"{front_tag}</li>"
    # Need to nest inside a html node with ul tag

# Ordered list to html
def o_list_to_html(block: str):
    split_block: list = block.split("\n")
    fixed_tags: list = [f"<li>{line}</li>" for line in split_block]
    return fixed_tags
    # Need to nest this inside a html node with ol tag

# Headings to html
def heading_to_html(block: str):
    heading: str = ""
    for i: int in range(6):
        heading += "#"
        if block.startswith(f"{heading} "):
            return f"<h{i}>{block}{</h{i}>}"

# Paragraph to html
def para_to_html(block: str):
    return f"<p>{block}</p>"

