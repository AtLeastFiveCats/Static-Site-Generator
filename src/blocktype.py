from enum import Enum
from textnode import TextType
class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"

def block_to_block_type(block):
    if not block:
        return BlockType.PARAGRAPH

    if block[0].startswith("```") and block[-1].endswith["```"]:
        return BlockType.CODE
    
    beginning = block[0]
    heading = ""
    for i in range(6):
        heading += "#"
        if beginning.startswith(f"{heading} "):
            return BlockType.PARAGRAPH

    if all(text.startswith("> ") for text in block):
        return BlockType.QUOTE

    elif all(text.startswith("- ") for text in block):
        return BlockType.UNORDERED_LIST
 
    elif text.startswith(f"{expected_number}. "):
            return BlockType.ORDERED_LIST
        
    else:
        return BlockType.PARAGRAPH 

