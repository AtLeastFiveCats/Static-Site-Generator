from blocktype import BlockType, block_to_block_type
from split_blocks import markdown_block_splitter
from text_to_nodes import markdown_to_textnode
from textnode import TextType, TextNode
from enum import Enum
from parentnode import ParentNode
from leafnode import LeafNode

# Helper func for child
def child_md_to_html(block: str):
    stripper: str = block.replace("\n", " ")
    inline_node = markdown_to_textnode(stripper)
    child = LeafNode(tag = text_type_to_tag(inline_node.text_type), value = inline_node.text)
    return child

# Helper func for code block child
def child_code_md_to_html(code):
    pass

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
            return "c"

        case TextType.QUOTE:
            return "q"

        case TextType.LINK:
            return "a"

        case TextType.IMAGE:
            return "img"

# Func to split text into blocks
def markdown_to_blocks(markdown: str):
    blocks: list = markdown_block_splitter(markdown)
    for block: str in blocks:
        block_type: str = block_to_block_type(block)

        match block_type:
            case BlockType.PARAGRAPH:
                # add the parentnode with the appropriate tag that calls child_md_to_html
                parent = ParentNode(tag = "p", children = child_md_to_html(block))

            case BlockType.HEADING:

            case BlockType.QUOTE:

            case BlockType.UNORDERED_LIST:

            case BlockType.ORDERED_LIST:

            case BlockType.CODE:

