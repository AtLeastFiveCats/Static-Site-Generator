from blocktype import BlockType, block_to_block_type
from split_blocks import markdown_block_splitter
from text_to_nodes import markdown_to_textnode
from textnode import TextType
from enum import Enum
from parentnode import ParentNode
from leafnode import LeafNode

# Func to split text into blocks
def markdown_to_blocks(markdown: str):

