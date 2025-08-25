from blocktype import BlockType, block_to_block_type
from split_blocks import markdown_block_splitter
from text_to_nodes import markdown_to_textnode
from textnode import TextType, TextNode
from enum import Enum
from parentnode import ParentNode
from leafnode import LeafNode
import re

# Helper func for child
def child_md_to_html(block: str):
    stripper: str = re.sub(r" +", " ", block.replace("\n", " "))
    inline_node = markdown_to_textnode(stripper)
    child_list: list = []
    for node in inline_node:
        child = LeafNode(tag = text_type_to_tag(node.text_type), value = node.text)
        child_list.append(child)
    return child_list

# Helper func for code block child
def child_code_md_to_html(code):
    # Might need to strip the ```
    code_content: str = code[3:-3]
    if code_content.startswith("\n"):
        lines = code_content.split("\n")
        code_content = [line.lstrip() for line in lines]
        joined_code = "\n".join(code_content)
        #        code_content = code_content[5:]
    html_code = LeafNode(value = joined_code)
    code_list = [html_code]
    return code_list

# Helper func to convert tag
def text_type_to_tag(text_type: str):
    match text_type:
        case TextType.TEXT:
            return None
        
        case TextType.BOLD:
            return "b"
        
        case TextType.ITALIC:
            return "i"

        case TextType.CODE:
            return "code"

        case TextType.QUOTE:
            return "q"

        case TextType.LINK:
            return "a"

        case TextType.IMAGE:
            return "img"

# Helper func to wrap list items in li tags
def li_helper(block):
    return ParentNode(tag = "li", children = child_md_to_html(block))

# Func to split text into blocks
def markdown_to_blocks(markdown: str):
    blocks: list = markdown_block_splitter(markdown)
    parent_list: list = []
    for block in blocks:
        block_type: str = block_to_block_type(block)

        match block_type:
            case BlockType.PARAGRAPH:
                # add the parentnode with the appropriate tag that calls child_md_to_html
                parent = ParentNode(tag = "p", children = child_md_to_html(block))

            case BlockType.HEADING:
                number = 0
                heading: str = ""
                for i in range(6):
                    heading += "#"
                    if block.startswith(f"{heading}"):
                        number = i
                parent = ParentNode(tag = "h{number}", children = child_md_to_html(block))

            case BlockType.QUOTE:
                parent = ParentNode(tag = "blockquote", children = child_md_to_html(block))

            case BlockType.UNORDERED_LIST:
                li_child = li_helper(block)
                parent = ParentNode(tag = "ul", children = li_child)

            case BlockType.ORDERED_LIST:
                li_child = li_helper(block)
                parent = ParentNode(tag = "ol", children = li_child)

            case BlockType.CODE:
                code_tag = ParentNode(tag = "code", children = child_code_md_to_html(block))
                parent = ParentNode(tag = "pre", children = [code_tag])
        parent_list.append(parent)
    
    div_node = ParentNode(tag = "div", children = parent_list)
    return div_node
