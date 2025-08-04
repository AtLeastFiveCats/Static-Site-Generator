from blocktype import BlockType
from blocktype import block_to_block_type
from split_blocks import markdown_block_splitter
from htmlnode import HTMLNode
from text_to_node import markdown_to_textnode
from textnode import TextType

# Func to split text into blocks
def markdown_to_blocks(markdown: str):
    parent_html_node = []
    blocks: list = markdown_block_splitter(markdown)
    for block in blocks:
        block_type: str = block_to_block_type(block)
        html_node = HTMLNode(block, block_type) 
        html_node.props: list = inline_to_html(block, block_type)
        parent_html_node.append(html_node)


# Func to deal with inline
def inline_to_html(block, block_type):
    child_nodes: list = []    
    if block_type == BlockType.CODE:
        return code_md_to_html(block)
    markdown_nodes: list = markdown_to_textnode(block)
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

